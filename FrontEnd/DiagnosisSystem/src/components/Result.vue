<template>

  <el-row>
    <el-col :span="12">

    <div style="margin-top: 60px;margin-left:80px;width: 600px" >
       <el-container >
      <el-header>
<!--        <el-input placeholder="请输入本地txt文件路径" v-model="file_path"></el-input>-->
<!--        <el-button type="primary" @click="getFileContent">读取文件</el-button>-->
        <el-radio-group v-model="model">
                  <el-radio-button label="CNN"></el-radio-button>
                  <el-radio-button label="INCEPTION"></el-radio-button>
        </el-radio-group>
        <el-button type="primary" @click="getFileContent">查看结果</el-button>

      </el-header>
      <el-main>
        <el-scrollbar style="height: 100%;">
          <pre>{{ fileContent }}</pre>
        </el-scrollbar>
      </el-main>

    </el-container>
    </div>
    </el-col>
    <el-col :span="12">
      <el-button type="primary" @click="showImages">展示图片</el-button>
           <el-image
            v-for="(image, index) in images"
            :key="index"
            :src="image"
            :fit="fit"
            :preview-src-list="images"
            style="margin-bottom: 20px;"
          ></el-image>
    </el-col>
  </el-row>

</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      fileContent: '',
      model:'',
      images:[],
      fit: 'cover'
    }
  },
  methods: {
    async getFileContent() {
      try {
        const response = await axios.post('http://localhost:5001/result', {
          model:this.model,
        })
        if (response.data.status === 'success') {
          this.fileContent = response.data.content
        } else {
          this.$message.error(response.data.error)
        }
      } catch (error) {
        this.$message.error('请求失败，请检查网络连接')
      }
    },
    showImages(){
       try {
         var image1='';
        var image2='';
        var image3='';
        var image4='';
        console.log('点击')
         if(this.model=='CNN'){
           // 使用require方法加载图片
           image1 = require('@/assets/CNN_sample.png');
           image2 = require('@/assets/CNN_result.png');
           image3 = require('@/assets/CNN_accuracy.png');
           image4 = require('@/assets/CNN_loss.png');
         }
        else{
          image1 = require('@/assets/INCEPTION_sample.png');
          image2 = require('@/assets/INCEPTION_result.png');
          image3 = require('@/assets/INCEPTION_accuracy.png');
          image4 = require('@/assets/INCEPTION_loss.png');
         }
        console.log(image1)

        // 将图片路径添加到images数组中
        this.images.push(image1);
        this.images.push(image2);
        this.images.push(image3);
        this.images.push(image4);
        console.log(this.images)
           } catch (error) {
        this.$message.error('请求失败，请检查网络连接')
         console.log(error)
      }
    }
  },
}
</script>

<style scoped>

</style>
