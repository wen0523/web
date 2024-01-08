import './assets/main.css'
import './assets/base.css'
import './assets/div-base.css'
import './assets/scroll_bar.css'
import './assets/font.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

import App from './App.vue'
import router from './router'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */

import { fas } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'



/* add icons to the library */
library.add(fas,far,fab)

const app = createApp(App)

app.use(ElementPlus)
app.use(createPinia())
app.use(router)
app.component('font-awesome-icon', FontAwesomeIcon)/*注册图标到app*/

app.mount('#app')
