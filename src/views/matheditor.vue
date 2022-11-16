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
            <span class="px-5 py-2 cursor-pointer" @click="showDLgType = 3;showUplaodImage=false">图片识别</span>
          </div>
          <div class="absolute right-9 cursor-pointer"><img :src="getImage('icon_setting')" /></div>
        </div>
        <div class="flex justify-center items-center" v-if="showDLgType == 3">
          <el-upload
            class="upload-demo"
            :before-upload="beforeImageUpload"
            v-if="!showUplaodImage"
          >
            <div class="bottom-font">
              <p class="py-4">上传公式图片自动识别</p>
              <img class="cursor-pointer" :src="getImage('icon_upload_img')" />
            </div>
          </el-upload>
          <div v-else>
            <p class="text-white mt-4">上传公式图片自动识别</p>
            <div class="border-dotted border-2 border-white flex items-center mt-4" style="height:144px;width:932px;background-color:#3E454A">
              <img :src="getImage('img_upload')" />
            </div>
            <div class="flex justify-center items-center flex-col relative" style="height:144px;width:932px;" v-if="!showUplaodImageF">
              <div class="dot_animation"></div>
              <div class="text-white top-24 absolute">识别中</div>
              <!-- <div style="width:20px;height:20px;border-radius:20px;background: #1ABEFF;"></div>
              <div style="width:35px;height:35px;border-radius:35px;background: #5566FF;"></div>
              <div class="text-white">识别中</div> -->
            </div>
            <div v-else>
              <div class="text-white mt-6 mb-4">根据你上传的图片转化公式</div>
              <img :src="getImage('img_upload_f')" />
            </div>
          </div>
        </div>
        <template v-else>
          <div class="flex justify-center items-center py-10" v-for="(math,mathindex) in mathList">
            <div class="mask" v-if="modelType == 'cnn' || modelType == 'mlp'"></div>
            <div class="mlp_hover" v-if="modelType == 'mlp'">
              <div class="box" style="left: 50px;">
                <div class="container">
                  <div class="list" @click="changeMlp('Relu')"><p>Relu</p><img class="help" :src="getImage('icon_help')" /></div>
                  <div class="tipbox">
                    <div class="gap" style="top:12px;left:-45px"></div>
                    <img :src="getImage('img_tipbox1')" />
                    <div class="btn"><a target="_blank" href="https://www.jiqizhixin.com/articles/2021-02-24-7">查看更多</a></div>
                  </div>
                </div>
                <div class="container">
                  <div class="list" @click="changeMlp('Sigmoid')"><p>Sigmoid</p><img class="help" :src="getImage('icon_help')" /></div>
                  <div class="tipbox">
                    <div class="gap" style="top:55px;left:-45px"></div>
                    <img :src="getImage('img_tipbox2')" />
                    <div class="btn"><a target="_blank" href="https://www.jiqizhixin.com/articles/2021-02-24-7">查看更多</a></div>
                  </div>
                </div>
                <div class="container">
                  <div class="list" @click="changeMlp('Softmax')"><p>Softmax</p><img class="help" :src="getImage('icon_help')" /></div>
                </div>
                <div class="container">
                  <div class="list" @click="changeMlp('Tanh')"><p>Tanh</p><img class="help" :src="getImage('icon_help')" /></div>
                </div>
              </div>
            </div>
            <div class="cnn_hover1" v-if="modelType == 'cnn'">
              <div class="box" style="left: 50px;">
                <div class="container">
                  <div class="list" @click="changeCnn1('Relu')"><p>Relu</p><img class="help" :src="getImage('icon_help')" /></div>
                  <div class="tipbox">
                    <div class="gap" style="top:12px;left:-45px"></div>
                    <img :src="getImage('img_tipbox1')" />
                    <div class="btn"><a target="_blank" href="https://www.jiqizhixin.com/articles/2021-02-24-7">查看更多</a></div>
                  </div>
                </div>
                <div class="container">
                  <div class="list" @click="changeCnn1('Sigmoid')"><p>Sigmoid</p><img class="help" :src="getImage('icon_help')" /></div>
                  <div class="tipbox">
                    <div class="gap" style="top:55px;left:-45px"></div>
                    <img :src="getImage('img_tipbox2')" />
                    <div class="btn"><a target="_blank" href="https://www.jiqizhixin.com/articles/2021-02-24-7">查看更多</a></div>
                  </div>
                </div>
                <div class="container">
                  <div class="list" @click="changeCnn1('Softmax')"><p>Softmax</p><img class="help" :src="getImage('icon_help')" /></div>
                </div>
                <div class="container">
                  <div class="list" @click="changeCnn1('Tanh')"><p>Tanh</p><img class="help" :src="getImage('icon_help')" /></div>
                </div>
              </div>
            </div>
            <div class="cnn_hover2" v-if="modelType == 'cnn'">
              <div class="box" style="left: 50px;">
                <div class="container">
                  <div class="list" @click="changeCnn2('Relu')"><p>Relu</p><img class="help" :src="getImage('icon_help')" /></div>
                  <div class="tipbox">
                    <div class="gap" style="top:12px;left:-45px"></div>
                    <img :src="getImage('img_tipbox1')" />
                    <div class="btn"><a target="_blank" href="https://www.jiqizhixin.com/articles/2021-02-24-7">查看更多</a></div>
                  </div>
                </div>
                <div class="container">
                  <div class="list" @click="changeCnn2('Sigmoid')"><p>Sigmoid</p><img class="help" :src="getImage('icon_help')" /></div>
                  <div class="tipbox">
                    <div class="gap" style="top:55px;left:-45px"></div>
                    <img :src="getImage('img_tipbox2')" />
                    <div class="btn"><a target="_blank" href="https://www.jiqizhixin.com/articles/2021-02-24-7">查看更多</a></div>
                  </div>
                </div>
                <div class="container">
                  <div class="list" @click="changeCnn2('Softmax')"><p>Softmax</p><img class="help" :src="getImage('icon_help')" /></div>
                </div>
                <div class="container">
                  <div class="list" @click="changeCnn2('Tanh')"><p>Tanh</p><img class="help" :src="getImage('icon_help')" /></div>
                </div>
              </div>
            </div>
            <div class="cnn_hover3" v-if="modelType == 'cnn'">
              <div class="box" style="left: 50px;">
                <div class="container">
                  <div class="list" @click="changeCnn3('Relu')"><p>Relu</p><img class="help" :src="getImage('icon_help')" /></div>
                  <div class="tipbox">
                    <div class="gap" style="top:12px;left:-45px"></div>
                    <img :src="getImage('img_tipbox1')" />
                    <div class="btn"><a target="_blank" href="https://www.jiqizhixin.com/articles/2021-02-24-7">查看更多</a></div>
                  </div>
                </div>
                <div class="container">
                  <div class="list" @click="changeCnn3('Sigmoid')"><p>Sigmoid</p><img class="help" :src="getImage('icon_help')" /></div>
                  <div class="tipbox">
                    <div class="gap" style="top:55px;left:-45px"></div>
                    <img :src="getImage('img_tipbox2')" />
                    <div class="btn"><a target="_blank" href="https://www.jiqizhixin.com/articles/2021-02-24-7">查看更多</a></div>
                  </div>
                </div>
                <div class="container">
                  <div class="list" @click="changeCnn3('Softmax')"><p>Softmax</p><img class="help" :src="getImage('icon_help')" /></div>
                </div>
                <div class="container">
                  <div class="list" @click="changeCnn3('Tanh')"><p>Tanh</p><img class="help" :src="getImage('icon_help')" /></div>
                </div>
              </div>
            </div>
            <div class="editor-box">
              <div class="editor-module flex items-center relative">
                <div class="module-title">Module</div>
                <div class="module-input">
                  <mathInput :defaulevalue="math.moduleVal1"></mathInput>(
                  <mathInput :defaulevalue="math.moduleVal2"></mathInput>;
                  <mathInput :defaulevalue="math.moduleVal3"></mathInput>)
                </div>
                <div class="plus" expanded="false">
                  <img class="plus-img" :src="getImage('icon_plus')" />
                  <div class="plus-tip state-font absolute p-2 rounded" style="background: #1F2C34;bottom: 32px;left: -102px;" @mouseenter="handlePlusArea($event,'enter')" @mouseleave="handlePlusArea($event,'leave')">
                    <div class="flex items-center w-56 h-12 rounded cursor-pointer hover:bg-statehover" @click="handlePlus(1,-1,mathindex)">
                      <p class="ml-3 mr-2">Statement</p>
                      <img class="mr-14" :src="getImage('icon_tip')" />
                      <img :src="getImage('icon_state_1')" />
                    </div>
                    <div class="flex items-center w-56 h-12 rounded cursor-pointer hover:bg-statehover" @click="handlePlus(2,-1,mathindex)">
                      <p class="ml-3 mr-2">Recursive Array</p>
                      <img class="mr-4" :src="getImage('icon_tip')" />
                      <img :src="getImage('icon_state_2')" />
                    </div>
                  </div>
                </div>
              </div>
              <div v-for="(state, index) in math.statementList" :key="state.id">
                <div class="editor-statement" v-if="state.type == 1">
                  <div class="statement-input">
                    <div class="deletetip absolute top-6 -left-3">
                      <img class="absolute max-w-none -left-8 -top-11 z-10" :src="getImage('icon_delete_tip')" />
                      <img class="max-w-none cursor-pointer" @click="handleDeleteArrow(mathindex,index)" :src="getImage('icon_delete_row')" />
                    </div>
                    <mathInput :defaulevalue="state.value1"></mathInput>
                    <img class="w-8 mx-2 inline-block" :src="getImage('statement-arrow')" />
                    <mathInput :defaulevalue="state.value2"></mathInput>
                  </div>
                  <div class="plus relative" expanded="false">
                    <img class="plus-img" :src="getImage('icon_plus')" />
                    <div class="plus-tip state-font absolute p-2 rounded" style="background: #1F2C34;bottom: 32px;left: -102px;" @mouseenter="handlePlusArea($event,'enter')" @mouseleave="handlePlusArea($event,'leave')">
                      <div class="flex items-center w-56 h-12 rounded cursor-pointer hover:bg-statehover" @click="handlePlus(1,index,mathindex)">
                        <p class="ml-3 mr-2">Statement</p>
                        <img class="mr-14" :src="getImage('icon_tip')" />
                        <img :src="getImage('icon_state_1')" />
                      </div>
                      <div class="flex items-center w-56 h-12 rounded cursor-pointer hover:bg-statehover" @click="handlePlus(2,index,mathindex)">
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
                      <img class="max-w-none cursor-pointer" @click="handleDeleteArrow(mathindex, index)" :src="getImage('icon_delete_row')" />
                    </div>
                    <div class="array-left">
                      <mathInput :defaulevalue="state.leftValue"></mathInput>
                    </div>
                    <div class="array-mid">
                      <img :src="getImage('statement-arrow')" />
                    </div>
                    <div class="array-right">
                      <div class="inline-block">
                        <div class="table">
                            <div class="row" v-for="(arr, arrindex) in state.array" :key="arr.id">
                                <div class="cell relative">
                                  <mathInput :defaulevalue="arr.value1"></mathInput>
                                  <div class="array-plus cursor-pointer" @click="handleArrayPlus(state, arrindex)">
                                    <img :src="getImage('icon_plus')" />
                                  </div>
                                  <div class="array-delete cursor-pointer" @click="handleArraydelete(state, arrindex)">
                                    <img :src="getImage('icon_delete_row')" />
                                  </div>
                                </div>
                                <div class="cell">
                                  <mathInput :defaulevalue="arr.value2"></mathInput>
                                </div>
                            </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="plus relative" expanded="false">
                    <img class="plus-img" :src="getImage('icon_plus')" />
                    <div class="plus-tip state-font absolute p-2 rounded" style="background: #1F2C34;bottom: 32px;left: -102px;" @mouseenter="handlePlusArea($event,'enter')" @mouseleave="handlePlusArea($event,'leave')">
                      <div class="flex items-center w-56 h-12 rounded cursor-pointer hover:bg-statehover" @click="handlePlus(1,index,mathindex)">
                        <p class="ml-3 mr-2">Statement</p>
                        <img class="mr-14" :src="getImage('icon_tip')" />
                        <img :src="getImage('icon_state_1')" />
                      </div>
                      <div class="flex items-center w-56 h-12 rounded cursor-pointer hover:bg-statehover" @click="handlePlus(2,index,mathindex)">
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
                  <mathInput :defaulevalue="math.returnVal"></mathInput>
                </div>
              </div>
            </div>
          </div>
        </template>
        
        <div class="rounded w-full mt-10" style="background: #1C2C35;height: 97px;" v-show="isShowFoot">
          <div class="bottom-font absolute right-0 flex items-center mx-4" style="height: 97px;">
            <div class="bg-black flex justify-center items-center h-16 w-40 rounded mx-4 cursor-pointer"><img :src="getImage('icon_code')" /><p class="ml-2 my-0">生成代码</p></div>
            <div class="bg-black flex justify-center items-center h-16 w-40 rounded mx-4 cursor-pointer" @click="changeCurrentStep(2)"><img :src="getImage('icon_code')" /><p class="ml-2 my-0">立即使用</p></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { ref, defineProps, onMounted, defineEmits } from "vue";
