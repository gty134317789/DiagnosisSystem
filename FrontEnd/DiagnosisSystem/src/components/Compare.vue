<template>
<el-container style="height: 100vh;">
    <!-- 上部分 -->
    <el-header  class="grid-content"  >
      <h1>使用的模型数据集，样本类别为10，样本长度为784，每类样本数量为300并且标准化，迭代次数为100此，训练集、验证集、测试集划分比例为8：1：1</h1>
    </el-header>

    <!-- 下部分 -->
    <el-main>
      <el-row>
        <el-image :src="require('@/assets/compare/data.png')" :fit="fit" :preview-src-list="images" style="margin-bottom: 20px; width: 800px; height: 800px;"></el-image>
<!--         style="width: 200px; height: 200px;"-->
      </el-row>

      <el-row>
        <!-- 田字格布局 -->
        <el-col :span="12"  >
          <div class="grid-content bg-purple" >
            <h1>CNN一维卷积神经网络</h1>
          </div>
            <el-image :src="require('@/assets/compare/CNN_result.png')" :fit="fit" :preview-src-list="images" style="margin-bottom: 20px; width: 384px; height: 384px;"></el-image>
             <el-image :src="require('@/assets/compare/CNN_loss.png')" :fit="fit" :preview-src-list="images" style="margin-bottom: 20px; width: 384px; height: 288px;"></el-image>
            <el-image :src="require('@/assets/compare/CNN_accuracy.png')" :fit="fit" :preview-src-list="images" style="margin-bottom: 20px; width: 384px; height: 288px;"></el-image>
            <el-image :src="require('@/assets/compare/CNN_confusion.png')" :fit="fit" :preview-src-list="images" style="margin-bottom: 20px; width: 384px; height: 288px;"></el-image>
        </el-col>
        <el-col :span="12">
          <div class="grid-content bg-purple" >
            <h1>Inception深度循环神经网络</h1>
          </div>
            <el-image :src="require('@/assets/compare/Inception_result.png')" :fit="fit" :preview-src-list="images" style="margin-bottom: 20px; width: 384px; height: 384px;"></el-image>
             <el-image :src="require('@/assets/compare/Inception_loss.png')" :fit="fit" :preview-src-list="images" style="margin-bottom: 20px; width: 384px; height: 288px;"></el-image>
            <el-image :src="require('@/assets/compare/Inception_accuracy.png')" :fit="fit" :preview-src-list="images" style="margin-bottom: 20px; width: 384px; height: 288px;"></el-image>
            <el-image :src="require('@/assets/compare/Inception_confusion.png')" :fit="fit" :preview-src-list="images" style="margin-bottom: 20px; width: 384px; height: 288px;"></el-image>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="12">
          <div class="grid-content bg-purple" >
            <h1>LSTM长短期记忆人工神经网络</h1>
          </div>
            <el-image :src="require('@/assets/compare/LSTM_result.png')" :fit="fit" :preview-src-list="images" style="margin-bottom: 20px; width: 384px; height: 384px;"></el-image>
            <el-image :src="require('@/assets/compare/LSTM_loss.png')" :fit="fit" :preview-src-list="images" style="margin-bottom: 20px; width: 384px; height: 288px;"></el-image>
            <el-image :src="require('@/assets/compare/LSTM_accuracy.png')" :fit="fit" :preview-src-list="images" style="margin-bottom: 20px; width: 384px; height: 288px;"></el-image>
            <el-image :src="require('@/assets/compare/LSTM_confusion.png')" :fit="fit" :preview-src-list="images" style="margin-bottom: 20px; width: 384px; height: 288px;"></el-image>
        </el-col>
        <el-col :span="12">
          <div class="grid-content bg-purple" >
            <h1>GRU深度循环神经网络</h1>
          </div>
            <el-image :src="require('@/assets/compare/GRU_result.png')" :fit="fit" :preview-src-list="images" style="margin-bottom: 20px; width: 384px; height: 384px;"></el-image>
             <el-image :src="require('@/assets/compare/GRU_loss.png')" :fit="fit" :preview-src-list="images" style="margin-bottom: 20px; width: 384px; height: 288px;"></el-image>
            <el-image :src="require('@/assets/compare/GRU_accuracy.png')" :fit="fit" :preview-src-list="images" style="margin-bottom: 20px; width: 384px; height: 288px;"></el-image>
            <el-image :src="require('@/assets/compare/GRU_confusion.png')" :fit="fit" :preview-src-list="images" style="margin-bottom: 20px; width: 384px; height: 288px;"></el-image>
        </el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<script>
import axios from 'axios'

export default {
    data() {
    return {
      fileContent: '',
      model:'',
      images:['@/assets/compare/data.png',],
      fit: 'cover',
      data:[],
    }
  },
}
</script>

<style scoped>
.grid-content {
  border-radius: 4px;
  min-height: 36px;
  text-align: center;
  padding: 20px 0;
  background-color: #9c27b0;
  color: #fff;
  margin: 10px;
}
</style>
