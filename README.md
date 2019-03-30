# SuperTags
一个Burpsuite插件，用于检测隐藏的XSS，需要安装Jython环境：https://blog.csdn.net/sinat_25449961/article/details/77374407

对于一些不可视标签，往往存在可以XSS的标签，但是被忽略。

# How it work
自动监听HTTP请求。获取包括但不限于get、cookie、reffer等参数，并查询responce中的标签是否含有该值


# Demo
![](http://static.zybuluo.com/1160307775/k6jqghl8fgk7de1r8s4vw17u/image_1d76pe1bihb110g88k617aqgha9.png)

可以看到test参数可以利用，结果在Output中查看
![](http://static.zybuluo.com/1160307775/5hlk0q563e4rpwv29mujrljq/image_1d76phstmb8d1vqo1l1j1b4m1ba213.png)