import mathInput from "./mathinput.vue";
import { useRouter } from "vue-router";
const router = useRouter()
const props = defineProps({
  isShowTitle: {
    type: Boolean,
    default: true
  },
  isShowFoot: {
    type: Boolean,
    default: true
  },
  modelType: {
    type: String,
    default: ""
  },
})
const emits = defineEmits(['changeActivation','changeCurrentStep'])
const getImage = (name: string): string => {
  return new URL(`../assets/images/home/${name}.png`, import.meta.url).href;
};
let mathList = ref([
  {  
    moduleVal1: '',
    moduleVal2: '',
    moduleVal3: '',
    returnVal: '',
    statementList: [
      { type: 1, id:1, value1:"", value2:""},
      { type: 2, id:2, array: [{id:1,value1:"",value2:""},{id:2,value1:"",value2:""}], leftValue: "" }
    ]
  }
])
let arrayid = 10
let stateid = 10
const handleArrayPlus = (state:any, arrindex:number) => {
  state.array.splice(arrindex+1,0,{id:arrayid++})
}
const handleArraydelete = (state:any, arrindex:number) => {
  if(state.array.length > 1)
  state.array.splice(arrindex,1)
}
const handlePlus = (type:number,index:number,mathindex:number) => {
  if(type == 1){
    mathList.value[mathindex].statementList.splice(index+1,0,{ type: 1, id:stateid++, value1:"", value2:"" })
  }else{
    mathList.value[mathindex].statementList.splice(index+1,0,{ type: 2, id:stateid++, array: [{id:1,value1:"",value2:""},{id:2,value1:"",value2:""}], leftValue: "" })
  }
}
const handlePlusArea = (e:any, type:string) => {
  if(type == 'enter'){
    e.currentTarget.parentElement.setAttribute('expanded',true)
  }else{
    e.currentTarget.parentElement.setAttribute('expanded',false)
  }
}
const handleDeleteArrow = (mathindex:number,index:number) => {
  mathList.value[mathindex].statementList.splice(index,1)
}
const jumpTo = (route:string,type:number) => {
  router.push({name: route,params:{currentStep:type}})
}
let showUplaodImage = ref(false)
let showUplaodImageF = ref(false)
const beforeImageUpload = () => {
  showUplaodImageF.value = false
  showUplaodImage.value = true
  setTimeout(() => {
    showUplaodImageF.value = true
  }, 2000);
}
let showDLgType = ref(1)
if(props.modelType == "mlp"){
  mathList.value = [{
    moduleVal1: "MLP",
    moduleVal2: "x",
    moduleVal3: "W,b",
    returnVal: "h_{\\left[L\\right]}",
    statementList: [
      { type: 1, id:stateid++,value1:"L",value2:"\\left|W\\right|" },
      { type: 2, id:stateid++, array: [{id:1,value1:"x",value2:"i=0"},{id:2,value1:"\\text{Relu}\\left(W_{\\left[i-1\\right]}\\cdot h_{\\left[i-1\\right]}+b_{\\left[i-1\\right]}\\right)",value2:"i<L"}, {id:3,value1:"W_{\\left[i-1\\right]}\\cdot h_{\\left[i-1\\right]}+b_{\\left[i-1\\right]}",value2:"otherwise"}],leftValue: "h_\\left[0\\le i\\le L\\right]" }
    ]
  }]
}else if(props.modelType == "cnn") {
  mathList.value = [
    {
      moduleVal1: "ConBlock",
      moduleVal2: "x",
      moduleVal3: "Conv2d_0,Conv2d_1",
      returnVal: "\\text{Relu}(Conv2d_0,(\\text{Relu}(Conv2d_0(x))))",
      statementList: []
    },
    {
      moduleVal1: "CNN",
      moduleVal2: "x",
      moduleVal3: "ConvBlock,MaxPoll_2d,MLP",
      returnVal: "y",
      statementList: [
        { type: 1, id:stateid++, value1:"h_c", value2:"MaxPool_{2d}(ConvBlock(x))"},
        { type: 1, id:stateid++, value1:"h", value2:"\\text{Flatten}(h_c)"},
        { type: 1, id:stateid++, value1:"y", value2:"MLP(h)"},
      ]
    }
  ]
}
const changeCurrentStep = (value:number) => {
  emits('changeCurrentStep',value)
}
const changeMlp = (value:string) => {
  emits("changeActivation",value)
  let str = `\\text{${value}}\\left(W_{\\left[i-1\\right]}\\cdot h_{\\left[i-1\\right]}+b_{\\left[i-1\\right]}\\right)`
  mathList.value[0].statementList[1].array![1].value1 = str
}
let cnnvalue1 = 'Relu'
let cnnvalue2 = 'Relu'
const changeCnn1 = (value:string) => {
  emits("changeActivation",value)
  cnnvalue1 = value
  let str = `\\text{${value}}(Conv2d_0,(\\text{${cnnvalue2}}(Conv2d_0(x))))`
  mathList.value[0].returnVal = str
}
const changeCnn2 = (value:string) => {
  emits("changeActivation",value)
  cnnvalue2 = value
  let str = `\\text{${cnnvalue1}}(Conv2d_0,(\\text{${value}}(Conv2d_0(x))))`
  mathList.value[0].returnVal = str
}
const changeCnn3 = (value:string) => {
  let str = `\\text{${value}}(h_c)`
  mathList.value[1].statementList[1].value2 = str
}
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
  margin: 0 0 0 20px;
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
.table {
    display: table;
}
.row {
    display: table-row;
}
.cell {
    display: table-cell;
}
.dot_animation{
  position: absolute;
  animation: dot 1s infinite linear;
}
@keyframes dot
{
    /* 0%   {top:0px;width:0px;height:0px;border-radius: 0px;background: #1ABEFF;} */
    35%  {top:30px;width:20px;height:20px;border-radius: 20px;background: #1ABEFF;}
    /* 50%  {top:40px;width:20px;height:20px;border-radius: 20px;background: #5566FF;} */
    100% {top:60px;width:30px;height:30px;border-radius: 30px;background: #5566FF;}
}
.mask{width: 100%;position: absolute;z-index: 10;top: 15%;height: 70%;}
.box {
  z-index: 20;
  top:0px;
  left: 0px;
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 22px;
  z-index:1000;
  justify-content: center;
  align-items: center;
  display: none;
  flex-direction: column;
  position:absolute;
  color:black;
  width:127px;
  height:188px;
  background-color:white;
  border: 0.5px solid #DCDCDC;
  box-shadow: 0px 3px 14px 2px rgba(0, 0, 0, 0.05), 0px 8px 10px 1px rgba(0, 0, 0, 0.06), 0px 5px 5px -3px rgba(0, 0, 0, 0.1);
  border-radius: 3px;
}
.box .container {
  width:112px;
  height:40px;
  padding:12px;
  border-radius: 3px;
  cursor: pointer;
}
.box .container .gap {
  position: absolute;
  width:112px;
  height:40px;
}
.box .container .list{
  justify-content: left;
  align-items: center;
  display: flex;
}
.box .container:hover{
  color: #4844A3;
  background: #ECF2FE;
}
.box .container:hover .tipbox{
  display: block;
}
.box .container .list .help{
  position: absolute;
  right: 12px;
}
.box .container .tipbox{
  display: none;
  top: 0px;
  left: 136px;
  position: absolute;
  width: 600px;
  padding: 32px;
  background-color: white;
  border-radius: 3px;
}
.box .container .tipbox .btn{
  margin-top: 16px;
  width: 530px;
  height: 32px;
  border: 1px solid #DCDCDC;
  border-radius: 3px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.cnn_hover1{height: 25px;width: 60px;position: absolute;top: 232px;left: 427px;z-index: 20;}
.cnn_hover1:hover .box {display: flex;}
.cnn_hover2{height: 25px;width: 60px;position: absolute;top: 232px;left: 617px;z-index: 20;}
.cnn_hover2:hover .box {display: flex;}
.cnn_hover3{height: 25px;width: 60px;position: absolute;top: 558px;left: 383px;z-index: 20;}
.cnn_hover3:hover .box {display: flex;}
.mlp_hover{height: 25px;width: 60px;position: absolute;top: 367px;left: 484px;z-index: 20;}
.mlp_hover:hover .box {display: flex;}
</style>