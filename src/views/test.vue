<template>
  <p>Type math here: <span id="math-field"></span></p>
  <p>LaTeX of what you typed: <span id="latex"></span></p>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from "vue";
let initMathQuill = function() {
  var mathFieldSpan = document.getElementById('math-field');
  var latexSpan = document.getElementById('latex');

  var MQ = window.MathQuill.getInterface(2); // for backcompat
  var mathField = MQ.MathField(mathFieldSpan, {
    spaceBehavesLikeTab: true, // configurable
    handlers: {
      edit: function() { // useful event handlers
        latexSpan!.textContent = mathField.latex(); // simple API
      }
    }
  });
};
onMounted(initMathQuill);
</script>