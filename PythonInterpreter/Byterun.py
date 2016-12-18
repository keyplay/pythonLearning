#! python2.7
# -*- coding: utf-8 -*-
# Byterun.py - a python interpreter implemented in python

import dis

class VirtualMachineError(Exception):
    pass
    
class VirtualMachine(object):
    def __init__(self):
        self.frames = []     # The call stack of frames.
        self.frame = None    # The current frame.
        self.return_value = None
        self.last_exception = None
        
    def run_code(self, code, global_names=None, local_names=None):
        """ An entry point to execute code using the virtual machine."""
        frame = self.make_frame(code, global_names=global_names, 
                                local_names=local_names)
        self.run_frame(frame)
    
    # Frame manipulation
    def make_frame(self, code, callargs={}, global_names=None, local_names=None):
        if global_names is not None and local_names is not None:
            local_names = global_names
        elif self.frames:
            global_names = self.frames.global_names
            local_names = {}
        else:
            global_names = local_names = {                
                '__builtins__': __builtins__,
                '__name__': '__main__',
                '__doc__': None,
                '__package__': None,
            }
        local_names.update(callargs)
        frame = Frame(code, global_names, local_names, self.frame)
        return frame
        
    def push_frame(self, frame):
        self.frames.append(frame)
        self.frame = frame
        
    def pop_frame(self):
        self.frames.pop()
        if self.frames:
            self.frame = self.frames[-1]
        else:
            self.frame = None
    
    def dispatch(self, byte_name, argument):
        """ Dispatch by bytename to the corresponding methods.
          Exceptions are caught and set on the virtual machine."""
        why = None
        try:
            bytecode_fn = getattr(self, 'byte_%s' % byte_name, None)
            if bytecode_fn is None:
                if byte_name.startswith('UNARY_'):
                    self.unaryOperator(byte_name[6:])
                elif byte_name.startswith('BINARY_'):
                    self.binaryOperator(byte_name[7:])
                else:
                    raise VirtualMachineError(
                        "unsupported bytecode type: %s" % byte_name
                    )
            else:
                why = bytecode_fn(*argument)
        except:
            # deal with exceptions encountered while executing the op.
            self.last_exception = sys.exc_info()[:2] + (None,)
            why = 'exception'

        return why
    
    def run_frame(self):
        pass
    
    # Data stack manipulation
    def top(self):
        return self.frame.stack[-1]
        
    def pop(self):
        return self.frame.stack.pop()
        
    def push(self, *vals):
        self.frame.stack.extend(vals)
        
    def popn(self, n):
        """Pop a number of values from the value stack.
          A list of `n` values is returned, the deepest value first.
          """
        if n:
            ret = self.frame.stack[-n:]
            self.frame.stack[-n:] = []
            return ret
        else:
            return []
            
    def parse_byte_and_args(self):
        f = self.frame
        opoffset = f.last_instruction
        byteCode = f.code_obj.co_code[opoffset]
        f.last_instruction += 1
        byte_name = dis.opname[byteCode]
        if byteCode >= dis.HAVE_ARGUMENT:
            # index into the bytecode
            arg = f.code_obj.co_code[f.last_instruction:f.last_instruction+2]
            f.last_instruction += 2       # advance the instruction pointer
            arg_val = arg[0] + (arg[1] * 256)
            if byteCode in dis.hasconst:    # Look up a constant
                arg = f.code_obj.co_consts[arg_val]
            elif byteCode in dis.hasname:   # Look up a name
                arg = f.code_obj.co_names[arg_val]
            elif byteCode in dis.haslocal:  # Look up a local name
                arg = f.code_obj.co_varnames[arg_val]
            elif byteCode in dis.hasjrel:   # Calculate a relative jump
                arg = f.last_instruction + arg_val
            else:
                arg = arg_val
            argument = [arg]
        else:
            argument = []
            
        return byte_name, argument
        
class Frame(object):
    def __init__(self, code_obj, global_names, local_names, prev_frame):
        self.code_obj = code_obj
        self.global_names = global_names
        self.local_names = local_names
        self.prev_frame = prev_frame
        self.stack = []
        if prev_frame:
            self.buildin_names = prev_frame.buildin_names
        else:
            self.buildin_names = local_names['__builtins__']
            if hasattr(self.buildin_names, '__dict__'):
                self.buildin_names = self.buildin_names.__dict__
                
        self.last_instruction = 0
        self.block_stack = []
        
class Function(object):
    """
    Create a realistic function object, defining the things the interpreter expects.
    """
    __slots__ = [
        'func_code', 'func_name', 'func_defaults', 'func_globals',
        'func_locals', 'func_dict', 'func_closure',
        '__name__', '__dict__', '__doc__',
        '_vm', '_func',
    ]

    def __init__(self, name, code, globs, defaults, closure, vm):
        """You don't need to follow this closely to understand the interpreter."""
        self._vm = vm
        self.func_code = code
        self.func_name = self.__name__ = name or code.co_name
        self.func_defaults = tuple(defaults)
        self.func_globals = globs
        self.func_locals = self._vm.frame.f_locals
        self.__dict__ = {}
        self.func_closure = closure
        self.__doc__ = code.co_consts[0] if code.co_consts else None

        # Sometimes, we need a real Python function.  This is for that.
        kw = {
            'argdefs': self.func_defaults,
        }
        if closure:
            kw['closure'] = tuple(make_cell(0) for _ in closure)
        self._func = types.FunctionType(code, globs, **kw)

    def __call__(self, *args, **kwargs):
        """When calling a Function, make a new frame and run it."""
        callargs = inspect.getcallargs(self._func, *args, **kwargs)
        # Use callargs to provide a mapping of arguments: values to pass into the new 
        # frame.
        frame = self._vm.make_frame(
            self.func_code, callargs, self.func_globals, {}
        )
        return self._vm.run_frame(frame)

    def make_cell(value):
        """Create a real Python closure and grab a cell."""
        # Thanks to Alex Gaynor for help with this bit of twistiness.
        fn = (lambda x: lambda: x)(value)
        return fn.__closure__[0]
