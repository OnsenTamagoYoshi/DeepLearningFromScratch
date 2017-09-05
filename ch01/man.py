# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 22:00:21 2017

@author: win8_VM_user
"""

class Man:
    def __init__(self, name):
        self.name = name
        print("Inityalized!")
        
    def hello(self):
        print("Hello " + self.name + "!")
        
    def goodbye(self):
        print("Good-bye " + self.name + "!")
        
m = Man("David")
m.hello()
m.goodbye()
