all: pwn pwn_debug

pwn: pwn.c
	gcc ./pwn.c -o pwn -fstack-protector-all -pie -z now -z noexecstack -O0 -w
	strip ./pwn

pwn_debug: pwn.c
	gcc ./pwn.c -o pwn_debug -fstack-protector-all -pie -z now -z noexecstack -O0 -g3

clean:
	rm -rf ./pwn ./pwn_debug


#栈保护：
    #-fstack-protector: 启用栈保护，检测栈溢出
    #-fstack-protector-all: 同上，但对所有函数应用栈保护。
    #-fno-stack-protector: 禁用栈保护，不检测栈溢出
#PIE（位置独立执行）：
    #-fPIE: 生成位置独立可执行文件。
    #-pie: 链接时启用位置独立执行。
    #-no-pie: 关闭位置独立执行。
#NX（不可执行栈）：
    #-z noexecstack: 禁用栈上代码执行。
    #-z execstack: 启用栈上代码执行
#ASLR（地址空间布局随机化）：
    #-z now: 立即启用 ASLR。'''