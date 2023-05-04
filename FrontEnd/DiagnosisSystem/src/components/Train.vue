<template>
    <div style="margin-top: 60px;margin-left:80px;width: 600px" >
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="120px" >
            <el-form-item label="样本类别数量" prop="num_classes"
                          >
                <el-input v-model.number="ruleForm.num_classes"></el-input>
            </el-form-item>

            <el-form-item label="迭代次数" prop="epochs"
                          :rules="[
    { required: true, message: '迭代次数不能为空'},
  ]">
                <el-input v-model="ruleForm.epochs"></el-input>
            </el-form-item>

            <el-form-item label="每类样本数量" prop="number"
                          :rules="[
    { required: true, message: '地区不能为空'},
  ]">
                <el-input v-model="ruleForm.number"></el-input>
            </el-form-item>

            <el-form-item label="训练集比例" prop="train"
                          :rules="[
    { required: true, message: '联系方式不能为空'},
  ]">
                <el-input v-model="ruleForm.train"></el-input>
             </el-form-item>

            <el-form-item label="验证集比例" prop="valid"
                          :rules="[
    { required: true, message: '简介不能为空'},
  ]">
                <el-input v-model="ruleForm.valid"></el-input>
            </el-form-item>

            <el-form-item label="测试集比例" prop="test"
                          :rules="[
    { required: true, message: '是否选中不能为空'},
  ]">
                <el-input v-model="ruleForm.test"></el-input>
            </el-form-item>


            <el-form-item>
                <el-button type="primary" @click="submitForm('ruleForm')">确定</el-button>
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
        name: "Train",
        data() {
          var checkNum = (rule, value, callback) => {
        if (!value) {
          return callback(new Error('样本类别数量不能为空'));
        }
        setTimeout(() => {
          if (!Number.isInteger(value)) {
            callback(new Error('请输入数字值'));
          } else {
            if (value>11 || value<0) {
              callback(new Error('样本类别数量必须在1-10'));
            } else {
              callback();
            }
          }
        }, 1000);
      };
            return {
              fileList:[],
                ruleForm: {
                    num_classes: '',
                    epochs: '',
                    number: '',
                    train: '',
                    valid:'',
                    test:''
                },
              rules:{
                num_classes:[
                   { required: true, message: '样本类别数量不能为空'},
                  { validator: checkNum, trigger: 'blur' }
                ]
              }
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


        }

}

</script>

<style scoped>

</style>
