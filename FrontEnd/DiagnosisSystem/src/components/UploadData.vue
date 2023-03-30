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
               <el-upload
              :limit="1"
              :file-list="fileList"
              :auto-upload="true"
              action="http://127.0.0.1:5001/uploadDatafile"
              :before-upload="makedir"
              :data="uploadData"
        >
          <el-button size="small" type="primary">点击上传</el-button>
          <div slot="tip" class="el-upload__tip">只能上传mat文件，且不超过500M</div>
        </el-upload>
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
const pathfile = 'http://127.0.0.1:5001/uploadDatafile';
const makdir='http://127.0.0.1:5001/makeDatadir';


    export default {
        name: "UploadData",
        data() {
            return {
              fileList:[],
              uploadData:{'name':''},
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
            submitForm() {
              const that=this
              console.log(that.ruleForm)
                axios.post(path,that.ruleForm).then(function (resp){
                  console.log(resp.data)
                  if(resp.data){
                  that.$alert('操作成功', '', {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        that.$router.push('/existeddata')
                                    }
                                });}
              })

            },
            resetForm(formName) {
                const that=this
                that.$refs[formName].resetFields();
            },
            uploadFile(response,file){
              const that=this;

              name=that.ruleForm.name
              console.log('输出名字')
              console.log(name)
              console.log('response是',response)
          },
            makedir(){
              const that=this
              console.log('已调用')
              that.uploadData.name=that.ruleForm.name
              axios.post(makdir,that.uploadData).then(function (resp){
                console.log('成功')
                console.log(that.ruleForm.name)
                console.log(resp.data)
              })
          },
        }
    }
</script>

<style scoped>

</style>
