#!/usr/bin/env python
#coding=utf-8

#导入BOS相关模块
from baidubce import exception
from baidubce.services import bos
from baidubce.services.bos import canned_acl
from baidubce.services.bos.bos_client import BosClient

#导入BOSClient配置文件
import bos_conf 

class PythonBosClient(object):
    
    def __init__(self):    
        #新建BOSClient
        self._client = BosClient(bos_conf.config)
                
    def list_buckets(self):
        response = self._client.list_buckets()
        for bucket in response.buckets:
            print bucket.name            
    
    def list_objects(self,bucket_name,prefix = ""):
        response = self._client.list_objects(bucket_name,1000,prefix)
        for object in response.contents:
           print object.key  
           
    def del_objects(self,bucket_name,key_name):            
        response = self._client.list_objects(bucket_name,1000,prefix)
        for object in response.contents:                             
            self._client.delete_object(bucket_name,object.key)  
            print object.key + " Deleted"  
                       
    def dels_objects(self,bucket_name,prefix):            
        response = self._client.list_objects(bucket_name,1000,prefix)
        for object in response.contents:                             
            self._client.delete_object(bucket_name,object.key)  
            print object.key + " Deleted"                                                                      