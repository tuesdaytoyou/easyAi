import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
import store from './store/index'
import { Image } from "ant-design-vue";
// import "ant-design-vue/dist/antd.css";
// import './plugins/mathlive.js'
import './plugins/mathquill-0.10.1/mathquill.css'
import './plugins/mathquill-0.10.1/mathquill.js'
import './assets/css/index.css'
import './assets/css/css.css'

const APP = createApp(App)
APP.use(router)
APP.use(store)
APP.use(Image)
APP.mount('#app')
