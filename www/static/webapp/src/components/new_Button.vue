<template>
    <label class="night-day-toggle day">
        <input type="checkbox" />
        <div class="planet">
            <div class="moon">
                <div class="crater crater-1"></div>
                <div class="crater crater-2"></div>
                <div class="crater crater-3"></div>
                <div class="crater crater-4"></div>
                <div class="crater crater-5"></div>
            </div>
            <div class="sun"></div>
        </div>
        <div class="sky sky-night">
            <svg class="star star-1" width="12" height="12" viewBox="0 0 24 24">
                <path
                    d="M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.45,13.97L5.82,21L12,17.27Z">
                </path>
            </svg>
            <svg class="star star-2" width="10" height="10" viewBox="0 0 24 24">
                <path
                    d="M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.45,13.97L5.82,21L12,17.27Z">
                </path>
            </svg>
            <svg class="star star-3" width="8" height="8" viewBox="0 0 24 24">
                <path
                    d="M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.45,13.97L5.82,21L12,17.27Z">
                </path>
            </svg>
            <svg class="star star-4" width="6" height="6" viewBox="0 0 24 24">
                <path
                    d="M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.45,13.97L5.82,21L12,17.27Z">
                </path>
            </svg>
            <svg class="star star-5" width="4" height="4" viewBox="0 0 24 24">
                <path
                    d="M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.45,13.97L5.82,21L12,17.27Z">
                </path>
            </svg>
        </div>
        <div class="sky sky-day">
            <div class="cloud cloud-1">
                <div class="cloud-bubble cloud-bubble-1"></div>
                <div class="cloud-bubble cloud-bubble-2"></div>
                <div class="cloud-bubble cloud-bubble-3"></div>
                <div class="cloud-bubble cloud-bubble-4"></div>
                <div class="cloud-bubble cloud-bubble-5"></div>
            </div>
            <div class="cloud cloud-2">
                <div class="cloud-bubble cloud-bubble-1"></div>
                <div class="cloud-bubble cloud-bubble-2"></div>
                <div class="cloud-bubble cloud-bubble-3"></div>
                <div class="cloud-bubble cloud-bubble-4"></div>
                <div class="cloud-bubble cloud-bubble-5"></div>
            </div>
            <div class="cloud cloud-3">
                <div class="cloud-bubble cloud-bubble-1"></div>
                <div class="cloud-bubble cloud-bubble-2"></div>
                <div class="cloud-bubble cloud-bubble-3"></div>
                <div class="cloud-bubble cloud-bubble-4"></div>
                <div class="cloud-bubble cloud-bubble-5"></div>
            </div>
            <div class="cloud cloud-4">
                <div class="cloud-bubble cloud-bubble-1"></div>
                <div class="cloud-bubble cloud-bubble-2"></div>
                <div class="cloud-bubble cloud-bubble-3"></div>
                <div class="cloud-bubble cloud-bubble-4"></div>
                <div class="cloud-bubble cloud-bubble-5"></div>
            </div>
        </div>
    </label>
</template>

<script lang="ts" setup>
import { onMounted } from 'vue';

const States = {
    NIGHT: 0,
    DAY: 1
};

/**
 * Night Day Toggle Class
 */
class NightDayToggle {
    private _element: Element;
    private _input: HTMLInputElement;
    private _state: number;
    /**
     * Constructor
     */
    constructor(element: Element) {
        this._element = element;
        this._input = element.querySelector('input[type="checkbox"]')!;
        this._state = States.NIGHT;

        this._initialize();
        this._bindEventListeners();
    }

    /**
     * Initializes the toggle
     *
     * @return void
     */
    _initialize() {
        if (this._element.classList.contains('night')) {
            this._state = States.NIGHT;
        } else if (this._element.classList.contains('day')) {
            this._state = States.DAY;
        }

        this._setValue();
        this._setBackground();
    }

    /**
     * Binds the event listeners
     *
     * @return void
     */
    _bindEventListeners() {
        this._element.addEventListener('change', () => {
            this._toggle();
        });
    }

    /**
     * Toggles the night/day state
     *
     * @return void
     */
    _toggle() {
        if (this._state === States.NIGHT) {
            localStorage.setItem('new_button', 'day');//将信息保存到localStorage
            this._setDay();
        } else {
            localStorage.setItem('new_button', 'night');//将信息保存到localStorage
            this._setNight();
        }

        this._setValue();
        this._setBackground();
    }

