<template>
    <div style="margin-top: 60px;margin-left:80px;width: 600px" >
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="120px" class="demo-ruleForm">
            <el-form-item label="数据集id" prop="id"
                          :rules="[
    { required: true, message: '数据集id不能为空'},
  ]">
                <el-input v-model="ruleForm.id"></el-input>
            </el-form-item>

            <el-form-item label="数据集名称" prop="name"
                          :rules="[
    { required: true, message: '数据集名称不能为空'},
  ]">
                <el-input v-model="ruleForm.name"></el-input>
            </el-form-item>

            <el-form-item label="地区" prop="region"
                          :rules="[
    { required: true, message: '地区不能为空'},
  ]">
                <el-input v-model="ruleForm.region"></el-input>
            </el-form-item>

            <el-form-item label="联系方式" prop="contact"
                          :rules="[
    { required: true, message: '联系方式不能为空'},
  ]">
                <el-input v-model="ruleForm.contact"></el-input>
             </el-form-item>

            <el-form-item label="简介" prop="description"
                          :rules="[
    { required: true, message: '简介不能为空'},
  ]">
                <el-input v-model="ruleForm.description"></el-input>
            </el-form-item>

            <el-form-item label="是否选中" prop="ischoosed"
                          :rules="[
    { required: true, message: '是否选中不能为空'},
  ]">
                <el-input v-model="ruleForm.ischoosed"></el-input>
            </el-form-item>

            <el-form-item>
                <el-button type="primary" @click="submitForm('ruleForm')">添加</el-button>
                <el-button @click="resetForm('ruleForm')">重置</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
import axios from "axios";
const path = 'http://127.0.0.1:5001/uploadDataset';
    export default {
        name: "UploadData",
        data() {
            return {
                ruleForm: {
                    id: '',
                    name: '',
                    region: '',
                    contact: '',
                    description:'',
                    ischoosed:''
                },
                rules: {
                  id: [
                        { required: true, message: 'id不能为空', trigger: 'change' }
                    ],
                  name: [
                        { required: true, message: '数据集名称不能为空', trigger: 'change' },
                    ],

                },
            };
        },
        methods: {
            submitForm(formName) {
                let that= this
              console.log(that.ruleForm)
                axios.post(path,that.ruleForm).then(function (resp){
                  console.log(resp.data())
                if(resp.data)
                  that.alert('上传成功','',{
                    confirmButtonText:'确定',
                    callback:action=>{
                      that.$router.push('/existeddata')
                }
                  })
              })
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            }
        }
    }
</script>

<style scoped>

</style>
