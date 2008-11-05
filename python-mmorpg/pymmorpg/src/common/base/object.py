# -*- coding: utf8 -*-
#中文？
class ISaveable:
    def Save(self):
        pass

class ILoadable:   
    def Load(self):
        pass
    
class ISerializeable:
    def Serialize(self):
        pass
    
    def Unserialize(self):
        pass
    
class Object(ISerializeable):
    def SetAttribute(self,attr,value):
        setattr(self,'s_'+attr,value)
        return
    
    def GetAttribute(self,attr,default):
        return getattr(self,'s_'+attr,default)
    
    
    
