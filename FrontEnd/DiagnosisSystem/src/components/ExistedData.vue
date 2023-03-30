<template>
  <div style="margin-top: 60px;margin-left:80px;border: 0px solid red;" >

    <el-table
      :data="tableData"
      border
      stripe
      style="width: 100%">
      <el-table-column
        prop="id"
        label="序号"
        width="100">
      </el-table-column>
      <el-table-column
        prop="name"
        label="数据集提供者"
        width="300">
      </el-table-column>
      <el-table-column
        prop="region"
        label="国家/地区"
        width="100">
      </el-table-column>
      <el-table-column
        prop="contact"
        label="联系方式"
        width="400">
      </el-table-column>
      <el-table-column
        prop="description"
        label="简介"
        width="490">
      </el-table-column>
      <el-table-column
        prop="ischoosed"
        label="是否选中"
        width="100">
      </el-table-column>
        <el-table-column
      fixed="right"
      label="操作"
      width="100">

          <el-button type="primary" @click="choose()">选中</el-button>

    </el-table-column>
    </el-table>
  </div>

</template>

<script>
import axios from "axios";
const path = 'http://127.0.0.1:5001/showDataset';
const updatepath = 'http://127.0.0.1:5001/updataDataset';

export default {
  name: "ExistedData",
  created() {
    const that = this
    axios.get(path).then(function (resp) {
      console.log(resp)
      console.log(resp.data)
      that.tableData = resp.data
    })
  },
  data(){
    return{
      status:'1',
      tableData:'' ,
    }
  },
  methods:{
    choose(){
      const that=this;
      console.log('当前status是：'+that.status)
      if(that.status=='1')
      {
        axios.post(updatepath,that.status).then(function (resp){
        console.log(resp.data)
      })
        that.status='0'
        // console.log('已更改为否')
         that.$alert('操作成功', '', {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        that.$router.push('/existeddata')
                                    }
                                })
      }
      else{
        axios.post(updatepath,that.status).then(function (resp){
        console.log(resp.data)
      })
        that.status='1'
        // console.log('已更改为是')
                 that.$alert('操作成功', '', {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        that.$router.push('/existeddata')
                                    }
                                })
      }
    }
  }

}
</script>

<style>

</style>
