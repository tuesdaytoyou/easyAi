<template>
  <div v-show="mainDlg == 'main'">
    <div class="ai-header flex items-center">
      <img class="header-img" :src="getImage('icon_mu')" />
      <div class="header-title">交互式机器学习模型</div>
    </div>
    <div class="flex justify-center items-center" style="margin-top:107px" v-if="typeSelectDlg">
      <div class="type-box">
        <div>
          <img class="type-image" :src="getImage('home-card1')" />
        </div>
        <div>
          <p class="type-title">图像分类</p>
          <p class="type-p">分类识别是监督式机器学习最常见的使用场景。</p>
          <div class="type-btn" @click="typeSelectDlg = false">
            <span>开始学习</span>
          </div>
        </div>
      </div>
      <div class="type-box">
        <div>
          <img class="type-image" :src="getImage('home-card2')" />
        </div>
        <div>
          <p class="type-title">文本翻译</p>
          <p class="type-p">文本翻译是最常见的机器学习应用方向，这里XXX。</p>
          <div class="type-btn">
            <span>开始学习</span>
          </div>
        </div>
      </div>
      <div class="type-box">
        <div>
          <img class="type-image" :src="getImage('home-card3')" />
        </div>
        <div>
          <p class="type-title">预测</p>
          <p class="type-p">分类识别是监督式机器学习最常见的使用场景。</p>
          <div class="type-btn">
            <span>开始学习</span>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <div style="margin: 50px 100px">
        <a-steps v-model:current="currentStep">
          <a-step @click="currentStep = 0" title="数据集" />
          <a-step @click="currentStep = 1" title="模型" />
          <a-step @click="currentStep = 3" title="参数调节" />
          <a-step @click="currentStep = 4" title="训练" />
          <a-step @click="currentStep = 5" title="结果" />
        </a-steps>
      </div>
      <div class="flex justify-center items-center" style="margin-top:107px" v-show="currentStep == 0">
        <div class="data-box">
          <div class="flex justify-center items-center" style="height:220px">
            <img class="data-image" :src="getImage('data_dog')" />
          </div>
          <div>
            <p class="data-title">猫狗识别</p>
            <p class="data-p">该数据集包含猫狗照片各5000张。</p>
            <div class="data-btn">
              <div class="gray-btn" @click="mainDlg = 'doc'"><span>查看</span></div>
              <div class="blue-btn"><span>使用</span></div>
            </div>
          </div>
        </div>
        <div class="data-box">
          <div class="flex justify-center items-center" style="height:220px">
            <img class="data-image" :src="getImage('data_number')" />
          </div>
          <div>
            <p class="data-title">手写数字识别</p>
            <p class="data-p">该数据集包含10000张书写数字。</p>
            <div class="data-btn">
              <div class="gray-btn"><span>查看</span></div>
              <div class="blue-btn"><span>使用</span></div>
            </div>
          </div>
        </div>
        <div class="data-box">
          <div class="flex flex-col justify-center items-center h-full data-add">
            <img class="data-image" :src="getImage('data_add')" />
            <div>创建你自己的分类数据集</div>
          </div>
        </div>
      </div>
      <div v-show="currentStep == 1" style="margin:0 100px">
        <div class="flex">
          <div class="blue-btn"><span>模型库</span></div>
          <div class="gray-btn"><span>创建</span></div>
        </div>
        <div>
          <div class="model-list flex justify-center items-center">
            <div class="model-img"><img :src="getImage('home-card1')" /></div>
            <div class="model-title">
              <p>多层感知器</p>
              <p>Multi-Layer Perception (MLP)</p>
            </div>
            <div class="blue-btn"><span>使用</span></div>
            <div class="model-arrow"><img :src="getImage('model-arrow')" /></div>
          </div>
          <div class="model-script">
            <div class="script-title">认识MLP</div>
            <div class="script-p">MLP由三层组成——输入层、隐藏层和输出层。输入层仅接收输入，隐藏层处理输入，输出层生成结果。基本上，每一层都要训练权值。
              使用MLP用于：Tabular data 列表数据，Image data 图像数据，Text data 文本数据。</div>
            <div class="script-title">多层感知器的优势</div>
            <div class="script-p">多层感知器能够学习任意非线性函数。因此，这些网络被普遍称为通用函数逼近器。通用逼近背后的主要原因之一是激活函数(activation
              function)。激活函数将非线性特征引入网络中，有助于网络学习输入和输出之间的复杂关系。</div>
            <div class="script-img"><img /></div>
            <div class="script-title">关于MLP更多学习入口</div>
            <div class="script-link"><a>Crash Course in Convolutional Neural Networks for Machine Learning</a></div>
            <div class="script-link"><a>Crash Course in Convolutional Neural Networks for Machine Learning</a></div>
            <div class="script-img"><img /></div>
          </div>
          <div class="model-list flex justify-center items-center">
            <div class="model-img"><img :src="getImage('home-card1')" /></div>
            <div class="model-title">
              <p>多层感知器</p>
              <p>Multi-Layer Perception (MLP)</p>
            </div>
            <div class="blue-btn"><span>使用</span></div>
            <div class="model-arrow"><img :src="getImage('model-arrow')" /></div>
          </div>
          <div class="model-list flex justify-center items-center">
            <div class="model-img"><img :src="getImage('home-card1')" /></div>
            <div class="model-title">
              <p>多层感知器</p>
              <p>Multi-Layer Perception (MLP)</p>
            </div>
            <div class="blue-btn"><span>使用</span></div>
            <div class="model-arrow"><img :src="getImage('model-arrow')" /></div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-show="mainDlg == 'doc'" style="background: #E5E5E5;">
    <div class="ai-header flex items-center">
      <img class="header-img" :src="getImage('icon_back')" />
      <div class="blue-btn" style="position: absolute;right: 50px;"><span>使用</span></div>
    </div>
    <div class="flex justify-center items-center">
      <div class="doc_side">
        <div class="doc_data"></div>
        <ul class="doc_type">
          <li></li>
        </ul>
      </div>
      <div class="doc_main">
        <div class="doc_upload"></div>
        <div class="doc_imgs">

        </div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { ref } from "vue";
const getImage = (name: string): string => {
  return new URL(`../assets/images/home/${name}.png`, import.meta.url).href;
};
const currentStep = ref(0);
let typeSelectDlg = ref(true)
let mainDlg = ref('main')
</script>
<style scoped>
p {
  margin: 0;
}
.header-img {
  margin-left: 50px;
  cursor: pointer;
}
.header-title {
  margin-left: 10px;
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 40px;
  line-height: 56px;
}
.data-add {
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 28px;
}
.data-add img {
  cursor: pointer;
}
.data-add div {
  margin-top: 20px;
}
.doc_side{
  width: 244px;
  height: 859px;
}
.doc_main{
  width: 1164px;
  height: 859px;
}
</style>