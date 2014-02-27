Y@gra
===================


What
===============


一个提供avatar hosting服务的站点

你可以在yagar上管理你的头像

功能:

* 注册（用户名，密码）

* 登录/登出

* 密码修改

* 上传/更换 头像

* 提供头像访问API



Status
----------
Version: 1.1

版本号:1.1


Installation 
===============

Dependency
----------

* Python 2.7:

 	参考网址 [Python 2.7](http://www.python.org/download/releases/2.7/)

* Mysql:

	sudo apt-get install mysql

    	sudo apt-get install mysql-dev
    
 	参考网址 [mysql](http://www.mysql.com/)

* Mysql-python(可使用make init自动安装):

    	pip install mysql-python

 	参考网址 [MySQL for Python](http://sourceforge.net/projects/mysql-python/)


note:

   	make init 自动安装依赖软件(mysql-python)
   	
   	make doc  自动生成使用文档,文档目录在doc/_build下

       

Install
-------



* 进入目录:

   		cd yagra  

* 初次运行创建数据库::

   		mysql -uname -ppassword < dbinit.sql      
   
* 初次运行设置参数(设置一次即可,详细介绍见下文)::

   		vi config.py            

* 运行(使用apache服务器分发请求)::

   		service apache2 start


Configuration 
================


Database Configuration
----------------------

使用dbinit.sql脚本创建数据库

默认创建名字为yagra的数据库,如果存在则会删除后创建

默认创建一个yagra账户(`密码为abcd!1234,与config对应`)并用此用户访问该数据库::



System Configuration
-------------
初始设置系统参数说明(config.py)::

    #######################
    # system Configure ##
    #######################
    #初始运行时设置cookie加密密钥,任意字符串
    COOKIE_SECRET =  'thisis secret' 

    
    
    #######################
    # Database Configure ##
    #######################
    
    #数据库连接设置,依次为IP,端口,用户名,用户密码,数据库名称
    DB_HOST = 'localhost' 
    DB_PORT = 3306
    DB_USER = 'yagra'
    DB_PASSWD = 'abcd!1234'
    DB_NAME = 'yagra'


Documentation
===============  
使用make doc创建项目文档

存储在 /docs/_build/html(首页为index.html)
    


CHANGELOG
===============   

2014.2.27  beta release

2013.2.28  document added

