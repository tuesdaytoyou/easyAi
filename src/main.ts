import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
import store from './store/index'
import Antd from "ant-design-vue";
import "ant-design-vue/dist/antd.css";
import './plugins/jquery.min.js'
import './plugins/mathquill-0.10.1/mathquill.css'
import './plugins/mathquill-0.10.1/mathquill.js'
import './plugins/mathlive.js'
import './assets/css/index.css'
import './assets/css/css.css'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import axios from 'axios'

axios.defaults.baseURL = '/api'

const app = createApp(App)

app.config.warnHandler = () => null

app.mount('#app')

const APP = createApp(App)
APP.use(router)
APP.use(store)
APP.use(Antd)
APP.use(ElementPlus)
APP.mount('#app')
