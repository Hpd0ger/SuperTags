# SuperTags
一个Burpsuite插件，用于检测隐藏的XSS，需要安装Jython环境：https://blog.csdn.net/sinat_25449961/article/details/77374407

在挖掘SRC的过程中，发现了很多参数回显到html的情况，但往往是一些不可视标签，容易被忽略。

# How it Works
自动监听HTTP请求。获取包括但不限于get、cookie、reffer等参数，并查询response中的标签是否含有该值


# Demo
![](http://static.zybuluo.com/1160307775/k6jqghl8fgk7de1r8s4vw17u/image_1d76pe1bihb110g88k617aqgha9.png)

可以看到test参数可以利用，结果在Output中查看
![](http://static.zybuluo.com/1160307775/5hlk0q563e4rpwv29mujrljq/image_1d76phstmb8d1vqo1l1j1b4m1ba213.png)
