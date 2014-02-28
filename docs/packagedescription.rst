.. _pakage-description:


****************
Layout 工程文件分布及说明
****************



.. _making-a-list:


* docs:  

   开发及使用文档(本网站源代码)

* log:  

   运行时候产生的log信息记录
   
 
* handlers:
   
       逻辑层:响应不同URL的handler 
       

* models:
   
      数据库相关的函数方法,与数据库相关的增删查改方法放在dbapi.py中
       
* static: 
   
      显示层,静态显示的CSS,JS文件
      

* template:
   
      显示层,动态显示的html文件
       

* config.py:  
   
      全局配置文件(数据库配置,服务器配置)
       
* main.py:
   
       服务器启动文件
       
* dbinit.sql:      
   
       初始建立数据库的脚本文件
          
    
* README:  

    项目说明文档


* Makefile:  

   安装脚本

* requirements.txt:  

   安装依赖软件

* LICENSE:  

   版权声明
