<template>
  <div class="h-24 flex items-center" style="background: rgba(72, 68, 163, 0.1);" v-show="isShowTitle">
    <img class="ml-8 cursor-pointer" @click="jumpTo('homepage',1)" :src="getImage('icon_back')" />
  </div>
  <div class="flex justify-center items-center my-4">
    <div class="rounded" style="background:#000;width:1360px;min-height:840px">
      <div class="w-full h-9 rounded" style="background:rgba(255, 255, 255, 0.19);"></div>
      <div class="editor-font ml-7 my-5">模型编辑器</div>
      <div class="rounded relative ml-7 mb-5" style="background:rgba(17, 26, 32, 1);width:1310px;">
        <div class="relative w-full flex items-center rounded" style="background: #1C2C35;height: 97px;">
          <div class="title-font flex items-center rounded left-16 absolute" style="background: rgba(242, 242, 242, 0.1);">
            <span class="px-5 py-2 cursor-pointer" @click="showDLgType = 1">快捷工具</span>
            <span class="px-5 py-2 cursor-pointer" @click="showDLgType = 2">模型库</span>
            <span class="px-5 py-2 cursor-pointer" @click="showDLgType = 3">图片识别</span>
          </div>
          <div class="absolute right-9 cursor-pointer"><img :src="getImage('icon_setting')" /></div>
        </div>
        <div class="flex justify-center items-center" v-if="showDLgType == 3">
          <div class="bottom-font">
            <p class="py-4">上传公式图片自动识别</p>
            <img class="cursor-pointer" :src="getImage('icon_upload_img')" />
          </div>
        </div>
        <div v-else class="flex justify-center items-center py-10">
          <div class="editor-box">
            <div class="editor-module flex items-center relative">
              <div class="module-title">Module</div>
              <div class="module-input">
                <mathInput></mathInput>(
                <mathInput></mathInput>;
                <mathInput></mathInput>)
              </div>
              <div class="plus" expanded="false">
                <img class="plus-img" :src="getImage('icon_plus')" />
                <div class="plus-tip state-font absolute p-2 rounded" style="background: #1F2C34;bottom: 32px;left: -102px;" @mouseenter="handlePlusArea($event,'enter')" @mouseleave="handlePlusArea($event,'leave')">
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
                  <div class="deletetip absolute top-6 -left-3">
                    <img class="absolute max-w-none -left-8 -top-11 z-10" :src="getImage('icon_delete_tip')" />
                    <img class="max-w-none cursor-pointer" @click="handleDeleteArrow(index)" :src="getImage('icon_delete_row')" />
                  </div>
                  <mathInput></mathInput>
                  <img class="w-8 mx-2 inline-block" :src="getImage('statement-arrow')" />
                  <mathInput></mathInput>
                </div>
                <div class="plus relative" expanded="false">
                  <img class="plus-img" :src="getImage('icon_plus')" />
                  <div class="plus-tip state-font absolute p-2 rounded" style="background: #1F2C34;bottom: 32px;left: -102px;" @mouseenter="handlePlusArea($event,'enter')" @mouseleave="handlePlusArea($event,'leave')">
                    <div class="flex items-center w-56 h-12 rounded cursor-pointer hover:bg-statehover" @click="handlePlus(1,index+1)">
                      <p class="ml-3 mr-2">Statement</p>
                      <img class="mr-14" :src="getImage('icon_tip')" />
                      <img :src="getImage('icon_state_1')" />
                    </div>
                    <div class="flex items-center w-56 h-12 rounded cursor-pointer hover:bg-statehover" @click="handlePlus(2,index+1)">
                      <p class="ml-3 mr-2">Recursive Array</p>
                      <img class="mr-4" :src="getImage('icon_tip')" />
                      <img :src="getImage('icon_state_2')" />
                    </div>
                  </div>
                </div>
              </div>
              <div class="editor-array-statement" v-if="state.type == 2">
                <div class="array-input flex items-center">
                  <div class="deletetip absolute top-1/2 -left-3">
                    <img class="absolute max-w-none -left-8 -top-11 z-10" :src="getImage('icon_delete_tip')" />
                    <img class="max-w-none cursor-pointer" @click="handleDeleteArrow(index)" :src="getImage('icon_delete_row')" />
                  </div>
                  <div class="array-left">
                    <mathInput></mathInput>
                  </div>
                  <div class="array-mid">
                    <img :src="getImage('statement-arrow')" />
                  </div>
                  <div class="array-right">
                    <div class="inline-block">
                      <li v-for="(arr, arrindex) in state.array" :key="arr.id">
                        <mathInput></mathInput>
                        <div class="array-plus cursor-pointer" @click="handleArrayPlus(state, arrindex)">
                          <img :src="getImage('icon_plus')" />
                        </div>
                        <div class="array-delete cursor-pointer" @click="handleArraydelete(state, arrindex)">
                          <img :src="getImage('icon_delete_row')" />
                        </div>
                      </li>
                    </div>
                    <div class="inline-block">
                      <li v-for="(arr, arrindex) in state.array" :key="arr.id">
                        <mathInput></mathInput>
                      </li>
                    </div>
                  </div>
                </div>
                <div class="plus relative" expanded="false">
                  <img class="plus-img" :src="getImage('icon_plus')" />
                  <div class="plus-tip state-font absolute p-2 rounded" style="background: #1F2C34;bottom: 32px;left: -102px;" @mouseenter="handlePlusArea($event,'enter')" @mouseleave="handlePlusArea($event,'leave')">
                    <div class="flex items-center w-56 h-12 rounded cursor-pointer hover:bg-statehover" @click="handlePlus(1,index+1)">
                      <p class="ml-3 mr-2">Statement</p>
                      <img class="mr-14" :src="getImage('icon_tip')" />
                      <img :src="getImage('icon_state_1')" />
                    </div>
                    <div class="flex items-center w-56 h-12 rounded cursor-pointer hover:bg-statehover" @click="handlePlus(2,index+1)">
                      <p class="ml-3 mr-2">Recursive Array</p>
                      <img class="mr-4" :src="getImage('icon_tip')" />
                      <img :src="getImage('icon_state_2')" />
                    </div>
                  </div>
                </div>
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
        <div class="rounded w-full mt-10" style="background: #1C2C35;height: 97px;" v-show="isShowFoot">
          <div class="bottom-font absolute right-0 flex items-center mx-4" style="height: 97px;">
            <div class="bg-black flex justify-center items-center h-16 w-40 rounded mx-4 cursor-pointer"><img :src="getImage('icon_code')" /><p class="ml-2 my-0">生成代码</p></div>
            <div class="bg-black flex justify-center items-center h-16 w-40 rounded mx-4 cursor-pointer" @click="jumpTo('homepage',2)"><img :src="getImage('icon_code')" /><p class="ml-2 my-0">立即使用</p></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { ref, defineProps } from "vue";
