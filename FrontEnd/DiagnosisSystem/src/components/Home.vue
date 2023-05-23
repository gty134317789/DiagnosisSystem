<template>
  <el-container class="home_container">
    <el-header>
      <div class="home_title">轴承故障诊断系统</div>
    </el-header>
    <el-container>

      <el-aside width="210px" style="background-color: #a5e7f0">

        <el-menu router>

          <el-submenu :index=String(0)>
            <template slot="title"><i class="el-icon-s-home"></i>数据集管理</template>

            <el-menu-item index="/existeddata">
              <div style="position: relative;left: 20px;">
                <i class="el-icon-s-data"></i>选择数据集
              </div>
            </el-menu-item>

            <el-menu-item index="/UploadData">
              <div style="position: relative;left: 20px;">
                <i class="el-icon-upload"></i>上传数据集
              </div>
            </el-menu-item>
          </el-submenu>


          <el-menu-item index="/train">
            <i class="el-icon-cpu"></i>
            <span slot="title">训练模型</span>
          </el-menu-item>

          <el-menu-item index="/result">
            <i class="el-icon-cpu"></i>
            <span slot="title">查看结果</span>
          </el-menu-item>

             <el-menu-item index="/compare">
        <i class="el-icon-document"></i>
        <span slot="title">不同模型比较</span>
      </el-menu-item>

          <el-menu-item index="/help">
            <div style="position: relative;left: 20px;">
              <i class="el-icon-question"></i>帮助
            </div>
          </el-menu-item>

            <el-menu-item index="/login">
              <div style="position: relative;left: 20px;">
                <i class="el-icon-switch-button"></i>退出登录
              </div>
            </el-menu-item>

        </el-menu>


      </el-aside>

      <el-container>
        <el-main>
          <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item v-text="this.$router.currentRoute.name"></el-breadcrumb-item>
            <el-image :src="require('@/assets/HomeHelp.png')" :fit="fit" :preview-src-list="images" style="margin-bottom: 20px; "></el-image>
            <h1>系统使用流程</h1>
          </el-breadcrumb>
          <router-view></router-view>
        </el-main>
        <el-footer>P.E.E.K.A</el-footer>
      </el-container>

    </el-container>

  </el-container>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'


export default {
  name: 'Home',
  components: {
    HelloWorld

  }
}
</script>

<style>
.home_container {
  height: 100%;
  position: absolute;
  top: 0px;
  left: 0px;
  width: 100%;
}

.el-header {
  background-color: #095db9;
  color: #333;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.el-aside {
  background-color: #ECECEC;
}

.el-main {
  background-color: #fff;
  color: #000;
  text-align: center;
}

.el-footer {
  background-color: #ff6e20;
  color: #fff;
  font-size: 22px;
  line-height: 60px;
  text-align: center;
}

.home_title {
  color: #fff;
  font-size: 22px;
  display: inline;
}

.home_userinfo {
  color: #fff;
  cursor: pointer;
}

.home_userinfoContainer {
  display: inline;
  margin-right: 20px;
}
</style>
