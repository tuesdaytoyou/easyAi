<template>
  <div class="p-52" style="background:#111A20">
    <div class="flex justify-center items-center">
      <div class="editor-box">
        <div class="editor-module flex items-center">
          <div class="module-title">Module</div>
          <div class="module-input">
            <mathInput></mathInput>(
            <mathInput></mathInput>;
            <mathInput></mathInput>)
          </div>
        </div>
        <div v-for="(state, index) in statementList">
          <div class="editor-statement" v-if="state.type == 1">
            <div class="statement-input">
              <mathInput></mathInput>
              <img :src="getImage('statement-arrow')" />
              <mathInput></mathInput>
            </div>
            <div class="plus" v-if="index != statementList.length-1">
              <img :src="getImage('plus')" />
            </div>
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
            <div class="plus" v-if="index != statementList.length-1">
              <img :src="getImage('plus')" />
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
  { type: 1, array: [{id:1}] },
  { type: 2, array: [{id:1},{id:2}] }
]);
let arrayid = 2
const handleArrayPlus = (state:any, arrindex:number) => {
  state.array.splice(arrindex+1,0,{id:arrayid++})
}
</script>
<style scoped>
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
.plus img {
  width: 32px;
  height: 32px;
  display: none;
}
.plus:hover img{
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
.array-plus:hover img{
  display: block;
}
</style>