<template>
    <div>

        <el-dialog :title="'报告详情如下：'+now_report_id" style="background-color: #d4f7fa" :visible.sync="dialogFormVisible3" width="90%">
                    <el-collapse v-for="i in apis_result">
                          <el-collapse-item title="一致性 Consistency" name="1">
                              <template slot="title">
                                  <strong :style="{color:getColor(i.result)}">{{ i.label }}</strong>
                              </template>
                              <span style="color:grey">【接口结果】</span><strong> {{i.result}} </strong> <br>
                              <span style="color:grey">【HttpStatus】</span><strong> {{i.status_code}} </strong> <br>
                              <span style="color:grey">【请求类型】</span><strong> {{i.method}} </strong> <br>
                              <span style="color:grey">【请求url】</span><strong> {{i.url}} </strong> <br>
                              <span style="color:grey">【请求头】</span><strong> {{i.request_headers}} </strong> <br>
                              <span style="color:grey">【请求体类型】</span><strong> {{i.payload_method}} </strong> <br>
                              <span style="color:grey">【配置执行结果】</span><strong> {{i.CR}} </strong> <br>
                              <span style="color:grey">【变量提取结果】</span><strong> {{i.TQ}} </strong> <br>
                              <span style="color:grey">【请求体raw类型】</span><strong> {{i.payload_raw_method}} </strong> <br>
                              <span style="color:grey">【请求体】</span><strong> {{i.payload}} </strong> <br>
                              <span style="color:grey">【返回体】</span><strong> {{i.R}} </strong> <br>
                              <span style="color:grey">【返回头】</span><strong> {{i.response_headers}} </strong> <br>


                          </el-collapse-item>
                    </el-collapse>

                </el-dialog>
        <el-button style="float: right" type="danger" @click="clear_all_reports">清空报告</el-button>
        <el-table :data="all_reports" stripe style="max-width: 100%;max-height: 500px;overflow-y: auto">
                    <el-table-column label="报告id" width="100">
                        <template slot-scope="scope">
                            <span>{{ scope.row.id}}</span>
                        </template>
                    </el-table-column>

                    <el-table-column label="生成时间" width="200">
                        <template slot-scope="scope">
                            <span>{{ scope.row.ctime}}</span>
                        </template>
                    </el-table-column>

                    <el-table-column label="总结果" width="100">
                        <template slot-scope="scope">
                            <span :style="{color:getColor(scope.row.all_result) }">{{ scope.row.all_result}}</span>
                        </template>
                    </el-table-column>

                    <el-table-column >
                        <template slot-scope="scope">
                            <el-button type="primary" size="mini" @click="look_report_detail(scope.$index)">查看详情</el-button>
                        </template>
                    </el-table-column>
                </el-table>

    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "Report",
        data(){
            return{
                apis_result:[],
                dialogFormVisible3:false,
                all_reports : [],
                now_report_id:'',
            }
        },
        mounted() {

             axios.get('/get_all_reports/',{
                    params:{
                        project_id:this.project_id
                    }
                }).then(res=>{
                    this.all_reports = res.data
                })
                console.log(this.all_reports)

        },
        methods:{

             clear_all_reports(){
                axios.get('/clear_all_reports/',{
                    params:{
                        project_id:this.project_id
                    }
                }).then(res=>{
                    this.all_reports = []
                })
            },
             look_report_detail(index){
                this.apis_result = [];
                this.dialogFormVisible3 = true;
                this.apis_result = this.all_reports[index].apis_result;
                this.now_report_id = this.all_reports[index].id
                console.log(this.apis_result)
            },
             getColor(result){
                if( result.toString() == 'true'){
                    return 'green'
                }else{
                    return 'red'
                }
            },

        },
        props:['project_id',]
    }
</script>

<style scoped>

</style>