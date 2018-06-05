#进入目录
cd  
cd .. 返回上一层 
cd -  返回到上次的目录
cd ~  快速回到家目录

#查看目录列表
ls
ls -a 查看隐藏文件
ls -l 查看文件的详细信息
ls -lh 把大小转成具体的数值

#新建文件夹
mkdir

#新建文件
touch 

#删除文件
rm

#删除文件夹
rm -r

#分屏显示
more

#重定向
> 覆盖
>> 追加

#管道
一头进
一头出
|

#查看有没有网络
ping www.baidu.com

ctrl+c 终端卡住用ctrl+c

#安装软件

sudo apt update
sudo apt install tree

sudo apt install sl



#编辑文件
gedit

#查看文件内容
cat

#查看当前路径
pwd

#帮助文档
ls --help
man ls


#创建软硬链接
ln -s 
ln

#重命名
mv 

#移动
mv
v
i 
f 

#复制
cp
i 交互式
v 显示进度
f 强制
r 复制目录

#

#通配符
* 任意
？ 任意一个
[1-9]*


#搜索电脑文件
find 搜索路径  -name 'xxx'
find 搜索路径  -size  2M

#搜索文件n内容
grep -nvi '^xxx' 以什么开头
grep -nvi 'xxx$' 以什么结尾

#归档
tar -cvf test.tar *
*归档没有压缩功能

#解档
tar -xvf test.tar

#如果想让数据压缩
gzip -r test.tar test.tar.gz

#解压
gzip -d test.tar.gz

上面两个步骤可以合起来

#gz格式
归档并压缩
tar -zcvf test.tar.gz *

解压缩
tar -zxvf test.tar.gz

#bz2格式
归档并压缩
tar -jcvf test.tar.bz2 *

解压缩
tar -jxvf test.tar.bz2 

#zip格式
归档并压缩
zip test *

解压缩
unzip test.zip

#用户管理

新增
sudo useradd xxx  -m  
-m 在home目录下创建家目录

设置密码
sudo passwd xxx

删除
sudo userdel xxx -r 

-r 删除用户并删除家目录

切换用户

su - xxx

切换root用户

su - root
sudo -s

创建组
sudo groupadd xxx

删除组

sudo groupdel xxx

把用户加到某个组当中
sudo usermod -a -G xxx 用户

文件加权限

sudo chmod 777 文件名

r ------- 4
w ------- 2
x ------- 1

查看进程

ps  -aux
top
htop

杀进程
kill -9 pid

查看ip地址

ifconfig   mac和linux用
ipconfig   windows  cmd上


查看网络是通畅

ping www.baidu.com

查看本机电脑网络设备是否良好

ping 127.0.0.1

关机
init0
shutdown -h now

重启
reboot
shutdown -r now


i: 插入光标前一个字符 

I: 插入行首 

a: 插入光标后一个字符 

A: 插入行未 

o: 向下新开一行,插入行首 

O: 向上新开一行,插入行首

yy: 复制

10yy:复制多行

p: 粘贴

dd：删除

3dd：删除多行

dd:剪切

dw:以单词是删除

d0：删除光标前

h:光标左移
j:光标下移
k:光标上移
l:光标右移

M：当前屏幕中间
L: 当前最后一行
G: 文件末尾
gg:移动文件开头


ctrl+d 向下翻半屏
ctrl+u 向上翻半屏

ctrl+f 向下翻一屏
ctrl+b 向上翻一篇

shift+} 向下按段走
shitf+{ 向上按段走

u 撤销
ctrl+r 反撤销

/xx  
n 向下找
N 向上找

%s/d/888/g  全局替换
1,10s/d/888/g 1到10行替换

w 向后移动一个字
b 向前移动一个字

10G 移动到第10行

x 删除一个字符
X 删除光标前的


v  按字符选中
v  按段选中

shift+>> 向右移动
shift+<< 向左移动

. 重复上一次命令

r 替换光标当前字符
R 替换光标后面的字符



wq! 保存并退出
x 保存并退出
shift+zz 保存并退出

1  执行
2  写
3  可写可执行
4  可读
5  可读可执行
6  可读可写
7  可读可写可执行





n 显示行数
v 取反
i 忽略大小写


作业：
1、命令 周一考  不会百遍起
2、单词
3、简书 Linux常用命令 博客一篇 班长整理简书地址
4、xmind 命令
5、周六下午 李老师讲课 2点开始 
6、周天晚上 邢凯分享搜狗输入安装 sublime安装 分为windows linux


在桌面1805/02day目录下 新建一个以自己的名字为名的目录
在此目录中创建一个11/22/33/44目录
并用tree查看 在33目录下新建1.txt 2.txt 3.txt 4.py 5.tar 6.a文件
并用ls筛选出已txt结尾的文件 重定向到7.txt中 然后 删除44目录 



在桌面上新建一个521文件夹，在521文件夹里面新建520文件夹，在里面创建3个文件分别是1.txt  2.html  3.py  并编辑1.txt写入 我爱你中国。然后查看文件内容


在windows把sublime text3安装上

