<template>
<div>
  <h1>问题反馈</h1>
  <pre>{{ fileContent }}</pre>
</div>

</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      fileContent: 'QQ:123456789 ' +
        '手机号:1234567890',
    }
  },
  methods: {

  },
}
</script>

<style scoped>

</style>
