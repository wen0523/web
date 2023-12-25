<template>
    <div class="shell">
        <div class="photo">
            <img src="/card2.png" alt="">
        </div>
        <div class="content">
            <div class="text">
                <h2>Wen-Blog</h2>
                <h6>&nbsp;&nbsp;&nbsp;Wenの小窝</h6>
            </div>
        </div>
        <div class="btn" @click="Pop"><span></span></div>
        <div class="box">
            <i><font-awesome-icon icon="fa-brands fa-github" size="xl"></font-awesome-icon></i>
            <i><font-awesome-icon icon="fa-brands fa-twitter" size="xl"></font-awesome-icon></i>
            <i><font-awesome-icon icon="fa-brands fa-telegram" size="xl"></font-awesome-icon></i>
            <i><font-awesome-icon icon="fa-solid fa-envelope" size="xl"></font-awesome-icon></i>
        </div>
    </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';

let btn: Element;
let box: Element;

onMounted(() => {/*在DOM组件被创建后调用*/
    btn = document.getElementsByClassName('btn')[0]!;
    box = document.getElementsByClassName('box')[0]!;
});
const Pop = () => {
    //含active时的操作
    if (btn.classList.contains('active')) {
        btn.classList.remove('active');//关闭选项
        box.classList.remove('open');
    }
    //不含active时的操作
    else {
        btn.classList.add('active');//弹出选项
        box.classList.add('open');
    }
}
</script>

<style scoped>
* {
    padding: 0;
    margin: 0;
}

.shell {
    width: 247.5px;
    height: 75px;
    position: absolute;
    top: 17em;
    left: 12.5em;
    transform: translate(-50%, -50%);
    border-radius: 5px;
    background-color: #fafafa;
    box-shadow: 0 0 2rem #babbbc;
    animation: show-shell 0.5s forwards ease-in-out;
}

@keyframes show-shell {
    0% {
        width: 0;
    }
}

.photo,
.content {
    box-sizing: border-box;
}

.photo {
    width: 75px;
    height: 75px;
    border-radius: 50%;
    overflow: hidden;
    border: 3.75px solid #fafafa;
    background-color: #fafafa;
    margin-left: -37.5px;
    box-shadow: 0 0 0.5rem #babbbc;
    animation: rotate-photo 0.5s forwards ease-in-out;
}

@keyframes rotate-photo {
    100% {
        transform: rotate(-360deg);
    }
}

.photo img {
    width: 100%;
}

.content {
    padding: 7.5px;
    overflow: hidden;
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    z-index: -1;
}

.content::before {
    content: "";
    position: absolute;
    width: 172.5px;
    height: 112.5px;
    left: 0;
    top: -15px;
    z-index: -1;
    transform: rotate(-8deg);
    background-image: linear-gradient(to top, #6866ee 0%, #fbc8d4 100%);
}

.content .text {
    margin-top: 1px;
    margin-left: 35px;
}

.content .text h3,
.content .text h6 {
    font-weight: normal;
    margin: 2.25px 0;
    letter-spacing: 0.5px;
    white-space: nowrap;
}

.btn {
    background-color: rgb(106, 106, 245);
    width: 37.5px;
    height: 37.5px;
    position: absolute;
    right: 18.75px;
    top: 18.75px;
    border-radius: 50%;
    z-index: 1;
    cursor: pointer;
    transition-duration: 0.3s;
    animation: pop-btn 0.3s both ease-in-out 0.5s;
}

@keyframes pop-btn {
    0% {
        transform: scale(0);
    }

    80% {
        transform: scale(1.2);
    }

    100% {
        transform: scale(1);
    }
}

.btn:hover {
    box-shadow: 0 0 0 5px rgba(170, 187, 204, 0.5);
}

.btn span {
    width: 60%;
    height: 1.5px;
    position: absolute;
    background-color: white;
    top: 50%;
    left: 20%;
    transform: translateY(-50%);
    animation: to-hamburger 0.3s forwards ease-in-out;
}

.btn span::before,
.btn span::after {
    content: "";
    width: 100%;
    height: 1.5px;
    position: absolute;
    background-color: white;
    transition-duration: 0.3s;
    transform: rotate(0deg);
    right: 0;
}

.btn span::before {
    margin-top: -5.25px;
}

.btn span::after {
    margin-top: 5.25px;
}

.btn.active span {
    animation: to-arrow 0.3s forwards ease-in-out;
}

.btn.active span::before,
.btn.active span::after {
    width: 60%;
    right: -0.75px;
}
.btn.active span::before {
    transform: rotate(45deg);
}

.btn.active span::after {
    transform: rotate(-45deg);
}

@keyframes to-hamburger {
    from {
        transform: translateY(-50%) rotate(-180deg);
    }
}

@keyframes to-arrow {
    from {
        transform: translateY(-50%) rotate(0deg);
    }

    to {
        transform: translateY(-50%) rotate(180deg);
    }
}

.box {
    opacity: 0;
    border-radius: 50%;
    background-color: rgba(255, 255, 255, 0.7);
    position: absolute;
    top: 50%;
    right: -30%;
    transform: translate(-50%, -50%);
    transition-duration: 0.3s;
    box-shadow: 0 0 10px #fff;
    border: 5px #fff solid;
}

.box::after {
    content: '';
    display: block;
    width: 90px;
    height: 90px;
    background-image: url(/card1.gif);
    background-size: cover;
    opacity: .7;
    border-radius: 50%;
}

.box i {
    width: 45px;
    height: 45px;
    border-radius: 50%;
    background-color: #ececec;
    font-size: 19.5px;
    text-align: center;
    line-height: 45px;
    position: absolute;
    left: 13.5px;
    top: calc(60px - 50px/2)*0.75;
    box-shadow: 0 0 10px #fff;
    color: rgb(106, 106, 245);
    background-color: #fff;
    transition-duration: 0.3s;
}

.box i:hover {
    transition-delay: initial !important;
    box-shadow: 0 0 0 5px #babbbc;
    background-color: rgb(106, 106, 245);
    color: #fff;
}

.box.open {
    opacity: 1;
}

.box.open i {
    left: 15px;
    opacity: 1;
}

.box.open i:nth-of-type(1) {
    transform: rotate(-90deg) translateX(60px) rotate(90deg);
    transition-delay: 0s;
}

.box.open i:nth-of-type(2) {
    transform: rotate(-20deg) translateX(76px) rotate(20deg);
    transition-delay: 0.15s;
}

.box.open i:nth-of-type(3) {
    transform: rotate(45deg) translateX(105px) rotate(-45deg);
    transition-delay: 0.3s;
}

.box.open i:nth-of-type(4) {
    transform: rotate(90deg) translateX(105px) rotate(-90deg);
    transition-delay: 0.45s;
}
</style> 