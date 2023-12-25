<template>
    <div class="live_2d">
        <live2d :style="style" :model="['Potion-Maker/Pio', 'school-2017-costume-yellow']" :direction="direction"
            :size="size"></live2d>
    </div>
</template>
  
<script lang="ts">

import live2d from 'vue-live2d'

export default {
    name: 'App',
    components: {
        live2d
    },
    data() {
        return {
            direction: 'left',
            style: '',
            width: 500,
            height: 500,
            size: 250,
        }
    }
}
</script>
  
<style>
.live_2d {
    position: fixed;
    left: 0;
    bottom: 0;
    z-index: 9999;
}
</style>