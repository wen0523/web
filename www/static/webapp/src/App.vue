<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Menu from './components/Menu.vue'
import new_Button from './components/new_Button.vue'
import Love_2D from './components/Love_2D.vue'
import Mouse from './components/Mouse.vue'
import Weather from './components/Weather.vue'
import Author_card from './components/Author_card.vue'
import { ref } from 'vue'

/*屏幕滑动的时候隐藏导航栏js*/
const header = document.getElementById("header")!;
let isActive = ref(false)
let lastScrollPosition = ref(window.scrollY)
window.addEventListener('scroll', () => {
    const pageY = window.scrollY  // 滚动条距离顶部的长度
    if (lastScrollPosition.value > pageY) {
        if (header.classList.contains("show")) {
            header.classList.remove("show");
            header.classList.add("hide");
        }
    } else {
        if (header.classList.contains("hide")) {
            header.classList.remove("hide");
            header.classList.add("show");
        }
    }
    lastScrollPosition.value = pageY
})

</script>

<template>
    <!--整体布局-->
    <el-container>
        <el-header id="header">
            <Menu />
            <Weather />
            <new_Button />
        </el-header>
        <el-container>
            <el-asider>
                <h1>fff</h1>
                <Author_card />
            </el-asider>
            <el-main><router-view /></el-main>
        </el-container>
        <el-footer>
            <h1>
                Footer
            </h1>
        </el-footer>
    </el-container>

    <!-- 独立部分 -->
    <Love_2D />
    <Mouse />
</template>

<style>
/*导航栏*/
.show {
    animation: show-animation 1s forwards ease-in-out;
}

.hide {
    animation: hide-animation 1s forwards ease-in-out;
}

@keyframes show-animation {
    0% {
        height: 0;
    }
    100% {
        height: 100%;
    }
}

el-asider {
    width: 25em;
    padding-top: 4em;
}

.el-main {
    padding: 4em;
    padding-left: 0;
}
</style>