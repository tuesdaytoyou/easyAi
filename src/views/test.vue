<template>
<div contenteditable="true">
    <p>a+b</p>
</div>
<div style="height:100px;width:100px;background:red;" @click="log()"></div>
</template>

<script setup lang="ts">

const log = () => {
  const selection = window.getSelection()
  console.log(selection)
}
</script>