    /**
     * Sets the state to night
     *
     * @return void
     */
    _setNight() {
        this._element.classList.remove('day');
        this._element.classList.add('night');
        this._state = States.NIGHT;
    }

    /**
     * Sets the state to day
     *
     * @return void
     */
    _setDay() {
        this._element.classList.remove('night');
        this._element.classList.add('day');
        this._state = States.DAY;
    }

    /**
     * Sets the value of the input
     *
     * @return void
     */
    _setValue() {
        this._input.value = String(this._state);
    }

    /**
     * Sets the background color to the current state
     */
    _setBackground() {
        let stateName;

        if (this._state === States.DAY) {
            stateName = 'day';
            const rootElement = document.documentElement;
            if (rootElement.classList.contains('dark')) {
                rootElement.classList.remove('dark');
            }
        } else {
            stateName = 'night';
            const rootElement = document.documentElement;
            rootElement.classList.add('dark');
        }

        document.body.style.setProperty('--background', `var(--background-${stateName})`);
    }
}

onMounted(() => {
    const element = document.querySelector('.night-day-toggle')!;

    //判断刷新，并设置状态（刷新之前的）
    if (window.name == "") {//此次为首次加载
        window.name = "reload"; // 给window.name设置一个固定值 
        localStorage.setItem('new_button', 'day');// 首次设置localStorage的值
        new NightDayToggle(element);
    } else if (window.name == "reload") {//此次为页面刷新
        const state = localStorage.getItem('new_button')!;
        if (element.classList.contains(state)) {//day
            new NightDayToggle(element);
        } else {//night
            element.classList.remove('day');
            element.classList.add('night');
            new NightDayToggle(element);
        }
    }

});
</script>

<style lang="scss">
$size: 2.3rem;
$size-multiplier: 2;
$padding: .5rem;
$background-night: #f5f5f5;
$background-day: #ffe7c0;
$toggle-background-night: #3c4360;
$toggle-background-day: #afdfeb;
$moon-color: #fff;
$moon-crater-color: #efefef;
$sun-color: #feeb97;
$sun-accent-color: #f4ce8c;
$clouds-color: #fff;
$stars-color: #fff;
$anim-dur: .3s;
$easing: ease;

* {
    box-sizing: border-box;

    &:before,
    &:after {
        box-sizing: border-box;
    }
}

