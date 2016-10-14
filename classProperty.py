#! python2.7
# -*- coding: utf-8 -*-
# classProperty.py - add some attributes to a class.
  
class Screen(object):
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float, long)):
            raise ValueError('width must be a number!')
        if value <= 0:
            raise ValueError('width must be positive!')
        self._width = value
    
    @property
    def height(self):
        return self._height
        
    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float, long)):
            raise ValueError('height must be a number!')
        if value <= 0:
            raise ValueError('height must be positive!')
        self._height = value
        
    @property
    def resolution(self):
        return self._height * self._width

# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
