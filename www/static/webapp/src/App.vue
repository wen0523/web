<script setup lang="ts">
import { RouterView } from 'vue-router'
import Menu from './components/Menu.vue'
import new_Button from './components/new_Button.vue'
import Love_2D from './components/Love_2D.vue'
import Mouse from './components/Mouse.vue'
import Weather from './components/Weather.vue'
import Author_card from './components/Author_card.vue'
import Clock from './components/Clock.vue'
//导航栏

</script>

<template>
    <!--页面整体布局-->
    <header>
        <Menu />
        <Weather />
        <new_Button />
    </header>

    <main>
        <div class="left-column">
            <div class="personal_card day" id="my_card">
                <Author_card />
                <Clock />
            </div>
        </div>
        <div class="right-column">
            <router-view></router-view>
        </div>
    </main>

    <footer>
        <p>Page Footer</p>
    </footer>

    <Love_2D />
    <Mouse />
</template>
<style scoped>
/*页面样式*/
header {
    height: 100px;
    margin-bottom: 30px;
}

main {
    display: flex;
    flex: 1;
}

.left-column {
    padding: 20px;
    padding-left: 140px;
    display: flex;
    flex-direction: column;
}

.right-column {
    padding-right: 140px;
    flex: 1;
}

footer {
    text-align: center;
    margin-top: 20px;
    height: 200px;
    /* 固定页脚高度 */
}

/*导航栏*/

/*Author_card和Clock底层卡片*/
.personal_card {
    /*basic样式*/
    display: flex;
    justify-content: space-between;
    flex-direction: column;
    align-items: center;
    width: 290px;
    height: 400px;
    border: none;
    border-radius: 10px;
}

.personal_card.day {
    /*day*/
    background: radial-gradient(ellipse farthest-side at 76% 77%, rgba(245, 228, 212, 0.25) 4%, rgba(255, 255, 255, 0) calc(4% + 1px)), radial-gradient(circle at 76% 40%, #fef6ec 4%, rgba(255, 255, 255, 0) 4.18%), linear-gradient(135deg, #ff0000 0%, #000036 100%), radial-gradient(ellipse at 28% 0%, #ffcfac 0%, rgba(98, 149, 144, 0.5) 100%), linear-gradient(180deg, #cd6e8a 0%, #f5eab0 69%, #d6c8a2 70%, #a2758d 100%);
    background-blend-mode: normal, normal, screen, overlay, normal;
}

.personal_card.night {
    /*night*/
    background:
        radial-gradient(ellipse farthest-side at 76% 77%, rgba(30, 12, 12, 0.25) 4%, rgba(0, 0, 0, 0) calc(4% + 1px)),
        /*河水*/
        radial-gradient(circle at 76% 40%, #dfdede 4%, rgba(255, 255, 255, 0) calc(2.5% + 8px)),
        /*月亮*/
        linear-gradient(135deg, rgb(1, 20, 39) 0%, rgb(18, 44, 88) 100%),
        /*整体*/
        radial-gradient(ellipse at 28% 0%, rgba(255, 255, 255, 0) 0%, rgba(227, 227, 227, 0.5) 100%),
        /*倒影*/
        linear-gradient(180deg, #000000 0%, #0f0f1f 69%, #1f1f1f 70%, #121212 100%);
    background-blend-mode: normal, normal, screen, overlay, normal;
}</style>