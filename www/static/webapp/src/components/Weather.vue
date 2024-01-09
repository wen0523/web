<template>
  <div id="he-plugin-simple"></div>
</template>
<script lang="ts">
export default {
  mounted() {
    const weather = document.getElementById("he-plugin-simple")!;

    // Your script content goes here
    const script1 = document.createElement('script');
    script1.innerHTML = `
        WIDGET = {
          "CONFIG": {
            "modules": "01234",
            "background": "1",
            "tmpColor": "FFFFFF",
            "tmpSize": "18",
            "cityColor": "FFFFFF",
            "citySize": "18",
            "aqiColor": "FFFFFF",
            "aqiSize": "18",
            "weatherIconSize": "24",
            "alertIconSize": "18",
            "padding": "6.5px 10px 6.5px 10px",
            "shadow": "0",
            "language": "auto",
            "borderRadius": "20",
            "fixed": "true",
            "vertical": "top",
            "horizontal": "left",
            "key": "32156f85f7284b238a2d4e4b6abf8ed1"
          }
        }
      `;
    weather.appendChild(script1);

    const script2 = document.createElement('script');
    script2.src = "https://widget.qweather.net/simple/static/js/he-simple-common.js?v=2.0";
    weather.appendChild(script2);
  }
};
</script>

<style>
#he-plugin-simple {
  width: 17em;
  top: 1.5em;
  right: 19em;
}

#weather-view-he{/*弹出框*/
  height: 290px !important;
}
</style>