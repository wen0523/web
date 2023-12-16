<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Menu from './components/Menu.vue'
import new_Button from './components/new_Button.vue'
import Love_2D from './components/Love_2D.vue'
</script>

<template>
    <Menu />
    <new_Button />
    <Love_2D />
    <router-view></router-view>
</template>
<style>
.new {
  background-color: white;
  width: 100px;
  height: 100px;
}
</style>