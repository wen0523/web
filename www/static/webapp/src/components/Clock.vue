<template>
    <div id="clock" class="day">
        <p class="time">{{ time }}</p>
        <p class="date">{{ date }}</p>
    </div>
</template>
  
<script setup lang="ts">
import { ref, onMounted } from 'vue';

const date = ref('');
const time = ref('');

onMounted(() => {
    const my_card = document.getElementById('my_card')!;
    const my_clock = document.getElementById('clock')!;

    var week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
    var timerID = setInterval(updateTime, 1000);
    updateTime();//初始化时间
    updateCard();//初始化卡片

    function updateCard() {//卡片函数
        const rootElement = document.documentElement;
        //根据暗黑模式按钮改变卡片,也用于刷新界面时。
        if (rootElement.classList.contains('dark')) {
            my_card.classList.remove('day');
            my_card.classList.add('night');
            my_clock.classList.remove('day');
            my_clock.classList.add('night');
        }
    }

    function updateTime() {//时间函数

        var cd = new Date();
        var time_value =
            zeroPadding(cd.getHours(), 2) +
            ':' +
            zeroPadding(cd.getMinutes(), 2) +
            ':' +
            zeroPadding(cd.getSeconds(), 2);
        var date_value =
            zeroPadding(cd.getFullYear(), 4) +
            '-' +
            zeroPadding(cd.getMonth() + 1, 2) +
            '-' +
            zeroPadding(cd.getDate(), 2) +
            ' ' +
            week[cd.getDay()];
        time.value = time_value;
        date.value = date_value;
    }

    function zeroPadding(num: number, digit: number) {//规整时间
        var zero = '';
        for (var i = 0; i < digit; i++) {
            zero += '0';
        }
        return (zero + num).slice(-digit);
    }
});
</script>
  
<style scoped>
p {
    margin: 0;
    padding: 0;
}

#clock {
    /*basic*/
    text-align: center;
    text-shadow: 0 0 20px rgba(10, 175, 230, 1), 0 0 20px rgba(10, 175, 230, 0);

    .time {
        letter-spacing: 0.05em;
        font-size: 40px;
    }

    .date {
        letter-spacing: 0.1em;
        font-size: 24px;
        margin-bottom: 10px;
    }
}

#clock.day {
    /*day*/
    color: black;
}

#clock.night {
    /*night*/
    color: white;
}
</style>
  