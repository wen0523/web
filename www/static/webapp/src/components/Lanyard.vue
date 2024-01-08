<template>
    <div id="rope"></div><!--绳子-->
    <div id="lanyard" @click="hadleClick"><!--小猫-->
        <div class="comment"><!--对话框-->
            <p class="comment-p">点击我</p>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted, nextTick } from 'vue';
import type { RouteLocationNormalizedLoaded } from 'vue-router';// 导入类型语句
import router from '../router'; // 调整成你的实际路径

//各部分元素高度
var HeightHeader = document.getElementById('header')!.offsetHeight;
var HeightMain = 0;//高度改变，动态获得。
var HeightFooter = document.getElementById('footer')!.offsetHeight;
var HeightHMF = 0;//三项总高度
var viewportHeight = window.innerHeight;//窗口可视高度
var scrollHeight = 0;// 获取垂直方向上的滚动条滚动高度
var Height = 0;//最终高度

//点击小猫返回顶部(平滑)
function hadleClick() {
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: 'smooth'
    });
}

onMounted(() => {
    const lanyard = document.getElementById('lanyard')!;
    const rope = document.getElementById('rope')!;

    //检测路由变化
    router.afterEach((to: RouteLocationNormalizedLoaded, from: RouteLocationNormalizedLoaded) => {
        window.scrollTo(0, 0);//保持新页面处在顶部

        // 使用 nextTick 来确保在 DOM 更新完成后执行回调，为切换后的页面。
        nextTick(() => {
            HeightMain = document.getElementById('main')!.offsetHeight;
        });
    });

    //滚动事件
    window.addEventListener('scroll', () => {
        HeightHMF = HeightHeader + HeightMain + HeightFooter;
        scrollHeight = document.documentElement.scrollTop;
        Height = (scrollHeight / (HeightHMF - viewportHeight)) * viewportHeight * 0.7;
        if (Height <= 1) {
            lanyard.style.top = -64 + 'px';
            rope.style.height = 0 + 'px';
        } else {
            lanyard.style.top = Height + 50 + 'px';
            rope.style.height = Height + 60 + 'px';
        }

    });
});
</script>

<style scoped>
#lanyard {
    position: fixed;
    right: 50px;
    top: -64px;
    width: 64px;
    height: 64px;
    background-image: url("https://bu.dusays.com/2022/07/20/62d812db74be9.png");
    background-repeat: no-repeat;
    background-size: contain;
}

#rope {
    background-color: rgb(255, 255, 255, 0.3);
    background-image: linear-gradient(45deg, rgba(20, 7, 7, 0.61) 25%, transparent 25%, transparent 50%, rgba(38, 16, 16, 0.5) 50%, rgba(94, 27, 27, 0.436) 75%, transparent 75%, transparent);
    width: 6px;
    position: fixed;
    right: 81px;
    top: 0px;
}

#lanyard:hover {
    .comment {
        opacity: 1;
        transition: 0.5s;
    }
}

.comment {
    position: relative;
    bottom: 72px;
    right: 68px;
    width: 100px;
    height: 100px;
    background-image: url("https://bu.dusays.com/2022/07/20/62d812d95e6f5.png");
    background-size: contain;
    opacity: 0;
}

.comment .comment-p {
    position: relative;
    top: 38px;
    left: 25px;
    color: black;
    font-weight: bold;
}
</style>