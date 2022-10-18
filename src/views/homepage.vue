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
          <div class="type-btn" @click="typeSelectDlg = false;currentStep=0">
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
          <a-step @click="currentStep = 2" title="参数调节" />
          <a-step @click="currentStep = 3" title="训练" />
          <a-step @click="currentStep = 4" title="结果" />
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
              <div class="blue-btn" @click="currentStep = 1"><span>使用</span></div>
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
          <div class="blue-btn cursor-pointer"><span>模型库</span></div>
          <div class="gray-btn cursor-pointer" @click="jumpTo('matheditor')"><span>创建</span></div>
        </div>
        <div>
          <div class="model-list flex justify-center items-center">
            <div class="model-img"><img :src="getImage('home-card1')" /></div>
            <div class="model-title">
              <p>多层感知器</p>
              <p>Multi-Layer Perception (MLP)</p>
            </div>
            <div class="blue-btn cursor-pointer" @click="currentStep = 2"><span>使用</span></div>
            <div class="model-arrow cursor-pointer" @click="modelScript = !modelScript">
              <img v-show="!modelScript" :src="getImage('model-arrow')" />
              <img v-show="modelScript" :src="getImage('model-arrow-up')" />
            </div>
          </div>
          <div class="model-script" style="background: #FCFBF8;" v-show="modelScript">
            <div class="script-title">认识MLP</div>
            <div class="script-p">MLP由三层组成——输入层、隐藏层和输出层。输入层仅接收输入，隐藏层处理输入，输出层生成结果。基本上，每一层都要训练权值。
              使用MLP用于：Tabular data 列表数据，Image data 图像数据，Text data 文本数据。</div>
            <div class="script-title">多层感知器的优势</div>
            <div class="script-p">多层感知器能够学习任意非线性函数。因此，这些网络被普遍称为通用函数逼近器。通用逼近背后的主要原因之一是激活函数(activation
              function)。激活函数将非线性特征引入网络中，有助于网络学习输入和输出之间的复杂关系。</div>
            <div class="script-img flex justify-center"><img :src="getImage('img_mlp')"/></div>
            <div class="script-title">关于MLP更多学习入口</div>
            <div class="script-link"><a>Crash Course in Convolutional Neural Networks for Machine Learning</a></div>
            <div class="script-link"><a>Crash Course in Convolutional Neural Networks for Machine Learning</a></div>
            <div class="script-title">模型编辑器</div>
            <div class=" block">
              <mathEditor :isShowTitle="false" :isShowFoot="false"></mathEditor>
            </div>
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
      <div class="flex justify-center items-center" v-show="currentStep == 2" style="margin:0 100px">
        <div class="w-80">
          <div class="border rounded h-14 flex justify-center items-center font-p">超参数</div>
          <div>
            <div>
              <div>
                <div>
                  <a-checkbox v-model:checked="checked">Checkbox</a-checkbox>
                  <!-- <img :src="getImage('icon_back')" /> -->
                </div>
                <div class="pl-8">
                  <div class="my-2"><a-checkbox v-model:checked="checked">Checkbox</a-checkbox></div>
                  <div class="my-2"><a-checkbox v-model:checked="checked">Checkbox</a-checkbox></div>
                  <div class="my-2"><a-checkbox v-model:checked="checked">Checkbox</a-checkbox></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- <div>
          <div class="data-btn">
            <div class="gray-btn"><span>查看</span></div>
            <div class="blue-btn"><span>使用</span></div>
          </div>
          <div></div>
        </div> -->
      </div>
    </div>
  </div>
  <div v-show="mainDlg == 'doc'" style="background: #E5E5E5;height: 100vh;">
    <div class="ai-header flex items-center" style="box-shadow: none;height: 104px;">
      <img class="header-img" :src="getImage('icon_back')" @click="mainDlg = 'main'" />
      <div class="blue-btn cursor-pointer" style="position: absolute;right: 50px;" @click="mainDlg = 'main';currentStep = 1"><span>使用</span></div>
    </div>
    <div class="flex justify-center items-center" style="margin-top:32px">
      <div class="doc_side">
        <div class="doc_data flex items-center relative">
          <div class="absolute left-2" style="">数据集</div>
          <img class="absolute right-2 cursor-pointer" :src="getImage('icon_add_file')" />
        </div>
        <ul class="doc_type">
          <li class="flex items-center relative h-12 cursor-pointer" :class="{cur:doc_type == 'cat'}" @click="doc_type = 'cat'">
            <p class="absolute left-2" style="color: #121212;">Cat</p>
            <p class="absolute right-2" style="color: #979797;">500</p>
          </li>
          <li class="flex items-center relative h-12 cursor-pointer" :class="{cur:doc_type == 'dog'}" @click="doc_type = 'dog'">
            <p class="absolute left-2" style="color: #121212;">Dog</p>
            <p class="absolute right-2" style="color: #979797;">500</p>
          </li>
        </ul>
      </div>
      <div class="doc_main px-14 py-7">
        <div class="doc_upload h-12 flex items-center">
          <img class="mx-4 my-3 cursor-pointer" :src="getImage('icon_upload')" />
        </div>
        <div class="doc_imgs flex items-center flex-wrap">
          <div class="relative" v-for="item in 20">
            <img class="mx-4 my-3 w-40 h-36" :src="getImageDataset(String(item))" />
            <img class="absolute top-5 right-6" :src="getImage('icon_delete')" />
            <div class="absolute bottom-5 left-6 px-2 text-center rounded" style="background: #FF3B5C;color: #ffffff;">{{doc_type}}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";
import mathEditor from "./matheditor.vue"
const router = useRouter()
const route = useRoute()
const currentStep = ref(0);
let typeSelectDlg = ref(true)
let mainDlg = ref('main')
let checked = ref(true)
let doc_type = ref('cat')
let modelScript = ref(false)
const getImage = (name: string): string => {
  return new URL(`../assets/images/home/${name}.png`, import.meta.url).href;
};
const getImageDataset = (name: string): string => {
  return new URL(`../assets/images/home/${doc_type.value}/${name}.jpg`, import.meta.url).href;
};

const jumpTo = (route:string) => {
  router.push({name: route})
}
onMounted(() => {
  console.log(route)
  if(route.params.currentStep){
    typeSelectDlg.value = false
    currentStep.value = Number(route.params.currentStep)
  }
})
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

.doc_side {
  background-color: #ffffff;
  border-radius: 8px;
  margin-right: 24px;
  width: 244px;
  height: 800px;
  box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.08);
}

.doc_main {
  background-color: #ffffff;
  border-radius: 8px;
  width: 1164px;
  height: 800px;
}

.doc_data {
  height: 48px;
  font-family: 'Proxima Nova';
  font-style: normal;
  font-weight: 600;
  font-size: 16px;
  line-height: 24px;
  color: #8A8A8A;
}

.doc_type {
  font-family: 'Proxima Nova';
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 22px;
}

.doc_type .cur {
  background: #FEEDEF;
}

.doc_type .cur p:first-child {
  color: #F60457 !important;
}
.font-p{
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 500;
  font-size: 24px;
  color: #4844A3;
}
</style>