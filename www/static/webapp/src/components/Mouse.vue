
<script lang="ts" setup>
import { onMounted } from 'vue';

//重写lerp
interface Math {
    lerp(start: number, end: number, t: number): number;
}
declare var Math: Math;

Math.lerp = (s: number, t: number, e: number) => (1 - e) * s + e * t;

class Cursor {
    pos: {
        curr: { x: number; y: number } | null;
        prev: { x: number; y: number } | null;
    };
    pt: string[];
    cursor: HTMLDivElement;
    scr: HTMLStyleElement;

    constructor() {
        this.cursor = document.getElementById("cursor") as HTMLDivElement;
        this.scr = document.getElementById("src") as HTMLStyleElement;
        this.pos = {
            curr: null,
            prev: null,
        };
        this.pt = [];
        this.create();
        this.init();
        this.render();
    }

    move(s: number, t: number) {
        this.cursor.style.left = `${s}px`;
        this.cursor.style.top = `${t}px`;
    }

    create() {
        if (!document.getElementById("cursor")) {
            this.cursor = document.createElement("div");
            this.cursor.id = "cursor";
            document.body.append(this.cursor);
        }
        var s = document.getElementsByTagName("*")
        for (let t = 0; t < s.length; t++)
            if (this.add(s[t]))
                this.pt.push(s[t].outerHTML);
    }

    add(tag: Element) {
        if (tag.tagName.toLowerCase() === "h1" || tag.tagName.toLowerCase() === "div" || tag.tagName.toLowerCase() === "html" || tag.tagName.toLowerCase() === "body" || tag.tagName.toLowerCase() === "head" || tag.tagName.toLowerCase() === "h2" || tag.tagName.toLowerCase() === "h6" || tag.tagName.toLowerCase() === "img" || tag.tagName.toLowerCase() === "el-container" || tag.tagName.toLowerCase() === "el-header" || tag.tagName.toLowerCase() === "el-asider" || tag.tagName.toLowerCase() === "el-main")  
            return false;
        else
            return true;
    }
    init() {
        document.onmouseover = (event: MouseEvent) => {
            if (event.target instanceof Element) {
                const outerHTML = event.target.outerHTML;
                if (outerHTML && this.pt.includes(outerHTML)) {
                    this.cursor.classList.add("hover");
                }
            }
        };

        document.onmouseout = (event: MouseEvent) => {
            if (event.target instanceof Element) {
                const outerHTML = event.target.outerHTML;
                if (outerHTML && this.pt.includes(outerHTML)) {
                    this.cursor.classList.remove("hover");
                }
            }
        };

        document.onmousemove = (event: MouseEvent) => {
            if (this.pos.curr === null) {
                this.move(event.clientX - 8, event.clientY - 8);
            }
            this.pos.curr = {
                x: event.clientX - 8,
                y: event.clientY - 8,
            };
            this.cursor.classList.remove("hidden");
        };

        document.onmouseenter = () => this.cursor.classList.remove("hidden");
        document.onmouseleave = () => this.cursor.classList.add("hidden");
        document.onmousedown = () => this.cursor.classList.add("active");
        document.onmouseup = () => this.cursor.classList.remove("active");
    }

    render() {
        if (this.pos.prev && this.pos.curr) {
            this.pos.prev.x = Math.lerp(this.pos.prev.x, this.pos.curr.x, 0.15);
            this.pos.prev.y = Math.lerp(this.pos.prev.y, this.pos.curr.y, 0.15);
            this.move(this.pos.prev.x, this.pos.prev.y);
        } else {
            this.pos.prev = this.pos.curr;
        }
        requestAnimationFrame(() => this.render());
    }
}
//在切换到别的url时只有reflash才能重新渲染（新增的组件），日后还要改进
window.onload = () => {
    new Cursor();
}

</script> 
<style id="src">
#cursor {
    position: fixed;
    width: 16px;
    height: 16px;
    background-color: #ffff00;
    border-radius: 8px;
    opacity: .25;
    z-index: 10086;
    pointer-events: none;
    transition: .2s ease-in-out;
    transition-property: background-color, opacity, transform
}

#cursor.hidden {
    opacity: 0
}

#cursor.hover {
    opacity: .1;
    transform: scale(2.5)
}

#cursor.active {
    opacity: .5;
    transform: scale(.5)
}

/*鼠标全局样式*/
:root :hover {
    cursor: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8' width='8px' height='8px'><circle cx='4' cy='4' r='4' opacity='.5'/></svg>") 4 4, auto
}
</style>