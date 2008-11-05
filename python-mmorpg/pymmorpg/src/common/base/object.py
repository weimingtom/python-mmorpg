# -*- coding: utf8 -*-
#中文？
class ISaveable:
    def Save(self):
        pass

class ILoadable:   
    def Load(self):
        pass

#序列化接口
class ISerializeable:
    def Serialize(self):#序列化
        pass
    
    def Unserialize(self):#反序列化
        pass
    
class Object(ISerializeable):
    def SetAttribute(self,attr,value):
        setattr(self,'s_'+attr,value)
        return
    
    def GetAttribute(self,attr,default):
        return getattr(self,'s_'+attr,default)
    
    
    