import mathInput from "./mathinput.vue";
import { useRouter } from "vue-router";
const router = useRouter()
defineProps({
  isShowTitle: {
    type: Boolean,
    default: true
  },
  isShowFoot: {
    type: Boolean,
    default: true
  },
})
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
const handleArraydelete = (state:any, arrindex:number) => {
  if(state.array.length > 1)
  state.array.splice(arrindex,1)
}
const handlePlus = (type:number,index:number) => {
  if(type == 1){
    statementList.value.splice(index,0,{ type: 1, array: [{id:1}] })
  }else{
    statementList.value.splice(index,0,{ type: 2, array: [{id:1},{id:2}] })
  }
}
const handlePlusArea = (e:any, type:string) => {
  if(type == 'enter'){
    e.currentTarget.parentElement.setAttribute('expanded',true)
  }else{
    e.currentTarget.parentElement.setAttribute('expanded',false)
  }
}
const handleDeleteArrow = (index:number) => {
  statementList.value.splice(index,1)
}
const jumpTo = (route:string,type:number) => {
  router.push({name: route,params:{currentStep:type}})
}
let showDLgType = ref(1)
</script>
<style scoped>
p {
  margin-bottom: 0;
}
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
  /* width: 600px; */
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
  display: none;
}
.plus .plus-tip {
  display: none;
}
.plus:hover .plus-img, .plus[expanded=true] .plus-img {
  display: block;
}
.plus:hover .plus-tip{
  display: block;
}
.array-plus {
  width: 20px;
  height: 20px;
  position: absolute;
  bottom: -13px;
  left: -7px;
  z-index: 2;
}
.array-plus img {
  width: 20px;
  height: 20px;
  display: none;
}
.array-plus:hover img{
  display: block;
}
.array-delete {
  width: 20px;
  height: 20px;
  position: absolute;
  bottom: 9px;
  left: -7px;
  z-index: 2;
}
.array-delete img {
  width: 20px;
  height: 20px;
  display: none;
}
.array-delete:hover img{
  display: block;
}
.deletetip{height: 24px;width: 24px;}
.deletetip img{display: none;}
.deletetip:hover img{display: block;}
.title-font span:hover{color: #19BEFF;border: 2px solid #19BEFF;border-radius: 4px;}
</style>