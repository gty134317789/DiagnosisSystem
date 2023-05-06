<template>
    <div style="margin-top: 60px;margin-left:80px;width: 600px" >
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="120px" >
            <el-form-item label="样本类别数量" prop="num_classes">
                <el-input v-model.number="ruleForm.num_classes"></el-input>
            </el-form-item>

            <el-form-item label="迭代次数" prop="epochs">
                <el-input v-model.number="ruleForm.epochs"></el-input>
            </el-form-item>

            <el-form-item label="每类样本数量" prop="number">
                <el-input v-model.number="ruleForm.number"></el-input>
            </el-form-item>

            <el-form-item label="训练集比例" prop="train">
                <el-input-number v-model.number="ruleForm.train" :precision="2" :step="0.01" :max="1" :min="0"></el-input-number>
            </el-form-item>

           <el-form-item label="验证集比例" prop="valid">
                <el-input-number v-model.number="ruleForm.valid" :precision="2" :step="0.01" :max="1" :min="0"></el-input-number>
           </el-form-item>

          <el-form-item label="测试集比例" prop="test">
                <el-input-number v-model.number="ruleForm.test" :precision="2" :step="0.01" :max="1" :min="0"></el-input-number>
          </el-form-item>

          <el-form-item>
           <el-button type="primary" @click="checkForm('ruleForm')">校验</el-button>
          </el-form-item>

          <el-form-item>
            <el-button type="primary" v-bind:disabled="ruleForm.check" @click="submitForm('ruleForm')">确定</el-button>
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
          //验证样本数量
          var checkNum = (rule, value, callback) => {
          if (!value) {
            return callback(new Error('样本类别数量不能为空'));
          }
          setTimeout(() => {
            if (!Number.isInteger(value)) {
              callback(new Error('请输入数字值'));
            } else {
              if (value>10 || value<0) {
                callback(new Error('样本类别数量必须在1-10'));
              } else {
                callback();
              }
            }
          }, 100);
        };

          //验证迭代次数
           var checkEpochs = (rule, value, callback) => {
          if (!value) {
            return callback(new Error('每类样本数量不能为空'));
          }
          setTimeout(() => {
            if (!Number.isInteger(value)) {
              callback(new Error('请输入数字值'));
            } else {
              if (value>200 || value<100) {
                callback(new Error('迭代次数需要在100-200次之间'));
              } else {
                callback();
              }
            }
          }, 100);
        };

           //验证每类样本数量
           var checkNumbers = (rule, value, callback) => {
          if (!value) {
            return callback(new Error('每类样本数量不能为空'));
          }
          setTimeout(() => {
            if (!Number.isInteger(value)) {
              callback(new Error('请输入数字值'));
            } else {
              if (value>784 || value<100) {
                callback(new Error('每类样本数量需要在100-784个之间'));
              } else {
                callback();
              }
            }
          }, 100);
        };


            return {
              fileList:[],
                ruleForm: {
                    num_classes: '',
                    epochs: '',
                    number: '',
                    train: '',
                    valid:'',
                    test:'',
                    check:true
                },
              rules:{
                num_classes:[
                   { required: true, message: '样本类别数量不能为空'},
                  { validator: checkNum, trigger: 'blur' }
                ],
                epochs:[
                  { required: true, message: '迭代次数不能为空'},
                  { validator: checkEpochs, trigger: 'blur' }
                ],
                number:[
                  { required: true, message: '每类样本数量不能为空'},
                  { validator: checkNumbers, trigger: 'blur' }
                ],
                train:[
                  { required: true, message: '训练集比例不能为空'},
                ],
                valid:[
                  { required: true, message: '验证集比例不能为空'},
                ],
                test:[
                  { required: true, message: '测试集比例不能为空'},
                ],

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
                const that=this;
                that.$refs[formName].resetFields();
            },
            checkForm(formName){
              const that=this;
              if(that.ruleForm.train+that.ruleForm.valid+that.ruleForm.test==1){
                that.$alert('数据无误可提交', '', {
                                    confirmButtonText: '确定',
                                    callback: action => {this.ruleForm.check=false}
                                });
              }
              else if(that.ruleForm.train+that.ruleForm.valid+that.ruleForm.test<1){
                 that.$alert('数据有误，训练集、验证集、测试集和小于1', '', {
                                    confirmButtonText: '确定',
                                    callback: action => {this.ruleForm.check=true}
                                });
              }
              else if(that.ruleForm.train+that.ruleForm.valid+that.ruleForm.test>1){
                 that.$alert('数据有误，训练集、验证集、测试集和大于1', '', {
                                    confirmButtonText: '确定',
                                    callback: action => {this.ruleForm.check=true}
                                });
              }
            }
  },


}

</script>

<style scoped>

</style>
