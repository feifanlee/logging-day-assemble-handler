# logging-my-handler

## 解决问题

* 使用配置文件配置logging，并滚动保存日志。
* 将属于同一天的日志文件归档存到对应的目录中。

## 代码文件

> myHandler.py


## 配置方法

* *myHandler.py*放在运行目录中（和代码同级）。
* 配置文件中，handler配置为myHandler.AdHandler
> class=myHandler.AdHandler
* 配置参数为:
    + 日志文件名
    + 日志切分单位（'S','M','H','D')
    + 日志切分长度 (1,2,3 ...)
    + 编码
> args=('./log/abc.log','H',1)

## 实现原理
* 继承```TimedRotatingFileHandler```类
* 在时间滚动前会调用```getFilesToDelete(self)```方法获取需要删除的日志
* 将保留的日志文件数设为1
* 获取将要删除掉的文件后将该文件复制到对应时间（天）的目录中
* 让父类删除该文件继续进行滚动