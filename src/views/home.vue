<template>
  <div style="width:200px;height:200px;background:red">click me</div>
  <math-field>f(x) = x + 1</math-field>
  <math-field>
    x=\frac{-b\pm \sqrt{b^2-4ac}}{2a}
  </math-field>
  <div id="math">
    <p>
    When $a \ne 0$, there are two solutions to \(ax^2 + bx + c = 0\) and they are
    $$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$
    </p>
  </div>
</template>

<script setup lang="ts">
import { initMathjaxConfig } from '../utils/mathJaxInt'
import { onMounted } from 'vue'
const mathJaxInt = () => {
  initMathjaxConfig()
  // 如果，不传入第三个参数，则渲染整个document
  // window.MathJax.Hub.Queue([
  //     "Typeset",
  //     window.MathJax.Hub,
  //     document.getElementById("math")
  // ]);
}
onMounted(mathJaxInt)
</script>
