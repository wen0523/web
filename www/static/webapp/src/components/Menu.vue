<template>
  <el-menu  class="el-menu-demo" mode="horizontal" active-text-color="white">
    <el-menu-item @click="handleMenuItemClick('')">主页</el-menu-item>
    <el-sub-menu>
      <template #title>文章</template>
      <el-menu-item class="item" @click="handleMenuItemClick('Archives')">归档</el-menu-item>
      <el-menu-item class="item" @click="handleMenuItemClick('Tags')">标签</el-menu-item>
      <el-menu-item class="item" @click="handleMenuItemClick('Categories')">分类</el-menu-item>
    </el-sub-menu>
    <el-menu-item @click="handleMenuItemClick('Comments')">留言板</el-menu-item>
    <el-menu-item @click="handleMenuItemClick('Link')">友链</el-menu-item>
    <el-menu-item @click="handleMenuItemClick('About')">关于</el-menu-item>
  </el-menu>
</template>

<script lang="ts" setup>
import { useRouter } from 'vue-router';

const $router = useRouter();

const handleMenuItemClick = (route: string) => {
  title_change(route);
  $router.push({ path:"/"+route});
}

const title_change = (title: string) => {
  switch (title){
    case "":
      document.title = "Wen";
      break;
    case "Archives":
      document.title = "归档 | Wen";
      break;
    case "Tags":
      document.title = "标签 | Wen";
      break;
    case "Categories":
      document.title = "分类 | Wen";
      break;
    case "Comments":
      document.title = "留言板 | Wen";
      break;
    case "Link":
      document.title = "友链 | Wen";
      break
    case "About":
      document.title = "关于 | Wen";
  }
}
</script>
<style>
/*
总体
*/
.el-menu-demo {
  height: 2.15em;
  position: fixed;
  left: 36em;
  width: 32em;
  background: transparent;
  top: 1.2em;
  border-bottom-width: 0 !important;
}

/*
一级
*/
.el-menu-demo>.el-menu-item {
  /*静态*/
  font-weight: bold;
  font-size: 1.15em;
  color: white !important;
  border-bottom-width: 0 !important;
}

.el-menu-demo>.el-menu-item:hover {
  /*悬浮*/
  background: transparent !important;
  color: white !important;
  border-bottom-width: 0.3em !important;
  border-bottom-color: rgb(37, 69, 137) !important;
}

.el-menu-demo>.el-menu-item:focus {
  /*焦点*/
  background: transparent !important;
}

/*
二级
*/

.item {
  /*静态*/
  /*light*/
  display: inline-block !important;
  color: black;
  font-weight: bold;
  font-size: 1.4em;
  background: transparent !important;
}

.dark .item {
  /*静态*/
  /*dark*/
  color: white !important;
}

.el-menu-item.item:hover {
  /*悬浮*/
  /*light*/
  border-radius: 0.4em;
  color: black !important;
  background-color: rgb(204, 192, 255, 0.6) !important;
}

.dark .el-menu-item.item:hover {
  /*悬浮*/
  /*dark*/
  color: white !important;
}

li.el-menu-item.is-active.item {
  /*激活*/
  /*light*/
  color: black !important;
}

.dark li.el-menu-item.is-active.item {
  color: white !important;
}

/*
sub-menu
*/
.el-sub-menu__title {
  /*静态*/
  /*文章*/
  font-weight: bold;
  font-size: 1.15em;
  color: white !important;
  border-bottom-width: 0 !important;
}

.el-sub-menu :hover {
  /*悬浮*/
  /*文章*/
  border-bottom-width: 0.3em !important;
  border-bottom-color: rgb(37, 69, 137) !important;
  background: transparent !important;
}

.el-popper {
  /*弹窗位置的第二层*/

  border-width: 0 !important;
  background: transparent !important;
}

.el-menu--popup-container {
  /*弹窗位置的第三层*/
  /*light*/
  position: relative;
  left: -3.5em;
  width: 14.5em;
  border-radius: 1em;
  background-color: white;
}

.dark .el-menu--popup-container {
  /*弹窗位置的第三层*/
  /*dark*/
  background-color: rgb(0, 0, 0, 0.6);
}

.el-menu--popup-bottom-start {
  /*第三层中的ul*/
  background: transparent !important;
  position: relative !important;
  right: -0.55em !important;
}</style>