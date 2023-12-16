/// <reference types="vite/client" />
// shims-vue.d.ts
declare module '*.vue' {
    import { DefineComponent } from 'vue';
    const component: DefineComponent;
    export default component;
  }
  
// vue-live2d.d.ts

declare module 'vue-live2d';
