<template>
    <div style="margin-top: 60px;margin-left:80px;width: 600px" >
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="120px" class="demo-ruleForm">
            <el-form-item label="数据集id" prop="id"
                          :rules="[
    { required: true, message: '数据集id'},
  ]">
                <el-input v-model="ruleForm.companyCode"></el-input>
            </el-form-item>

            <el-form-item label="数据集名称" prop="name"
                          :rules="[
    { required: true, message: '数据集名称不能为空'},
  ]">
                <el-input v-model="ruleForm.companyManager"></el-input>
            </el-form-item>

            <el-form-item label="地区" prop="region"
                          :rules="[
    { required: true, message: '地区不能为空'},
  ]">
                <el-input v-model="ruleForm.companyAddress"></el-input>
            </el-form-item>

            <el-form-item label="联系方式" prop="contact"
                          :rules="[
    { required: true, message: '联系方式不能为空'},
  ]">
                <el-input v-model="ruleForm.companyIndustry"></el-input>
             </el-form-item>

            <el-form-item label="简介" prop="description"
                          :rules="[
    { required: true, message: '简介不能为空'},
  ]">
                <el-input v-model="ruleForm.companyPhone"></el-input>
            </el-form-item>

            <el-form-item label="是否选中" prop="ischoosed"
                          :rules="[
    { required: true, message: '是否选中达标不能为空'},
  ]">
                <el-input v-model="ruleForm.isUpToStandard"></el-input>
            </el-form-item>

            <el-form-item>
                <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
                <el-button @click="resetForm('ruleForm')">重置</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
const axios = require('axios');
    export default {
        name: "Addcompany",
        data() {
            return {
                ruleForm: {
                  companyCode: '',
                    companyManager: '',
                    companyAddress: '',
                    companyIndustry: '',
                    companyPhone:'',
                    isUpToStandard:''
                },
                rules: {
                  companyCode: [
                        { required: true, message: '公司代码不能为空', trigger: 'change' }
                    ],
                  companyManager: [
                        { required: true, message: '公司管理员不能为空', trigger: 'change' },
                        { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
                    ],

                },
            };
        },
        methods: {
            submitForm(formName) {
                let _this = this
              // _this.$alert('企业已存在，请重新添加', '', {
              //   confirmButtonText: '确定',
              //   callback: action => {
              //     _this.$router.push('/productmanager')
              //   }
              // });
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        axios.post('http://42.192.207.238:8181/company/save',_this.ruleForm).then(function (resp) {
                          console.log(resp.data)
                            if(resp.data){
                                _this.$alert('【'+_this.ruleForm.companyCode+'】添加成功', '', {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        _this.$router.push('/companymanager')
                                    }
                                });
                            }
                        })
                    }
                });
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            }
        }
    }
</script>

<style scoped>

</style>
