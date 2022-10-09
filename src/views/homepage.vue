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
        <div class="model-list">
          <div class="model-img"><img /></div>
          <div class="model-title"><span>多层感知器</span><span>Multi-Layer Perception (MLP)</span></div>
          <div class="model-btn">使用</div>
          <div class="model-arrow"></div>
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
.ai-header {
  height: 120px;
  width: 100%;
  box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
}
.type-box {
  width: 496px;
  height: 626px;
  display: inline-block;
  border: 1px solid #000000;
  border-radius: 20px;
  margin: 23px;
  position: relative;
}
.type-image {
  border-radius: 20px;
}
.type-title {
  position: absolute;
  width: 184px;
  height: 46px;
  left: 31px;
  top: 313px;
  font-family: "PingFang SC";
  font-style: normal;
  font-weight: 400;
  font-size: 40px;
  line-height: 56px;
}
.type-p {
  position: absolute;
  width: 434px;
  height: 50px;
  left: 31px;
  top: 391px;
  font-family: "PingFang SC";
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  line-height: 34px;
}
.type-btn {
  position: absolute;
  width: 432px;
  height: 66.55px;
  left: 31px;
  top: 524px;
  background: #4844a3;
  border-radius: 10px;
}
.type-btn span {
  position: absolute;
  width: 145px;
  height: 35px;
  left: 145px;
  top: 10px;
  font-family: "PingFang SC";
  font-style: normal;
  font-weight: 400;
  font-size: 32px;
  line-height: 45px;
  color: #ffffff;
}
.data-box {
  width: 401px;
  height: 423px;
  display: inline-block;
  border: 1px solid #000000;
  border-radius: 10px;
  margin: 23px;
  position: relative;
}
.data-image {
  border-radius: 10px;
}
.data-title {
  position: absolute;
  width: 103px;
  height: 34px;
  left: 53px;
  top: 249px;
  font-family: "PingFang SC";
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  line-height: 34px;
}
.data-p {
  position: absolute;
  width: 434px;
  height: 50px;
  left: 53px;
  top: 291px;
  font-family: "PingFang SC";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 28px;
}
.data-btn {
  position: absolute;
  width: 293px;
  height: 54px;
  left: 53px;
  top: 335px;
  background: #4844a3;
  border-radius: 10px;
}
.data-btn span {
  position: absolute;
  width: 145px;
  height: 35px;
  left: 80px;
  top: 5px;
  font-family: "PingFang SC";
  font-style: normal;
  font-weight: 400;
  font-size: 32px;
  line-height: 45px;
  color: #ffffff;
}
.blue-btn{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 148px;
  height: 67px;
  background: #4844A3;
  border-radius: 10px;
  margin: 13px;
}
.blue-btn span{
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 32px;
  line-height: 45px;
  color: #ffffff;
}
.gray-btn{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 148px;
  height: 67px;
  background: #DEDCFC;
  border-radius: 10px;
  margin: 13px;
}
.gray-btn span{
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 32px;
  line-height: 45px;
  color: #4844A3;
}
</style>