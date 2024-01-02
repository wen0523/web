<template>
  <div class="home">
    <div class="container">
      <div class="article div-base">aaaaaaaaaaa</div>
      <div class="article div-base">bbbbbbbbbbb</div>
    </div>
    <div class="container">
      <div class="article div-base">bbbbbbbbbbb</div>
      <div class="article div-base">bbbbbbbbbbb</div>
    </div>
    <div class="container">
      <div class="article div-base">bbbbbbbbbbb</div>
      <div class="article"></div>
    </div>
    
  </div>
</template>
 
<style scoped>
.home {
  display: flex;
  flex-direction: column;
}

.container{
  display: flex;
  flex-direction: row;
}
.article {
  flex: 1;
  margin: 20px;
  height: 320px;
}
</style>