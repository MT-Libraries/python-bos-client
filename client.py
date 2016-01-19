#!/usr/bin/env python
#coding=utf-8

#导入系统模块
import sys

#导入客户端模块
import bos.bos_client as bos_client

#主程序入口
def main():    

    # 初始化bos服务
    client = bos_client.PythonBosClient()
    argv = sys.argv
      
    # 返回对应的函数                                        
    def case(argv):                                
        return {
            'list': client.list_objects,
            'del':  client.del_objects,
            'dels': client.dels_objects
        }.get(argv, None)   
    
    def default():
        pass
               
    # print client.list_objects    
    # client.list_objects("live-implements","flash/")    
    # client.del_objects("live-implements","lve-gapbiak6k0c5b0em/")
    # func("live-implements","flash/")                
    
    # 获取方法与参数                    
    func = case(argv[1])                           
    bucket_name = argv[2]
    option_param = ""
    
    if len(argv) < 4:
        option_param = ""        
    else:
        option_param = argv[3]        
    
    # 执行对应的方法            
    if func == None:
        print "\nUsage:\n\tpython client.py {del || dels || list} {bucket_name} {prefix || key_name}\n"
    else:    
        func(bucket_name,option_param)   
                   
if __name__ == '__main__':
    main()