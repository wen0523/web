<template>
  <div class="Wen">
    <span>Wen</span>
  </div>
  <el-menu class="el-menu-demo" mode="horizontal" active-text-color="white">
    <el-menu-item @click="handleMenuItemClick" index="">
      <span><font-awesome-icon icon="fa-home" />&nbsp;主页</span>
    </el-menu-item>
    <el-sub-menu index="sub-menu">
      <template #title>
        <span><font-awesome-icon icon="fa-list" />&nbsp;文章</span>
      </template>
      <el-menu-item class="item" @click="handleMenuItemClick" index="Archives">
        <font-awesome-icon icon="fa-box-archive" pull="left" transform="down-10.2"></font-awesome-icon>归档
      </el-menu-item>
      <el-menu-item class="item" @click="handleMenuItemClick" index="Tags">
        <font-awesome-icon icon="fa-tag" pull="left" transform="down-10.2" />标签
      </el-menu-item>
      <el-menu-item class="item" @click="handleMenuItemClick" index="Categories">
        <font-awesome-icon icon="fa-folder-open" pull="left" transform="down-10.2" />分类
      </el-menu-item>
    </el-sub-menu>
    <el-menu-item @click="handleMenuItemClick" index="Comments">
      <span><font-awesome-icon icon="fa-envelope-open" />&nbsp;留言板</span>
    </el-menu-item>
    <el-menu-item @click="handleMenuItemClick" index="Link">
      <span><font-awesome-icon icon="fa-link" />&nbsp;友链</span>
    </el-menu-item>
    <el-menu-item @click="handleMenuItemClick" index="About">
      <span><font-awesome-icon icon="fa-heart" />&nbsp;关于</span>
    </el-menu-item>
  </el-menu>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';

const $router = useRouter();

const handleMenuItemClick = (event: { index: string }) => {
  const route = title_change(event.index);
  $router.push({ path: "/" + route });
}

const title_change = (title: string) => {
  switch (title) {
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
      break;
    case "About":
      document.title = "关于 | Wen";
      break;
  }
  return title;
}
</script>

<style>
/*一级菜单字体*/
span{/*basic*/
  font-weight: bold;
  font-size: 1.3em;
  color: black;
  display: flex;
  align-items: center;/*使图标居中*/
}

.dark span{
  color: white;
}

.top span{/*top*/
  color: white;
}
/*名字*/
.Wen {
  background-color: transparent;
  position: fixed;
  left: 4em;
  top: 0.5em;

  span {
    font-size: 1.7em;
  }
}

/*
总体
*/
.el-menu-demo {
  height: 2.15em;
  position: fixed;
  left: 36em;
  width: 33em;
  background: transparent;
  top: 1.2em;
  border-bottom-width: 0 !important;
}

/*
一级
*/
.el-menu-demo>.el-menu-item {
  /*静态*/
  border-bottom-width: 0 !important;
  padding-left: 0.5em;
  padding-right: 0.5em;
}

.el-menu-demo>.el-menu-item:hover {
  /*悬浮*/
  background: transparent !important;
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
  border-bottom-width: 0 !important;
  padding-left: 0.5em;
  /*el-sub-menu左边的内边距*/
}

.el-icon {
  /*文章后面的箭头的位置*/
  position: absolute;
  right: 0.5em !important;
}

.el-sub-menu {
  width: 6em;
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
  left: -6em;
  width: 20em;
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
}
</style>