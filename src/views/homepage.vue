<template>
  <div class="ai-header"></div>
  <div class="flex justify-center items-center" style="margin-top:107px" v-show="false">
    <div class="type-box">
      <div>
        <img class="type-image" :src="getImage('home-card1')" />
      </div>
      <div>
        <p class="type-title">图像分类</p>
        <p class="type-p">分类识别是监督式机器学习最常见的使用场景。</p>
        <div class="type-btn">
          <span>开始学习</span>
        </div>
      </div>
    </div>
    <div class="type-box">
      <div>
        <img class="type-image" :src="getImage('home-card2')" />
      </div>
      <div>
        <p class="type-title">图像分类</p>
        <p class="type-p">分类识别是监督式机器学习最常见的使用场景。</p>
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
        <p class="type-title">图像分类</p>
        <p class="type-p">分类识别是监督式机器学习最常见的使用场景。</p>
        <div class="type-btn">
          <span>开始学习</span>
        </div>
      </div>
    </div>
  </div>
  <div>
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
        <div>
          <img class="data-image" :src="getImage('home-card1')" />
        </div>
        <div>
          <p class="data-title">猫狗识别</p>
          <p class="data-p">该数据集包含猫狗照片各5000张。</p>
          <div class="data-btn">
            <span>开始学习</span>
          </div>
        </div>
      </div>
      <div class="data-box">
        <div>
          <img class="data-image" :src="getImage('home-card1')" />
        </div>
        <div>
          <p class="data-title">猫狗识别</p>
          <p class="data-p">该数据集包含猫狗照片各5000张。</p>
          <div class="data-btn">
            <span>开始学习</span>
          </div>
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
          <div class="model-title"><p>多层感知器</p><p>Multi-Layer Perception (MLP)</p></div>
          <div class="blue-btn"><span>使用</span></div>
          <div class="model-arrow"><img :src="getImage('model-arrow')" /></div>
        </div>
        <div class="model-script">
          <div class="script-title">认识MLP</div>
          <div class="script-p">MLP由三层组成——输入层、隐藏层和输出层。输入层仅接收输入，隐藏层处理输入，输出层生成结果。基本上，每一层都要训练权值。
                                使用MLP用于：Tabular data 列表数据，Image data 图像数据，Text data 文本数据。</div>
          <div class="script-title">多层感知器的优势</div>
          <div class="script-p">多层感知器能够学习任意非线性函数。因此，这些网络被普遍称为通用函数逼近器。通用逼近背后的主要原因之一是激活函数(activation function)。激活函数将非线性特征引入网络中，有助于网络学习输入和输出之间的复杂关系。</div>
          <div class="script-img"><img /></div>
          <div class="script-title">关于MLP更多学习入口</div>
          <div class="script-link"><a>Crash Course in Convolutional Neural Networks for Machine Learning</a></div>
          <div class="script-link"><a>Crash Course in Convolutional Neural Networks for Machine Learning</a></div>
          <div class="script-img"><img /></div>
        </div>
        <div class="model-list flex justify-center items-center">
          <div class="model-img"><img :src="getImage('home-card1')" /></div>
          <div class="model-title"><p>多层感知器</p><p>Multi-Layer Perception (MLP)</p></div>
          <div class="blue-btn"><span>使用</span></div>
          <div class="model-arrow"><img :src="getImage('model-arrow')" /></div>
        </div>
        <div class="model-list flex justify-center items-center">
          <div class="model-img"><img :src="getImage('home-card1')" /></div>
          <div class="model-title"><p>多层感知器</p><p>Multi-Layer Perception (MLP)</p></div>
          <div class="blue-btn"><span>使用</span></div>
          <div class="model-arrow"><img :src="getImage('model-arrow')" /></div>
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
</script>
<style scoped>
p{margin: 0;}
</style>