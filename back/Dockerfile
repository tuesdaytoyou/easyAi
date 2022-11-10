FROM tensorflow/tensorflow
# FROM tensorflow/tensorflow:devel-gpu 

WORKDIR /code

ADD requirements.txt tensor_api.py /code/
RUN pip3 install -r /code/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# RUN pip3 install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple

ADD . /code
CMD ["python", "./tensor_api.py"]

# # 基于镜像基础
# FROM python:3.9-alpine
# # 创建代码文件夹工作目录 /code 
# RUN mkdir /code 
# # 复制当前代码文件到容器中 /code 
# COPY . /code 
# # 安装所需的包
# RUN pip install -r /code/requirements.txt
# # 指定cmd的工作目录 /code
# WORKDIR /code
# CMD ["python", "./tensor_api.py"]