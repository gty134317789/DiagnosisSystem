
<template>
  <div  class="login-container" >

    <el-form
      :model="inf"
      :rules="rules"
      status-icon
      label-position="left"
      class="demo-ruleForm login-page"
    >
      <h3 class="title">轴承故障诊断系统</h3>

      <el-form-item label="用户名" prop="username" label-width="80px"
       :rules="[
    { required: true, message: '用户名不能为空'},
  ]">
        <el-input
          type="text"
          v-model="inf.username"
          auto-complete="off"
          placeholder="用户名"
        ></el-input>
      </el-form-item>


      <el-form-item label="密码" prop="password" label-width="80px"
       :rules="[
    { required: true, message: '密码不能为空'},
  ]">
        <el-input
          type="password"
          v-model="inf.password"
          auto-complete="off"
          placeholder="密码"
        ></el-input>

      </el-form-item>
        <el-form-item label="确认密码" prop="password2" label-width="80px"
         :rules="[
    { required: true, message: '确认密码不能为空'},
  ]">
        <el-input
          type="password"
          v-model="inf.password2"
          auto-complete="off"
          placeholder="确认密码"
        ></el-input>
      </el-form-item>

      <el-form-item label="真实姓名" prop="truename" label-width="80px"
       :rules="[
    { required: true, message: '真实姓名不能为空'},
  ]">
        <el-input
          type="text"
          v-model="inf.truename"
          auto-complete="off"
          placeholder="真实姓名"
        ></el-input>
      </el-form-item>

      <el-form-item label="证件号" prop="idcardnum" label-width="80px"
       :rules="[
    { required: true, message: '证件号不能为空'},
  ]">
      <el-input
        type="text"
        v-model="inf.idcardnum"
        auto-complete="off"
        placeholder="证件号"
      ></el-input>
    </el-form-item>

      <el-form-item style="width: 100%">
        <el-button type="primary" plain style="width: 100%" @click="handleSubmit" :loading="logining">已有账号，去登录</el-button>
      </el-form-item>
      <el-form-item style="width: 100%">
        <el-button type="primary" plain style="width: 100%" @click="register" :loading="logining">注册</el-button>
      </el-form-item>
    </el-form>

  </div>
</template>

<script>
import axios from "axios";

const path = 'http://127.0.0.1:5000/register';
export default {
  data() {
    return {
      logining: false,
      inf:{
        username: '',
        password:'',
        password2:'',
        truename:'',
        idcardnum:''
      },
    rules: {
        username: [
          {required: true, message: '用户名不能为空',trigger: 'blur' }
        ],
        password: [
          {required: true, message: '密码不能为空',trigger: 'blur' }
        ],
        password2: [
          { required: true, message: '确认密码不能为空', trigger: 'blur'  }
        ],
        truename: [
          {required: true, message: '真实姓名不能为空',trigger: 'blur'  }
        ],
        idcardnum: [
          {required: true, message: '证件号不能为空',trigger: 'blur'  }
        ],
      }
    };
  },
  methods: {
    register(){
       var that = this;
       if(that.inf.password!=that.inf.password2)
       {
         that.$alert('两次密码不一致，请重新输入', '', {
          confirmButtonText: '确定',
           });
           console.log('密码不一致')
         stop()
       }
       else{
            // 对应 Python 提供的接口，这里的地址填写下面服务器运行的地址，本地则为127.0.0.1，外网则为 your_ip_address
            console.log("submit!")
            this.$alert('【'+this.inf.username+'】注册成功', '', {
                confirmButtonText: '确定',
            });
            if(axios.post(path,that.inf).then(function (resp) {
              console.log(resp);
            })
            ){
                console.log("响应成功")
                this.$router.push({path: '/login'});
            }
       }

    },
    handleSubmit(){
      this.$router.push({path: '/login'});
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
  margin: 250px 300px 300px 800px;
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

