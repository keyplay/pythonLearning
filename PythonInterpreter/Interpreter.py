#! python2.7
# -*- coding: utf-8 -*-
# Interpreter.py - a python interpreter implemented in python


what_to_execute = {
    "instructions": [("LOAD_VALUE", 0),
                     ("STORE_NAME", 0),
                     ("LOAD_VALUE", 1),
                     ("STORE_NAME", 1),
                     ("LOAD_NAME", 0),
                     ("LOAD_NAME", 1),
                     ("ADD_TWO_VALUES", None),
                     ("PRINT_ANSWER", None)],
    "numbers": [1, 2],
    "names":   ["a", "b"] }

class Interpreter:
    def __init__(self):
        self.stack = []          # store the values
        self.environment = {}    # keep track of what names are bound to what values

    # pushing the number onto the stack
    def LOAD_VALUE(self, number):
        self.stack.append(number)
    
    # pop the result back off the stack and print it
    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)

    # pop both numbers off, add them together, and push the result onto the stack
    def ADD_TWO_VALUES(self):
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        total = first_num + second_num
        self.stack.append(total)
    
    # store the value of a variable
    def STORE_NAME(self, name):
        val = self.stack.pop()
        self.environment[name] = val
    
    # retrieve the value of a variable
    def LOAD_NAME(self, name):
        val = self.environment[name]
        self.stack.append(val)
    
    def parse_argument(self, instruction, argument, what_to_execute):
        numbers = ['LOAD_VALUE']
        names = ['LOAD_NAME', 'STORE_NAME']
        
        if instruction in numbers:
            argument = what_to_execute['numbers'][argument]
        elif instruction in names:
            argument = what_to_execute['names'][argument]
            
        return argument
    
    def run_code(self, what_to_execute):
        instructions = what_to_execute['instructions']
        for step in instructions:
            instruction, argument = step
            argument = self.parse_argument(instruction, argument, what_to_execute)
            bytecode_method = getattr(self, instruction)
            if argument is None:
                bytecode_method()
            else:
                bytecode_method(argument)
                
                
interpreter = Interpreter()
interpreter.run_code(what_to_execute)
