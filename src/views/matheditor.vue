<template>
  <div class="h-24 flex items-center" style="background: rgba(72, 68, 163, 0.1);">
    <img class="ml-8 cursor-pointer" :src="getImage('icon_back')" />
  </div>
  <div class="flex justify-center items-center my-4">
    <div class="rounded" style="background:#000;width:1360px;min-height:840px">
      <div class="w-full h-9 rounded" style="background:rgba(255, 255, 255, 0.19);"></div>
      <div class="editor-font ml-7 my-5">模型编辑器</div>
      <div class="rounded relative ml-7 mb-5" style="background:rgba(17, 26, 32, 1);width:1310px;min-height: 693px;">
        <div class="relative w-full flex items-center rounded" style="background: #1C2C35;height: 97px;">
          <div class="title-font py-2 flex items-center rounded left-16 absolute" style="background: rgba(242, 242, 242, 0.1);width: 400px;">
            <span class="px-5 cursor-pointer">快捷工具</span>
            <span class="px-5 cursor-pointer">模型库</span>
            <span class="px-5 cursor-pointer">图片识别</span>
          </div>
          <div class="absolute right-9 cursor-pointer"><img :src="getImage('icon_setting')" /></div>
        </div>
        <div class="flex justify-center items-center mt-10">
          <div class="editor-box">
            <div class="editor-module flex items-center relative">
              <div class="module-title">Module</div>
              <div class="module-input">
                <mathInput></mathInput>(
                <mathInput></mathInput>;
                <mathInput></mathInput>)
              </div>
              <div class="plus relative">
                <img class="plus-img" :src="getImage('plus')" />
                <div class="plus-tip state-font absolute p-2 rounded" style="background: #1F2C34;bottom: 32px;left: -102px;">
                  <div class="flex items-center w-56 h-12 rounded cursor-pointer hover:bg-statehover" @click="handlePlus(1,0)">
                    <p class="ml-3 mr-2">Statement</p>
                    <img class="mr-14" :src="getImage('icon_tip')" />
                    <img :src="getImage('icon_state_1')" />
                  </div>
                  <div class="flex items-center w-56 h-12 rounded cursor-pointer hover:bg-statehover" @click="handlePlus(2,0)">
                    <p class="ml-3 mr-2">Recursive Array</p>
                    <img class="mr-4" :src="getImage('icon_tip')" />
                    <img :src="getImage('icon_state_2')" />
                  </div>
                </div>
              </div>
            </div>
            <div v-for="(state, index) in statementList">
              <div class="editor-statement" v-if="state.type == 1">
                <div class="statement-input">
                  <mathInput></mathInput>
                  <img :src="getImage('statement-arrow')" />
                  <mathInput></mathInput>
                </div>
                <!-- <div class="plus">
                  <img :src="getImage('plus')" />
                </div> -->
              </div>
              <div class="editor-array-statement" v-if="state.type == 2">
                <div class="array-input flex items-center">
                  <div class="array-left">
                    <mathInput></mathInput>
                  </div>
                  <div class="array-mid">
                    <img :src="getImage('statement-arrow')" />
                  </div>
                  <div class="array-right">
                    <li v-for="(arr, arrindex) in state.array" :key="arr.id">
                      <mathInput></mathInput>
                      <mathInput></mathInput>
                      <div class="array-plus" v-if="arrindex != state.array.length-1" @click="handleArrayPlus(state, arrindex)">
                        <img :src="getImage('plus')" />
                      </div>
                    </li>
                  </div>
                </div>
                <!-- <div class="plus">
                  <img :src="getImage('plus')" />
                </div> -->
              </div>
            </div>
            <div class="editor-return flex items-center">
              <div class="return-title">Return</div>
              <div class="return-input">
                <mathInput></mathInput>
              </div>
            </div>
          </div>
        </div>
        <div class="rounded w-full mt-10 absolute bottom-0" style="background: #1C2C35;height: 97px;">
          <div class="bottom-font absolute right-0 flex items-center mx-4" style="height: 97px;">
            <div class="bg-black flex justify-center items-center h-16 w-40 rounded mx-4 cursor-pointer"><img :src="getImage('icon_code')" /><p class="ml-2">生成代码</p></div>
            <div class="bg-black flex justify-center items-center h-16 w-40 rounded mx-4 cursor-pointer"><img :src="getImage('icon_code')" /><p class="ml-2">立即使用</p></div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>
