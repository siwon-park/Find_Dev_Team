<template>
  <footer>
    <div class="bar">
      <div style="text-align:center;  margin-top:20px; color:grey">
        <div style="padding-top: 5px; padding-bottom: 2px;">WMT(Where is My Team)</div>
        <div style="padding-bottom: 2px;">2022.07.01</div>
        <div class="name" style="width:12.5%; font-size: 15px;">SiWon Park | HyeonJeong Lee</div>
        <div style="padding-top: 2px; padding-bottom: 10px;">© 2022 All Rights Reserved.</div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'FootBar',
  data() {
    return {
    }
  }

}
</script>

<style scoped>

.bar{
  background-color: aliceblue;
  font-size: 13px;
}

.name{
  color: rgb(26, 26, 26);
  display: inline-block;

}


</style>