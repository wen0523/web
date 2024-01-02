<template>
    <div class="author_card">
        <div class="photo">
            <img src="/card2.png" alt="">
        </div>
        <h2>Wen-Blog</h2>
        <h6> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
            &nbsp; &nbsp;欢迎来到Wenの小窝</h6>
        <div class="social">
            <h2>Follow me</h2>
            <div class="social-links">
                <a href="https://github.com/wen0523/web" target="_blank"><i class="fa fa-github"></i></a>
                <a href="#"><i class="fa fa-envelope" aria-hidden="true"></i></a>
                <a href="#"><i class="fa fa-telegram" aria-hidden="true"></i></a>
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
.author_card {
    /*容器*/
    margin-top: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.photo {
    box-sizing: border-box;
}

.photo {
    width: 75px;
    height: 75px;
    border-radius: 50%;
    margin-bottom: 15px;
    overflow: hidden;
    border: 3.75px solid #fafafa;
    background-color: #fafafa;
    box-shadow: 0 0 0.5rem #babbbc;
}

.photo :hover {
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

@import 'https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css';

*,
div,
h2 {
    box-sizing: border-box;
}

// Demo Specific
// 
$blue: #3e82fb;

.social {
    background-color: #fafafa;
    margin-top: 20px;
    display: flex;
    align-items: center;
    position: relative;
    width: 200px;
    height: 46.7px;
    border-radius: 50px;
    overflow: hidden;
    transition: box-shadow .2s ease-out;

    // Flex Children
    div,
    h2 {
        margin: auto;
    }

    // Social Links
    //
    .social-links {
        display: flex;
        align-items: center;
        position: absolute;
        top: 0;
        left: 0;
        background: rgba($blue, 0);
        width: 100%;
        height: 100%;
        padding: 0 30px;
        transition: all .25s ease;

        // Links
        //
        a {
            margin: auto;
            background: #fff;
            color: $blue;
            width: 40px;
            height: 40px;
            border-radius: 20px;
            line-height: 40px;
            font-size: 18px;
            transform: translate3d(0, 60px, 0);
            transition: all .2s;

            &:hover {
                background: lighten($blue, 15%);
                color: #fff;
            }

            i {
                position: relative;
                left: 12px;
            }
        }
    }

    // Hover 
    &:hover {
        box-shadow: inset 0 0 0 2px #dbe3ea, 0 1rem 20px rgba($blue, .2);

        .social-links {
            background: rgba($blue, 1);

            // Sequential
            >a {
                animation: elastic .5s ease-out forwards 0s;

                &:nth-child(2) {
                    animation-delay: 0.05s;
                }

                &:nth-child(3) {
                    animation-delay: 0.1s;
                }

                &:nth-child(4) {
                    animation-delay: 0.15s;
                }

                &:nth-child(5) {
                    animation-delay: 0.2s;
                }
            }
        }
    }
}

@keyframes elastic {
    0% {
        transform: translate3d(0, 60px, 0);
    }

    40% {
        transform: translate3d(0, -5px, 0);
    }

    70% {
        transform: translate3d(0, 5px, 0);
    }

    100% {
        transform: translate3d(0, 0, 0);
    }
}

.dark .social {
    //dark
    background: rgb(0, 0, 0,0.5);
}
</style> 