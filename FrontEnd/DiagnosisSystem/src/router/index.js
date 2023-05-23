import Vue from 'vue'
import Router from 'vue-router'
import home from '../components/Home.vue'
import login from '../components/Login.vue'
import register from '../components/Register.vue'
import test from '../components/test.vue'
import existedData from "../components/ExistedData.vue";
import uploadData from "../components/UploadData.vue";
import train from "../components/Train.vue";
import result from "../components/Result.vue";
import compare from "../components/Compare.vue";
import help from  "../components/Help.vue"



Vue.use(Router)

export default new Router({
  routes: [
    {path:'/Home', name:'Home', component: home,
      children:[
        {path:'/existeddata',name:'已有数据集',component:existedData},
        {path:'/uploaddata',name:'上传数据集',component:uploadData},
        {path:'/train',name:'训练模型',component:train},
        {path:'/result',name:'结果查看',component:result},
        {path:'/compare',name:'模型比较',component:compare},
        {path:'/help',name:'帮助',component:help},
      ]
    },
    {path:'/login', name:'login', component:login},
    {path:'/register', name:'register', component:register},
    {path:'/test', name:'test', component:test},

  ]
})
