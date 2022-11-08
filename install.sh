apt-get install nodejs npm
nodejs --version
# https://cloud.tencent.com/developer/article/1649008
# https://repo.anaconda.com/archive/
wget -P /tmp https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
bash /tmp/Anaconda3-2022.10-Linux-x86_64.sh
source ~/.bashrc
# https://cloud.tencent.com/developer/article/1812624
conda update --all
conda init
conda create -n py36 python=3.6.12
conda activate py36
pip install tensorflow-gpu==2.2.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
conda install cudatoolkit=10.1 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/linux-64/
conda install cudnn=7.6.5
# import tensorflow as tf
# # 检查tensorflow是否得到CUDA支持，安装成功则显示true，否则为false
# tf.test.is_built_with_cuda()
# # 检查tensorflow是否可以获取到GPU，安装成功则显示true，否则为false
# tf.test.is_gpu_available()
git clone https://github.com/tuesdaytoyou/easyAi.git
npm install
python tensor_api.py