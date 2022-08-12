<template>
  <div class="flex items-center justify-center h-screen px-60">
    <div class="mx-12 border-solid border border-black rounded-lg" style="width:490px;height:620px">
      <div><img class="rounded-lg" :src="getImage('home-card1')"></div>
      <div>
        <div class="text-2xl mx-2 my-4">图像分类</div>
        <div class="mx-2 my-4">分类识别是监督式机器学习最常见的使用场景。</div>
        <div class="w-10/12 bg-clickbtn mx-auto my-2 py-2 text-center rounded-lg text-white">开始学习</div>
      </div>
    </div>
    <div class="mx-12 border-solid border border-black rounded-lg" style="width:490px;height:620px">
      <div><img class="rounded-lg" :src="getImage('home-card1')"></div>
      <div>
        <div class="text-2xl mx-2 my-4">图像分类</div>
        <div class="mx-2 my-4">分类识别是监督式机器学习最常见的使用场景。</div>
        <div class="w-10/12 bg-clickbtn mx-auto my-2 py-2 text-center rounded-lg text-white">开始学习</div>
      </div>
    </div>
    <div class="mx-12 border-solid border border-black rounded-lg" style="width:490px;height:620px">
      <div><img class="rounded-lg" :src="getImage('home-card1')"></div>
      <div>
        <div class="text-2xl mx-2 my-4">图像分类</div>
        <div class="mx-2 my-4">分类识别是监督式机器学习最常见的使用场景。</div>
        <div class="w-10/12 bg-clickbtn mx-auto my-2 py-2 text-center rounded-lg text-white">开始学习</div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
const getImage = (name: string): string => {
  return new URL(`../assets/images/home/${name}.png`, import.meta.url).href;
};
</script>