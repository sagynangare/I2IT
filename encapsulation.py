'''
name mangling
a=> Public
_b=>Protected
__c=>Private

object._classname__varibleName
'''
class Encapsulation:
    def __init__(self):
        self.a ='Public'
        self._b ='Protected'
        self.__c='Private'

obj=Encapsulation()
print(obj.a)
print(obj._b)
print(obj._Encapsulation__c)















