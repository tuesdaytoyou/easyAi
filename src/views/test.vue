<template>
  <math-field
    id="formula"
    style="
        font-size: 32px; 
        padding: 8px;"
  >x=\frac{-b\pm \sqrt{b^2-4ac}}{2a}</math-field>
  <span id="latex"></span>
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
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from "vue";
let mathFieldDom: any;
let latexDom: HTMLElement;
let initMathLive = function() {
  mathFieldDom = document.getElementById("formula") as HTMLElement;
  latexDom = document.getElementById("latex") as HTMLElement;
  mathFieldDom.addEventListener("input", (ev: Event) => {
    let event = <HTMLInputElement>ev.target;
    latexDom.innerHTML = event.value;
  });
};
onMounted(initMathLive);

let toolbarTop = ref("200px");
let toolbarLeft = ref("500px");
let toolArrowLeft = ref("0px");
let toolPrimaryLeft = ref("0px");
const setBoxStyle = () => {
  toolbarTop.value = mathFieldDom.offsetTop + mathFieldDom.offsetHeight + "px";
  toolbarLeft.value = mathFieldDom.offsetLeft + "px";
  toolArrowLeft.value = mathFieldDom.offsetWidth / 2 + "px";
  toolPrimaryLeft.value = mathFieldDom.offsetWidth / 2 - 45 + "px";
};

let showToolbar = ref(true);
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
// onMounted(listenClick);
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
  [
    { k: getImage("1-1"), v: "+", i: "" },
    { k: getImage("1-2"), v: "-", i: "" },
    { k: getImage("1-3"), v: "\\times", i: "" },
    { k: getImage("1-4"), v: "/", i: "" },
    { k: getImage("1-5"), v: "*", i: "" },
    { k: getImage("1-6"), v: "\\cdot", i: "" },
    { k: getImage("1-7"), v: "<", i: "" },
    { k: getImage("1-8"), v: ">", i: "" },
    { k: getImage("1-9"), v: "\\leq", i: "" },
    { k: getImage("1-10"), v: "=", i: "" }
  ],
  [
    { k: getImage("2-1"), v: "\\neq", i: "" },
    { k: getImage("2-2"), v: "\\geq", i: "" },
    { k: getImage("2-3"), v: "\\wedge", i: "" },
    { k: getImage("2-4"), v: "\\vee", i: "" },
    { k: getImage("2-5"), v: "\\neg", i: "" },
    { k: getImage("2-6"), v: "\\in", i: "" },
    { k: getImage("2-7"), v: "\\sum_{i=0}^n\\placeholder{}\\limits", i: "" },
    { k: getImage("2-8"), v: "\\left\\{\\right\\}", i: "" },
    { k: getImage("2-9"), v: "\\pi", i: "" },
    { k: getImage("2-10"), v: "\\triangleright", i: "" }
  ],
  [
    { k: getImage("3-1"), v: "^\\placeholder{}", i: "" },
    { k: getImage("3-2"), v: "_\\placeholder{}", i: "" },
    { k: getImage("3-3"), v: "", i: "" },
    { k: getImage("3-4"), v: "\\sqrt", i: "" },
    { k: getImage("3-5"), v: "\\frac", i: "" },
    { k: getImage("3-6"), v: "", i: "" },
    { k: getImage("3-7"), v: "\\lvert\\placeholder{}\\rvert", i: "" },
    {
      k: getImage("3-8"),
      v: "\\lfloor\\placeholder{}\\rfloor",
      i: "write"
    },
    { k: getImage("3-9"), v: "\\lceil\\placeholder{}\\rceil", i: "write" }
  ],
  [
    { k: getImage("4-1"), v: "\\lVert\\placeholder{}\\rVert", i: "" },
    { k: getImage("4-2"), v: "\\placeholder{}\\urcorner", i: "" },
    { k: getImage("4-3"), v: "\\placeholder{}\\Vert\\placeholder{}", i: "" },
    { k: getImage("4-4"), v: "\\lVert\\placeholder{}\\rVert_{\\placeholder{}}", i: "" },
    { k: getImage("4-5"), v: "\\placeholder{}_\\placeholder{}^\\placeholder{}", i: "" },
    { k: getImage("4-6"), v: "\\exp(\\placeholder{})", i: "write" },
    { k: getImage("4-7"), v: "\\sin(\\placeholder{})", i: "write" },
    { k: getImage("4-8"), v: "\\cos(\\placeholder{})", i: "write" },
    { k: getImage("4-9"), v: "\\tan(\\placeholder{})", i: "write" }
  ],
  [
    { k: getImage("5-1"), v: "\\sinh(\\placeholder{})", i: "write" },
    { k: getImage("5-2"), v: "\\cosh(\\placeholder{})", i: "write" },
    { k: getImage("5-3"), v: "\\tanh(\\placeholder{})", i: "write" },
    { k: getImage("5-4"), v: "\\max(\\placeholder{},\\placeholder{})", i: "write" },
    { k: getImage("5-5"), v: "\\min(\\placeholder{},\\placeholder{})", i: "write" }
  ],
  [
    { k: getImage("6-1"), v: "\\sum_{i=0}^n\\placeholder{}\\limits", i: "write" },
    { k: getImage("6-2"), v: "\\prod_{i=0}^n\\placeholder{}\\limits", i: "write" },
    {
      k: getImage("6-3"),
      v: "\\coprod_{i=0}^n\\placeholder{}\\limits",
      i: "write"
    },
    {
      k: getImage("6-4"),
      v: "\\text{mean}_\\placeholder{}^\\placeholder{}\\placeholder{}",
      i: "write"
    },
    { k: getImage("6-5"), v: "\\max_\\placeholder{}^\\placeholder{}\\placeholder{}", i: "write" }
  ],
  [
    { k: getImage("7-1"), v: "\\min_\\placeholder{}^\\placeholder{}\\placeholder{}", i: "write" },
    {
      k: getImage("7-2"),
      v: "\\text{argmin}_\\placeholder{}^\\placeholder{}\\placeholder{}",
      i: "write"
    },
    {
      k: getImage("7-3"),
      v: "\\text{argmax}_\\placeholder{}^\\placeholder{}\\placeholder{}",
      i: "write"
    }
  ]
];
interface panel {
  id: number;
  src: string;
  cmd: string;
}
const mathCommand = (cmd: string, type: string) => {
  if (type == "write") {
    mathFieldDom.executeCommand(["insert", cmd]);
  } else {
    mathFieldDom.executeCommand(["insert", cmd]);
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