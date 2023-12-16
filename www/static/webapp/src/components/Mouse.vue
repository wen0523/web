
<script lang="ts" setup>
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
        this.cursor = document.createElement("div");
        this.cursor.id = "cursor";
        this.cursor.classList.add("hidden");
        document.body.append(this.cursor);

        const elements = document.getElementsByTagName("*");
        for (let i = 0; i < elements.length; i++) {
            if (getStyle(elements[i], "cursor") === "pointer") {
                this.pt.push(elements[i].outerHTML);
            }
        }

        this.scr = document.createElement("style");
        document.body.appendChild(this.scr);
        this.scr.innerHTML =
            "* {cursor: url(\"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8' width='8px' height='8px'><circle cx='4' cy='4' r='4' opacity='.5'/></svg>\") 4 4, auto}";
    }

    refresh() {
        this.scr.remove();
        this.cursor.classList.remove("hover");
        this.cursor.classList.remove("active");
        this.pos = {
            curr: null,
            prev: null,
        };
        this.pt = [];
        this.create();
        this.init();
        this.render();
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

const CURSOR = new Cursor();

function getStyle(element: Element, style: string): string {
    try {
        return window.getComputedStyle ? window.getComputedStyle(element)[Number(style)] : (element as any).currentStyle[style];
    } catch (e) { }
    return "";
}


</script>
<style id="src">
#cursor {
    position: fixed;
    width: 16px;
    height: 16px;
    background-color: #00ff04;
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
:root :hover{
    cursor: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8' width='8px' height='8px'><circle cx='4' cy='4' r='4' opacity='.5'/></svg>") 4 4, auto
}
</style>