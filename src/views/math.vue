<template>
  <p>Type math here:</p>
  <div :id="fieldId" style="background:#ededed;padding: 4px 6px;border: 1px solid transparent;"></div>
  <!-- <div :id="fieldId" class="border-1 border-solid"></div> -->
  <p>
    LaTeX of what you typed:
    <span id="latex"></span>
  </p>
  <div
    class="toolbar"
    :style="{top: toolbarTop,left:toolbarLeft}"
    contenteditable="false"
    v-show="showToolbar"
  >
    <div class="toolbar-arrow" :style="{left:toolArrowLeft}"></div>
    <div contenteditable="false" class="toolbar-primary" :style="{left:toolPrimaryLeft}">
      <ul>
        <li v-for="(li, index) in primaryList">
          <img :src="li.src" class="panel_box" />
        </li>
      </ul>
    </div>
    <div contenteditable="false" class="toolbar-secondary" :style="{left:toolPrimaryLeft}">
      <ul>
        <li @click="mathCommand(item.v)" v-for="(item, index) in secondaryList">{{item.k}}</li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from "vue";
let isFoucs = ref(false);
let fieldId = "field-" + new Date().getTime();
let mathField: any;
let mathFieldDom: any;
let initMathQuill = function() {
  mathFieldDom = document.getElementById(fieldId);
  let latexSpan = document.getElementById("latex");

  let MQ = window.MathQuill.getInterface(2); // for backcompat
  mathField = MQ.MathField(mathFieldDom, {
    spaceBehavesLikeTab: true,
    leftRightIntoCmdGoes: "up",
    restrictMismatchedBrackets: true,
    sumStartsWithNEquals: true,
    supSubsRequireOperand: true,
    //charsThatBreakOutOfSupSub: '+-=<>',
    autoSubscriptNumerals: true,
    autoOperatorNames: "sin COMMA",
    maxDepth: 4,
    handlers: {
      edit: function(mathField: any) {
        // var texto = mathField.text();
        latexSpan!.textContent = mathField.latex();
        //that.$emit('update:value',mathField.latex())
        console.log(mathField);
        const controller = mathField.__controller;
        isFoucs = controller.cursor;
      },
      enter: function() {
        console.log("enter");
      },
      focus: function() {
        console.log("focus");
      },
      moveOutOf: function() {
        console.log("moveOutOf");
      }
    }
  });
};
onMounted(initMathQuill);
// watch(isFoucs, (newVal: boolean, oldVal: boolean) => {
//   console.log(newVal)
// })
let toolbarTop = ref("0px");
let toolbarLeft = ref("0px");
let toolArrowLeft = ref("0px");
let toolPrimaryLeft = ref("0px");
const setBoxStyle = () => {
  toolbarTop.value =
    mathFieldDom!.offsetTop + mathFieldDom!.offsetHeight + "px";
  toolbarLeft.value = mathFieldDom!.offsetLeft + "px";
  toolArrowLeft.value = mathFieldDom!.offsetWidth / 2 + "px";
  toolPrimaryLeft.value = mathFieldDom!.offsetWidth / 2 - 45 + "px";
};

let showToolbar = ref(false);
let listenClick = () => {
  addEventListener("click", e => {
    if (mathFieldDom!.classList.value.includes("mq-focused")) {
      setBoxStyle();
      showToolbar.value = true;
    } else {
      showToolbar.value = false;
    }
  });
};
onMounted(listenClick);
const getImage = (name: string): string => {
  return new URL(`../assets/images/${name}.png`, import.meta.url).href;
};
const getSvg = (name: string): string => {
  return new URL(`../assets/icons/${name}.svg`, import.meta.url).href;
};
const primaryList = [
  { id: 1, src: getSvg("primary1") },
  { id: 2, src: getSvg("primary2") },
  { id: 3, src: getSvg("primary3") }
];
const secondaryList = [
  { k: "+", v: "\\sum", i: "" },
  { k: "-", v: "-", i: "" },
  { k: "×", v: "\\times", i: "" },
  { k: "÷", v: "\\div", i: "" },
  { k: ">", v: ">", i: "" },
  { k: "<", v: "<", i: "" },
  { k: "≥", v: "\\geq", i: "" },
  { k: "≤", v: "\\leq", i: "" }
];
interface panel {
  id: number;
  src: string;
  cmd: string;
}
const mathCommand = (cmd: string) => {
  mathField.cmd(cmd);
};
</script>
<style scoped>
.toolbar {
  position: absolute;
  bottom: auto;
  display: block;
  font-family: Symbola, "Times New Roman", serif;
}
.toolbar-arrow {
  position: absolute;
  margin-left: -10px;
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  z-index: 1;
  border-bottom: 10px solid #2a2a2a;
}
.toolbar-primary {
  background: #2a2a2a;
  position: absolute;
  top: 10px;
}
.toolbar-primary ul,
.toolbar-secondary ul {
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 3px;
}
.toolbar-primary li,
.toolbar-secondary li {
  width: 30px;
  height: 30px;
  color: white;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
}
.toolbar-primary li:hover,
.toolbar-secondary li:hover {
  background: #505050;
}
.panel_box {
  width: 20px;
  height: 20px;
  padding: 5px;
}
.toolbar-secondary {
  background: #2a2a2a;
  position: absolute;
  top: 40px;
}
/* background: #f7f7f7;
    -moz-box-shadow: inset 0 0 3px #b4b4b4;
    -webkit-box-shadow: inset 0 0 3px #b4b4b4;
    box-shadow: inset 0 0 3px #b4b4b4; */
</style>