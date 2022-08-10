<template>
  <div class="flex items-center justify-center h-screen p-6">
    <div class="w-3/12 mx-12">
      <div><img :src="getImage('home-card1')"></div>
      <div>
        <div>图像分类</div>
        <div>分类识别是监督式机器学习最常见的使用场景。</div>
        <div>开始学习</div>
      </div>
    </div>
    <div class="w-3/12 mx-12">
      <div><img :src="getImage('home-card1')"></div>
      <div>
        <div>图像分类</div>
        <div>分类识别是监督式机器学习最常见的使用场景。</div>
        <div>开始学习</div>
      </div>
    </div>
    <div class="w-3/12 mx-12">
      <div><img :src="getImage('home-card1')"></div>
      <div>
        <div>图像分类</div>
        <div>分类识别是监督式机器学习最常见的使用场景。</div>
        <div>开始学习</div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
const getImage = (name: string): string => {
  return new URL(`../assets/images/home/${name}.png`, import.meta.url).href;
};
</script>