<template>
  <div v-show="mainDlg == 'main'">
    <div class="ai-header flex items-center">
      <div class="relative">
        <img class="header-img" :src="getImage('icon_mu')" @click="showmenu = !showmenu" />
        <div v-show="showmenu" class="absolute bg-white left-12 z-10">
          <ul class="menu_ul">
            <li class="font_menu flex items-center justify-start w-44 m-2 p-2 pl-4"><img :src="getImage('icon_menu_1')" /><div class="ml-2">新建项目</div></li>
            <li class="font_menu flex items-center justify-start w-44 m-2 p-2 pl-4"><img :src="getImage('icon_menu_2')" /><div class="ml-2">项目列表</div></li>
            <li class="font_menu flex items-center justify-start w-44 m-2 p-2 pl-4"><img :src="getImage('icon_menu_3')" /><div class="ml-2">保存项目</div></li>
            <li class="font_menu flex items-center justify-start w-44 m-2 p-2 pl-4"><img :src="getImage('icon_menu_4')" /><div class="ml-2">打开文件</div></li>
            <li class="font_menu flex items-center justify-start w-44 m-2 p-2 pl-4"><img :src="getImage('icon_menu_5')" /><div class="ml-2">下载文件</div></li>
            <li class="font_menu flex items-center justify-start w-44 m-2 p-2 pl-4"><img :src="getImage('icon_menu_6')" /><div class="ml-2">社区</div></li>
            <li class="font_menu flex items-center justify-start w-44 m-2 p-2 pl-4"><img :src="getImage('icon_menu_7')" /><div class="ml-2">帮助中心</div></li>
            <li class="font_menu flex items-center justify-start w-44 m-2 p-2 pl-4"><img :src="getImage('icon_menu_8')" /><div class="ml-2">个人中心</div></li>
            <li class="font_menu flex items-center justify-start w-44 m-2 p-2 pl-4"><img :src="getImage('icon_menu_9')" /><div class="ml-2">反馈</div></li>
          </ul>
        </div>
      </div>
      <div class="header-title cursor-pointer" v-if="typeSelectDlg" @click="showmenu = !showmenu">Playable ML Module</div>
      <div style="width:668px;margin-left:442px" v-else>
        <a-steps v-model:current="currentStep">
          <a-step title="创建数据集" />
          <a-step title="创建模型" />
          <a-step title="训练" />
          <a-step title="结果" />
        </a-steps>
      </div>
    </div>
    <div class="flex justify-center items-center flex-col" style="margin-top:107px" v-if="typeSelectDlg">
      <div class="font_tip_title" style="margin-left: -1370px;">开始一个新的项目</div>
      <div class="flex justify-center items-center">
        <div class="type-box">
          <div>
            <img class="type-image" :src="getImage('home-card1')" />
          </div>
          <div>
            <p class="type-title">图像分类</p>
            <p class="type-p">分类识别是监督式机器学习最常见的使用场景。</p>
            <p class="type-p" style="color:rgba(153, 153, 153, 0.8);font-size:14px;top: 391px;top:465px">20000人已学习</p>
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
            <p class="type-title">机器翻译</p>
            <p class="type-p">机器翻译是人工智能的终极目标之一，其核心语言理解和语言生成是自然语言处理的两大基本问题。</p>
            <p class="type-p" style="color:rgba(153, 153, 153, 0.8);font-size:14px;top: 391px;top:465px">15000人已学习</p>
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
            <p class="type-title">预测分析</p>
            <p class="type-p">预测分析包括各种统计技术，用于分析当前和历史事实，对未来做出预测。</p>
            <p class="type-p" style="color:rgba(153, 153, 153, 0.8);font-size:14px;top: 391px;top:465px">5000人已学习</p>
            <div class="type-btn">
              <span>开始学习</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <div class="flex justify-center items-center flex-col" style="margin-top:107px" v-show="currentStep == 0">
        <div class="font_tip_title" style="margin-left: -1170px;">创建数据集</div>
        <div class="" style="margin-left: -940px;">你可以直接选择下面的数据集也可以创建你自己的数据集</div>
        <div class="flex justify-center items-center">
          <div class="data-box">
            <div class="flex justify-center items-center border-b-2" style="height:220px">
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
            <div class="flex justify-center items-center border-b-2" style="height:220px">
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
              <div class="w-24 h-24 flex justify-center items-center" style="background:rgba(72, 68, 163, 0.1);">
                <img class="data-image" :src="getImage('data_add')" />
              </div>
              <div>创建你自己的分类数据集</div>
            </div>
          </div>
        </div>
      </div>
      <div v-show="currentStep == 1" style="margin: 0px 0 0 150px;">
        <div class="flex mt-8">
          <div class="blue-btn cursor-pointer"><span>模型库</span></div>
          <div class="gray-btn cursor-pointer" @click="jumpTo('matheditor')"><span>创建</span></div>
        </div>
        <div class="font_tip_title flex my-6">
          以下机器学习模型为经典的分类模型，你可以尝试不同的模型，运行并查看效果
        </div>
        <div>
          <div class="model-list flex justify-center items-center">
            <div class="model-img flex justify-center items-center"><img :src="getImage('img_model1')" /></div>
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
            <div class="model-img flex justify-center items-center"><img :src="getImage('img_model2')" /></div>
            <div class="model-title">
              <p>卷积神经网络</p>
              <p>Convolutional neural networks (CNN)</p>
            </div>
            <div class="blue-btn"><span>使用</span></div>
            <div class="model-arrow"><img :src="getImage('model-arrow')" /></div>
          </div>
          <div class="model-list flex justify-center items-center">
            <div class="model-img flex justify-center items-center"><img :src="getImage('img_model3')" /></div>
            <div class="model-title">
              <p>多层感知器</p>
              <p>Multi-Layer Perception (MLP)</p>
            </div>
            <div class="blue-btn"><span>使用</span></div>
            <div class="model-arrow"><img :src="getImage('model-arrow')" /></div>
          </div>
        </div>
      </div>
      <div class="flex justify-center" v-show="currentStep == 2 || currentStep == 3" style="margin:32px 100px">
        <div class="w-80 bottom-2 rounded mr-3 p-7 bg-white">
          <div class="font_help_title">训练</div>
          <div class="font_help_title border-2 rounded-lg flex justify-center items-center h-14 my-4 cursor-pointer bg-trainBtn hover:bg-trainBtnHover"
               :class="{train_btn:trainState}" @click="handleTrain()">
            <div v-if="trainState"><a-spin :indicator="indicator" />训练中</div>
            <div v-else>训练模型</div>
          </div>
          <div class="font_help_title my-4">
            超参数调节
          </div>
          <div class="border-b">
            <div class="font_help_p inline-block">Epochs</div>
            <img class="inline-block ml-1 mb-1 cursor-pointer" :src="getImage('icon_help')" />
            <div class="my-4">
              <el-input-number style="width:90px" v-model="epochsValue" :min="1" :max="100" controls-position="right"/>
            </div>
          </div>
          <div class="border-b">
            <div class="font_help_p inline-block mt-2">Learning Rate</div>
            <img class="inline-block ml-1 mb-1 cursor-pointer" :src="getImage('icon_help')" />
            <div class="my-4">
              <el-input-number style="width:90px" v-model="rateValue" :step="0.01" :min="0" :max="1" controls-position="right"/>
            </div>
          </div>
          <div class="border-b">
            <div class="font_help_p inline-block mt-2">Batch Size</div>
            <img class="inline-block ml-1 mb-1 cursor-pointer" :src="getImage('icon_help')" />
            <div>
              <a-radio-group v-model:value="batchValue">
                <a-radio :style="radioStyle" :value="16">16</a-radio>
                <a-radio :style="radioStyle" :value="32">32</a-radio>
                <a-radio :style="radioStyle" :value="64">64</a-radio>
                <a-radio :style="radioStyle" :value="128">128</a-radio>
              </a-radio-group>
            </div>
          </div>
          <div class="">
            <div class="font_help_p inline-block mt-2">Optimizer</div>
            <img class="inline-block ml-1 mb-1 cursor-pointer" :src="getImage('icon_help')" />
            <div>
              <a-radio-group v-model:value="optimizerValue">
                <a-radio :style="radioStyle" value="Adam">Adam</a-radio>
                <a-radio :style="radioStyle" value="RMSprop">RMSprop</a-radio>
                <a-radio :style="radioStyle" value="SGD">SGD</a-radio>
                <a-radio :style="radioStyle" value="Adamax">Adamax</a-radio>
                <a-radio :style="radioStyle" value="Adagrad">Adagrad</a-radio>
              </a-radio-group>
            </div>
          </div>
        </div>
        <div class="bottom-2 rounded p-7 bg-white" style="width:1164px">
          <div class="font_help_title">可视化面板</div>
          <div class="relative w-full flex items-center rounded" style="height: 97px;">
            <div class="title-font flex items-center rounded" style="background: #F2F2F2;">
              <span class="px-5 py-2 cursor-pointer" :class="{help_cur: showDLgType == 1}" @click="showDLgType = 1">折线图</span>
              <span class="px-5 py-2 cursor-pointer" :class="{help_cur: showDLgType == 2}" @click="showDLgType = 2">图像可视化</span>
              <span class="px-5 py-2 cursor-pointer" :class="{help_cur: showDLgType == 3}" @click="showDLgType = 3">训练日志</span>
            </div>
            <div class="cursor-pointer ml-4"><img :src="getImage('icon_plus_box')" /></div>
          </div>
          <div class="flex h-3/4">
            <div class="flex items-center flex-col h-full w-full mt-32" v-show="!trainEnd && showDLgType == 1">
              <img :src="getImage('img_train')" />
              <div class="font_tarin">点击训练模型，查看更多数据</div>
            </div>
            <div v-show="trainEnd && showDLgType == 1" style="width: 100%;height: 100%">
              <iframe id="myiframe" width="100%" height="100%" :src="curpreviewurl"></iframe>
            </div>
            <div v-if="showDLgType == 3" style="width: 100%">
              <el-table :data="tableData" style="width: 100%">
                <el-table-column prop="ai_id" label="训练ID" width="150" />
                <el-table-column prop="ai_model" label="AI Module" width="120" />
                <el-table-column prop="ai_rate" label="learning rate" width="120" />
                <el-table-column prop="ai_batch" label="batch size" width="120" />
                <el-table-column prop="ai_optimizer" label="optimizer" width="120" />
                <el-table-column prop="ai_loss" label="Train/loss" width="150" />
                <el-table-column prop="ai_acc" label="Train/acc" width="150" />
                <el-table-column prop="ai_time" label="Submission time" width="150" />
                <el-table-column fixed="right" label="Operations" width="120">
                  <template #default>
                    <el-button link type="primary" size="small">导出</el-button>
                    <el-button link type="primary" size="small">运行</el-button>
                  </template>
                </el-table-column>
              </el-table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-show="mainDlg == 'doc'" style="height: 100vh;">
    <div class="ai-header flex items-center" style="height: 104px;">
      <img class="header-img" :src="getImage('icon_back')" @click="mainDlg = 'main'" />
      <div style="width:668px;margin-left:442px">
        <a-steps v-model:current="currentStep">
          <a-step title="创建数据集" />
          <a-step title="创建模型" />
          <a-step title="训练" />
          <a-step title="结果" />
        </a-steps>
      </div>
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
import axios from 'axios'
import { LoadingOutlined } from '@ant-design/icons-vue';
import { ref, onMounted, reactive, watch, h } from "vue";
import { useRouter, useRoute } from "vue-router";
import { ElMessage } from 'element-plus'
// import mathEditor from "./matheditor.vue"
const router = useRouter()
const route = useRoute()
const currentStep = ref(0);
let typeSelectDlg = ref(true)
let mainDlg = ref('main')
let checked = ref(true)
let doc_type = ref('cat')
let modelScript = ref(false)
let showmenu = ref(false)
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
  document.querySelector('body')!.style.backgroundColor = '#F6F6F6'
  if(route.params.currentStep){
    typeSelectDlg.value = false
    currentStep.value = Number(route.params.currentStep)
  }
})
// watch(currentStep, (newValue, oldValue) => {
//   if(newValue == 2 || newValue == 3) {
//     document.querySelector('body')!.style.backgroundColor = '#F6F6F6'
//   }
// })
const indicator = h(LoadingOutlined, {
  style: {
    fontSize: '24px',
    marginRight: '12px',
    color: '#ffffff'
  },
  spin: true,
});
let trainState = ref(false)
let trainEnd = ref(false)
let curpreviewurl = ref('http://localhost:6008/#scalars')
const handleTrain = async () => {
  if(trainState.value == true) {
    ElMessage('上次训练还未完成，请稍后重试')
    return
  }
  curpreviewurl.value = ''
  trainState.value = true
  let res = await axios({
    method: 'post',
    url: '/update/tensorflow',
    data: {
      epochsValue: epochsValue.value,
      rateValue: rateValue.value,
      batchValue: batchValue.value,
      optimizerValue: optimizerValue.value,
    }
  });
  if(res.data.msg_code == 200) {
    setTimeout(() => {
      curpreviewurl.value = 'http://localhost:6008/#scalars'
      trainState.value = false
      trainEnd.value = true
      currentStep.value = 3
    }, 1000);
  }
}
const radioStyle = reactive({
  display: 'block',
  height: '30px',
  lineHeight: '30px',
});

