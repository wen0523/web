//控制菜单栏的显示与隐藏
import { onMounted } from "vue";
import throttle from "./throttle";//节流

var lastScrollTop = 0;

const Header_show_hide = () => {
    onMounted(() => {
        const Header = document.getElementById("header")!;
        const Root = document.documentElement;

        //监测滚轮滑动
        window.addEventListener("scroll", throttle(function () {
            var st = document.documentElement.scrollTop;

            if(Header.classList.contains('top')){//使背景不透明
                Header.classList.remove('top')
            }

            if (st > lastScrollTop) {
                Header.style.opacity = "0";
                Header.style.transition = "0.5s";
            } else {
                Header.style.opacity = "1";
                Header.style.transition = "0.5s";
            }
            lastScrollTop = st; //储存起来以便后面使用
        }, 100));

        // 监测是否在顶部
        function checkIfAtTop() {
            //当在顶部且为不透明时才设置
            if (document.documentElement.scrollTop <= 5&&!Header.classList.contains('top')) {
                Header.classList.add('top');//透明
                Header.style.transition = "0.5s";
            } 
        }

        // 使用setInterval函数限制 checkIfAtTop 函数的执行频率
        setInterval(checkIfAtTop, 300)
    });
}

export default Header_show_hide;