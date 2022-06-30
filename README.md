# 基于Python和OpenCV的给图形界面增加易用的滑动条功能
## 项目描述
基于OpenCV实现的图像处理和计算机视觉方面的通用算法，我们可以使用creatTrackbar()函数来创建一个滑动条，以调节参数，可以达到按钮的作用，是一个非常实用的功能。通过creatTrackbar()函数和回调函数的配合使用，利用滑动条功能我们可以给图形界面实现颜色、大小和是否出现等变化，并将它们进行组合，以实现不同的需求。
## 演示画面
1. 需要先开启程序on

![]() ![image](https://user-images.githubusercontent.com/107832597/176445622-c793dda8-563e-4cde-87a4-d61c6ae488f1.png)

2.可通过滑动RGB三个通道的滑块来改变数值，以此改变颜色

![]()![image](https://user-images.githubusercontent.com/107832597/176445723-1f61186d-b34f-43ba-9840-3c62f59ae966.png)

![]()<img width="365" alt="image" src="https://user-images.githubusercontent.com/107832597/176446294-982d73e3-abfc-44ec-aadc-5f541beeeb63.png">
## 项目使用说明
### 环境部署
+ Python3.8

+ OpenCV3.4.1(3.4.2以后有些算法申请了专利

+ 编译器pycharm

### Python环境下OpenCV的配置说明
#### Python安装
[python下载链接（windows）](http://www.python.org/downloads/windows/)

安装完成后win+r，输入Python确认，如果安装成功会显示Python版本信息，如下图!
![image](https://github.com/QAQDaisy/Daisy-s/blob/main/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20220629221309.jpg)
#### pycharm安装
[pycharm下载链接](https://www.jetbrains.com/pycharm/download/#section=windows)
##### 配置pycharm
* 首次使用会弹出以下窗口
![df6746e381cad2dfe828f3d32395452a.png](en-resource://database/516:1)

* 如果你之前使用过 pycharm 并有相关的配置文件，则在此处选择；如果没有，默认即可。同意用户使用协议：
![be697b7679396f8f4d2429914e0a85b1.png](en-resource://database/518:1)

* 确定是否需要进行数据共享：
![5ff880ce4f9fcc5919209d0ab9376ebd.png](en-resource://database/520:1)

* 下载插件，你可以根据需要下载，也可以不装。建议只装 MarkDown插件即可：
![9c79a14dd0779cf4a91feaa5c6979745.png](en-resource://database/522:1)

* 在使用过程中，如果出现 Interpreter field is empty 表示 Python 的环境变量有问题。当然我们也可以直接选择，请看下面。选择图中 1，如果 3 位置的下来中选不到 Python.exe， 则点击 2 位置按钮。
![3fdb02d274ac745323b68a8fcbad5e43.png](en-resource://database/524:1)

* 选择图中1， 如果 3 位置依然没有出现 Python.exe，则点击 2 位置按钮选择 Python 的安装目录，找到你安装的 Python 目录，然后选择 Python.exe。（下图3的位置以您安装的python位置为准）
![3393987fda0355b5dee06125d56b1267.png](en-resource://database/526:1)
### 配置OpenCV
* 在pycharm下安装；点击file，选择settings进入
![image](https://github.com/QAQDaisy/Daisy-s/blob/main/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20220629224010.jpg)
* 点击project里+号进入，并且搜索OpenCV-Python
![image](https://github.com/QAQDaisy/Daisy-s/blob/main/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20220629224448.jpg)
* 最后点击install package，等待安装完成。

* 下面是国内的opencv源，直接把链接复制过去点ok；

阿里云 http://mirrors.aliyun.com/pypi/simple/

中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/

豆瓣(douban) http://pypi.douban.com/simple/

清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/

中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/ 

如果在安装过程中遇到问题，详见项目FAQ文件

## 团队介绍
我们小组是热敏电组！:stuck_out_tongue_closed_eyes:
### 指导老师
+ 杨大利老师
### 成员
+ 程思琪（组长）
+ 倪芊睿
+ 孙鉴心
+ 张航
+ 张奕彤

