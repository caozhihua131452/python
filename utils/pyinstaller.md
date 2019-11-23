### pyinstaller

一个打包exe文件的工具

图标下载地址：https://www.iconfont.cn/collections/index?spm=a313x.7781069.1998910419.3

图标转换地址：https://www.easyicon.net/covert/

转换exe命令

``` python
pyinstaller [文件位置\test.py]                不推荐使用

pyinstaller  -F  [文件位置\test.py]           生成exe没有图标
pyinstaller  -F  -i [图片.ico] [文件位置]      生成exe有图表

# 例如   pyinstaller -F -i 1.ico C:\Users\Administrator\Desktop\test\test.py
```





