<template>

  <div  class="login-container" >
    <el-form
      :model="inf"
      :rules="rules"
      status-icon
      label-position="left"
      label-width="0px"
      class="demo-ruleForm login-page"
    >
      <h3 class="title">轴承故障诊断系统</h3>
      <el-form-item prop="inf.username"
      :rules="[
        {required:true ,message:'用户名不能为空'},
      ]">
        <el-input
          type="text"
          v-model="inf.username"
          auto-complete="off"
          placeholder="用户名"
        ></el-input>
      </el-form-item>


      <el-form-item prop="inf.password"
      :rules="[
        {required:true,message:'密码不能为空'}
      ]">
        <el-input
          type="password"
          v-model="inf.password"
          auto-complete="off"
          placeholder="密码"
        ></el-input>
      </el-form-item>
      <el-form-item style="width: 100%">
        <el-button type="primary"  plain style="width: 100%" @click="handleSubmit" :loading="logining">登录</el-button>
      </el-form-item>
      <el-form-item style="width: 100%">
        <el-button type="primary"   plain style="width: 100%" @click="register" :loading="logining">注册</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from "axios";
const path = 'http://127.0.0.1:5000/login';
export default {
  data() {
    return {
      logining: false,
      inf:{
        username:'',
        password:'',
      },
      rules: {
        username: [
          {required: true, message: "用户名不能为空", trigger: "blur",},
        ],
        password: [
          { required: true, message: "密码不能为空", trigger: "blur" },
        ],
      },
    };
  },
  methods: {
    register(){
      this.$router.push({path: '/register'});
    },
    handleSubmit(){
        var that=this;
        axios.post(path,that.inf).then(function (resp){
          console.log(resp)
          if(resp.data=='登录成功')
          {
          that.$alert('【'+that.inf.username+'】登录成功', '', {
                confirmButtonText: '确定',
            });
          console.log("响应成功")
          that.$router.push({path:'/home'})
          }
          else{
           that.$alert('【'+that.inf.username+'】登录失败，用户名或密码不正确', '', {
                confirmButtonText: '确定',
            });
        }
        })


    }
  },
};
</script>

<style scoped>



.login-container {
  padding: 0px;
  background-size: 100%;
  height: 110%;
  width: 120%;
  position:fixed;
  margin-top: -60px;/*上边距*/
  margin-left: -20px;/*左边距*/
  background: url("../assets/img.png") no-repeat;
  background-size: cover;

}

.login-page {
  -webkit-border-radius: 5px;
  border-radius: 5px;
  margin: 300px 300px 300px 800px;
  width: 350px;
  padding: 35px 35px 15px;
  background: #fff;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 25px #cac6c6;
}
label.el-checkbox.rememberme {
  margin: 0px 0px 15px;
  text-align: left;
}

.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #3880e3;
}

.el-carousel__item:nth-child(2n+1) {
  background-color: #2179da;
}
</style>

