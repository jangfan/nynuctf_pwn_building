## 搭建ctf用户态pwn题目环境工具
使用apline+xinetd+chroot+patchelf编写的模板
### 特点
1.根据时间戳自动生成flag

2.在指定版本容器中进行编译，并导出libc和pwn文件

3.使用apline简化部署，使用chroot，可以隔离应用程序和系统其他部分的交互
### 运行
将代码写入pwn.c中，并运行build_run.py文件
### 注意
如果指定容器是ubuntu：18.04以及以下版本，在dockerfile中设置设备节点应是
```
FROM ubuntu:18.04
# ......
RUN cp -R /usr/lib* /home/ctf && \
    cp -R /lib* /home/ctf && \
	mkdir /home/ctf/dev && \
    mknod /home/ctf/dev/null c 1 3 && \
    mknod /home/ctf/dev/zero c 1 5 && \
    mknod /home/ctf/dev/random c 1 8 && \
    mknod /home/ctf/dev/urandom c 1 9 && \
    chmod 666 /home/ctf/dev/*
```
ubuntu:23.04及更高版本，需要将用户的uid修改为1001
