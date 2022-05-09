import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/home.vue') // 建议进行路由懒加载，优化访问性能
  },
  {
    path: '/test',
    name: 'test',
    component: () => import('@/views/test.vue') // 建议进行路由懒加载，优化访问性能
  },
  {
    path: '/math',
    name: 'math',
    component: () => import('@/views/math.vue') // 建议进行路由懒加载，优化访问性能
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router