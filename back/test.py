import tensorflow as tf
# 检查tensorflow是否得到CUDA支持，安装成功则显示true，否则为false
tf.test.is_built_with_cuda()
# 检查tensorflow是否可以获取到GPU，安装成功则显示true，否则为false
tf.test.is_gpu_available()
import os
command = 'ping www.baidu.com ' #可以直接在命令行中执行的命令
r = os.popen(command) #执行该命令
info = r.readlines()  #读取命令行的输出到一个list
for line in info:  #按行遍历
    line = line.strip('\r\n')
    print('res'+line)