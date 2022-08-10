<template>
  <div style="">
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
      <div contenteditable="false" class="toolbar-secondary" style="left:-150px;">
        <ul v-for="secondary in secondaryList">
          <li @click="mathCommand(item.v,item.i)" v-for="(item, index) in secondary">
            <img :src="item.k" class="panel_box" />
          </li>
        </ul>
      </div>
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
    // spaceBehavesLikeTab: true,
    // leftRightIntoCmdGoes: "up",
    // restrictMismatchedBrackets: true,
    // sumStartsWithNEquals: true,
    // supSubsRequireOperand: true,
    // //charsThatBreakOutOfSupSub: '+-=<>',
    // autoSubscriptNumerals: true,
    // autoOperatorNames: "sin COMMA",
    // maxDepth: 4,
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
  return new URL(`../assets/images/math/${name}.png`, import.meta.url).href;
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
  [
    { k: getImage('1-1'), v: "+", i: "" },
    { k: getImage('1-2'), v: "-", i: "" },
    { k: getImage('1-3'), v: "\\times", i: "" },
    { k: getImage('1-4'), v: "\\div", i: "" },
    { k: getImage('1-5'), v: "\\times", i: "" },
    { k: getImage('1-6'), v: "\\cdot", i: "" },
    { k: getImage('1-7'), v: "<", i: "" },
    { k: getImage('1-8'), v: ">", i: "" },
    { k: getImage('1-9'), v: "\\leq", i: "" },
    { k: getImage('1-10'), v: "=", i: "" },
  ],
  [
    { k: getImage('2-1'), v: "\\neq", i: "" },
    { k: getImage('2-2'), v: "\\geq", i: "" },
    { k: getImage('2-3'), v: "\\wedge", i: "" },
    { k: getImage('2-4'), v: "\\vee", i: "" },
    { k: getImage('2-5'), v: "\\neg", i: "" },
    { k: getImage('2-6'), v: "\\in", i: "" },
    { k: getImage('2-7'), v: "\\sum", i: "" },
    { k: getImage('2-8'), v: "\\left\\{\\right\\}", i: "" },
    { k: getImage('2-9'), v: "\\pi", i: "" },
    { k: getImage('2-10'), v: "\\triangleright", i: "" },
  ],
  [
    { k: getImage('3-1'), v: "^", i: "" },
    { k: getImage('3-2'), v: "_", i: "" },
    { k: getImage('3-3'), v: "", i: "" },
    { k: getImage('3-4'), v: "\\sqrt", i: "" },
    { k: getImage('3-5'), v: "\\frac", i: "" },
    { k: getImage('3-6'), v: "<", i: "" },
    { k: getImage('3-7'), v: "|", i: "" },
    { k: getImage('3-8'), v: "\\lfloor\\left\\{\\right\\}\\rfloor", i: "write" },
    { k: getImage('3-9'), v: "\\lceil\\left\\{\\right\\}\\rceil", i: "write" },
  ],
  [
    { k: getImage('4-1'), v: "\\sum", i: "" },
    { k: getImage('4-2'), v: "-", i: "" },
    { k: getImage('4-3'), v: "", i: "" },
    { k: getImage('4-4'), v: "\\sqrt", i: "" },
    { k: getImage('4-5'), v: "\\frac", i: "" },
    { k: getImage('4-6'), v: "\\exp\\left(\\right)", i: "write" },
    { k: getImage('4-7'), v: "\\sin\\left(\\right)", i: "write" },
    { k: getImage('4-8'), v: "\\cos\\left(\\right)", i: "write" },
    { k: getImage('4-9'), v: "\\tan\\left(\\right)", i: "write" },
  ],
  [
    { k: getImage('5-1'), v: "\\sinh\\left(\\right)", i: "write" },
    { k: getImage('5-2'), v: "\\cosh\\left(\\right)", i: "write" },
    { k: getImage('5-3'), v: "\\tanh\\left(\\right)", i: "write" },
    { k: getImage('5-4'), v: "\\max\\left(\\right)", i: "write" },
    { k: getImage('5-5'), v: "\\min\left(\right)", i: "write" },
  ],
  [
    { k: getImage('6-1'), v: "\\sum_{ }^{ }\\left\\{\\right\\}", i: "write" },
    { k: getImage('6-2'), v: "\\prod_{}^{}\\left\\{\\right\\}", i: "write" },
    { k: getImage('6-3'), v: "\\text{concat}_{}^{}\\left\\{\\right\\}", i: "write" },
    { k: getImage('6-4'), v: "\\text{mean}_{}^{}\\left\\{\\right\\}", i: "write" },
    { k: getImage('6-5'), v: "\\max_{}^{}\\left\\{\\right\\}", i: "write" },
  ],
  [
    { k: getImage('7-1'), v: "\\min_{}^{}\\left\\{\\right\\}", i: "write" },
    { k: getImage('7-2'), v: "\\text{argmin}_{}^{}\\left\\{\\right\\}", i: "write" },
    { k: getImage('7-3'), v: "\\text{argmax}_{}^{}\\left\\{\\right\\}", i: "write" },
  ],
];
interface panel {
  id: number;
  src: string;
  cmd: string;
}
const mathCommand = (cmd: string,type: string) => {
  if(type == "write"){
    mathField.write(cmd)
  }else{
    mathField.cmd(cmd)
  }
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
  display: none;
}
.toolbar-primary {
  background: #2a2a2a;
  position: absolute;
  top: 10px;
  display: none;
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
  width: 50px;
  height: 50px;
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
/* .panel_box {
  width: 20px;
  height: 20px;
  padding: 5px;
} */
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