<script setup lang="ts">
import { ref } from "vue";
import mathInput from "./mathinput.vue";
const getImage = (name: string): string => {
  return new URL(`../assets/images/home/${name}.png`, import.meta.url).href;
};
let statementList = ref([
  { type: 1, array: [{id:1}] },
  { type: 2, array: [{id:1},{id:2}] }
]);
let arrayid = 2
const handleArrayPlus = (state:any, arrindex:number) => {
  state.array.splice(arrindex+1,0,{id:arrayid++})
}
const handlePlus = (type:number,index:number) => {
  if(type == 1){
    statementList.value.splice(index,0,{ type: 1, array: [{id:1}] })
  }else{
    statementList.value.splice(index,0,{ type: 2, array: [{id:1},{id:2}] })
  }
}
</script>
<style scoped>
.editor-font{
  font-family: 'Roboto Mono';
  font-style: normal;
  font-weight: 400;
  font-size: 32px;
  line-height: 42px;
  color: #FFFFFF;
}
.title-font{
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 23.9988px;
  line-height: 38px;
  text-align: center;
  color: #FFFFFF;
}
.state-font{
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 22px;
  color: #FFFFFF;
}
.bottom-font{
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 500;
  font-size: 18.1616px;
  line-height: 25px;
  color: #FFFFFF;
}
.editor-box {
  width: 780px;
  font-family: "Microsoft YaHei";
  font-style: normal;
  font-weight: 700;
  font-size: 25.0059px;
  line-height: 33px;
  color: #ffffff;
}
.editor-module {
  line-height: 62px;
  border-top: 4px solid #1abeff;
  border-bottom: 4px solid #1abeff;
}
.editor-statement,
.editor-array-statement {
  border-bottom: 1px solid #1abeff;
  position: relative;
}

.editor-return {
  line-height: 62px;
  border-bottom: 4px solid #1abeff;
}
.module-title {
  display: inline-block;
  margin: 0 50px 0 20px;
}
.module-input {
  display: inline-block;
}
.statement-input {
  padding: 16px 0;
  margin: 0 50px 0 20px;
}
.statement-input img {
  display: inline-block;
  margin: 0 10px;
  width: 32px;
}
.return-title {
  display: inline-block;
  margin: 0 50px 0 20px;
}
.return-input {
  display: inline-block;
}
.array-left {
  display: inline-block;
}
.array-input {
  padding: 16px 0;
  margin: 0 50px 0 20px;
}
.array-mid {
  display: inline-block;
}
.array-right {
  display: inline-block;
}
.array-right li {
  position: relative;
  width: 600px;
}
.array-mid img {
  display: inline-block;
  margin: 0 10px;
  width: 32px;
}
.plus {
  width: 32px;
  height: 32px;
  position: absolute;
  bottom: -17px;
  left: -15px;
  z-index: 2;
}
.plus .plus-img {
  width: 32px;
  height: 32px;
  /* display: none; */
}
.plus .plus-tip {
  /* display: none; */
}
.plus:hover .plus-img{
  display: block;
}
.plus:hover .plus-tip{
  display: block;
}
.array-plus {
  width: 32px;
  height: 32px;
  position: absolute;
  bottom: -15px;
  left: 63px;
  z-index: 2;
}
.array-plus img {
  width: 32px;
  height: 32px;
  display: none;
}
.array-plus:hover .plus-img{
  display: block;
}
.array-plus:hover .plus-tip{
  display: block;
}
</style>