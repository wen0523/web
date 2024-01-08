//节流函数,减少监听频率（回调次数）。
const throttle = (func: Function, delay: number) => {
    let isThrottled = false;

    return function (this: any) {
        const context = this;
        const args = arguments;

        if (!isThrottled) {
            func.apply(context, args);
            isThrottled = true;
            setTimeout(() => {
                isThrottled = false;
            }, delay);
        }
    };
}

export default throttle;