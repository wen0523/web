import { createRouter, createWebHistory } from 'vue-router'
import Home_Page from '../views/Home_Page.vue'//主页
import ArchivesView from '../views/Archives.vue'//归档
import TagsView from '../views/Tags.vue'//标签
import CategoriesView from '../views/Categories.vue'//分类
import CommentsView from '../views/Comments.vue'//留言板
import LinkView from '../views/Link.vue'//友链
import AboutView from '../views/About.vue'//关于

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: '/',
      component: Home_Page
    },
    {
      path: '/Archives',
      name: 'Archives',
      component: ArchivesView
    },
    {
      path: '/Tags',
      name: 'Tags',
      component: TagsView
    },
    {
      path: '/Categories',
      name: 'Categories',
      component: CategoriesView
    },
    {
      path: '/Comments',
      name: 'Comments',
      component: CommentsView
    },
    {
      path: '/Link',
      name: 'Link',
      component: LinkView
    },
    {
      path: '/About',
      name: 'About',
      component: AboutView
    }
  ]
})

export default router
