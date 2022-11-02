import { createRouter, createWebHistory, RouteRecordRaw, createWebHashHistory } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/homepage.vue') // 建议进行路由懒加载，优化访问性能
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
  {
    path: '/mathinput',
    name: 'mathinput',
    component: () => import('@/views/mathinput.vue') // 建议进行路由懒加载，优化访问性能
  },
  {
    path: '/homepage',
    name: 'homepage',
    component: () => import('@/views/homepage.vue') // 建议进行路由懒加载，优化访问性能
  },
  {
    path: '/matheditor',
    name: 'matheditor',
    component: () => import('@/views/matheditor.vue') // 建议进行路由懒加载，优化访问性能
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router