.night-day-toggle {
    cursor: pointer;
    position: fixed;
    width: $size * $size-multiplier;
    height: $size;
    border-radius: $size;
    transition: background $anim-dur ease;
    top: 1em;
    right: 5em;

    .planet {
        position: absolute;
        width: $size - $padding * 2;
        height: $size - $padding * 2;
        top: $padding;
        left: $padding;
        border-radius: 50%;
        overflow: hidden;
        transition: all $anim-dur $easing;

        .moon,
        .sun {
            visibility: hidden;
            opacity: 0;
            transition: all $anim-dur $easing;
            width: 100%;
            height: 100%;
            position: absolute;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
        }

        .moon {
            background: $moon-color;
            z-index: 5;

            .crater {
                position: absolute;
                border-radius: 50%;
                background: $moon-crater-color;
            }

            .crater-1 {
                width: 48%;
                height: 48%;
                right: 0;
                top: 18%;
                transform: translateX(35%);
            }

            .crater-2 {
                width: 13%;
                height: 13%;
                top: 7%;
                left: 10%;
                background: darken($moon-crater-color, 10%);
            }

            .crater-3 {
                width: 25%;
                height: 25%;
                top: 26%;
                left: 22%;
            }

            .crater-4 {
                width: 22%;
                height: 22%;
                top: 70%;
                left: 8%;
            }

            .crater-5 {
                width: 15%;
                height: 15%;
                top: 70%;
                left: 58%;
            }
        }

        .sun {
            background: $sun-color;
            border-right: .25rem solid $sun-accent-color;
            border-radius: 50%;
        }
    }

    .sky {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        visibility: hidden;
        opacity: 0;
        transition: all $anim-dur $easing;
    }

    .sky-night {
        .star {
            position: absolute;
            transform: translateX(-100%);
            transition: transform $anim-dur $easing;

            path {
                fill: $stars-color;
            }
        }

        .star-1 {
            right: 11%;
            bottom: 21%;
            width: 8%;
            height: 16%;
        }

        .star-2 {
            left: 50%;
            top: 20%;
            width: 7%;
            height: 15%;
        }

        .star-3 {
            top: 19%;
            right: 16%;
            width: 5%;
            height: 14%;
        }

        .star-4 {
            right: 27%;
            top: 47%;
            width: 5%;
            height: 9%;
        }

        .star-5 {
            left: 55%;
            bottom: 26%;
            width: 4%;
            height: 12%;
        }
    }

    .sky-day {
        .cloud {
            position: absolute;
            transform: translateX(100%);
            transition: transform $anim-dur $easing;

            .cloud-bubble {
                background: $clouds-color;
                border-radius: 50%;
                position: absolute;

                &:after {
                    content: "";
                    display: block;
                    padding-bottom: 100%;
                }
            }
        }

        .cloud-1 {
            width: 20%;
            height: 30.5%;
            right: 38%;
            bottom: 22%;

            .cloud-bubble-1 {
                width: 44%;
                bottom: 8%;
            }

            .cloud-bubble-2 {
                width: 44%;
                bottom: 0;
                left: 30%;
            }

            .cloud-bubble-3 {
                width: 44%;
                right: 0;
                bottom: 10%;
            }

            .cloud-bubble-4 {
                width: 42%;
                right: 20%;
                top: 0;
            }

            .cloud-bubble-5 {
                width: 44%;
                left: 10%;
                top: 0;
            }
        }

        .cloud-2 {
            width: 11.5%;
            height: 18%;
            left: 12%;
            top: 22%;

            .cloud-bubble-1 {
                width: 44%;
                bottom: 10%;
            }

            .cloud-bubble-2 {
                width: 40%;
                bottom: 0;
                left: 32%;
            }

            .cloud-bubble-3 {
                width: 42%;
                right: 0;
                bottom: 18%;
            }

            .cloud-bubble-4 {
                width: 40%;
                right: 18%;
                top: 5%;
            }

            .cloud-bubble-5 {
                width: 44%;
                left: 12%;
                top: 0;
            }
        }

        .cloud-3 {
            width: 11.5%;
            height: 16%;
            left: 42%;
            top: 12%;

            .cloud-bubble-1 {
                width: 44%;
                left: 0;
                bottom: 16%;
            }

            .cloud-bubble-2 {
                width: 42%;
                bottom: 0;
                left: 30%;
            }

            .cloud-bubble-3 {
                width: 44%;
                right: 0;
                bottom: 14%;
            }

            .cloud-bubble-4 {
                width: 40%;
                top: 0;
                right: 14%;
            }

            .cloud-bubble-5 {
                width: 32%;
                left: 23%;
                top: 4%;
            }
        }

        .cloud-4 {
            left: 15%;
            bottom: 22%;
            width: 10%;
            height: 13%;

            .cloud-bubble-1 {
                width: 42%;
                left: 0;
                bottom: 17%;
            }

            .cloud-bubble-2 {
                width: 45%;
                bottom: 0;
                left: 25%;
            }

            .cloud-bubble-3 {
                width: 44%;
                bottom: 0;
                right: 0;
            }

            .cloud-bubble-4 {
                width: 40%;
                top: 0;
                right: 5%;
            }

            .cloud-bubble-5 {
                width: 36%;
                left: 28%;
                top: 5%;
            }
        }
    }

    input[type="checkbox"] {
        width: 0;
        height: 0;
        overflow: hidden;
        position: absolute;
    }

    &.night {
        background: $toggle-background-night;

        .planet {
            .moon {
                visibility: visible;
                opacity: 1;
            }
        }

        .sky-night {
            visibility: visible;
            opacity: 1;

            .star {
                transform: translateX(0);
            }
        }
    }

    &.day {
        background: $toggle-background-day;

        .planet {
            transform: translateX($size * $size-multiplier - $size);

            .sun {
                visibility: visible;
                opacity: 1;
            }
        }

        .sky-day {
            visibility: visible;
            opacity: 1;

            .cloud {
                transform: translateX(0);
            }
        }
    }
}
</style>