let showDLgType = ref(1)
let epochsValue = ref(15)
let rateValue = ref(0.01)
let batchValue = ref(16)
let optimizerValue = ref('RMSprop')

const tableData = [
  {
    key: '1',
    ai_id: '猫狗识别_log/run1',
    ai_model: 'CNN',
    ai_rate: '0.0001',
    ai_batch: '64',
    ai_optimizer: 'Adam',
    ai_loss: '0.102432556426',
    ai_acc: '0.9531545',
    ai_time: '2022-11-02 16:00',
  },
  {
    key: '2',
    ai_id: '猫狗识别_log/run2',
    ai_model: 'MLP',
    ai_rate: '0.0001',
    ai_batch: '64',
    ai_optimizer: 'Adam',
    ai_loss: '0.102432556426',
    ai_acc: '0.9531545',
    ai_time: '2022-11-02 16:00',
  },
]
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
  font-size: 20px;
  line-height: 56px;
  color: #4844A3;
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
.font_help_title{
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  line-height: 34px;
  display: flex;
  align-items: center;
  color: #4844A3;
}
.font_tarin{
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  line-height: 24px;
  color: rgba(0, 0, 0, 0.7);
}
.font_tip_title{
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  line-height: 34px;
  color: #000000;
}
.font_help_p{
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 22px;
}
.font_menu{
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 22px;
  color: rgba(0, 0, 0, 0.6);
}
.help_cur{background-color: #ffffff;border: 1px solid #4844A3;border-radius: 4px;}
.train_btn{background-color: #4844A3; color: #ffffff}
.menu_ul li:hover{background-color:rgba(72, 68, 163, 0.1); color: #4844A3;}
</style>