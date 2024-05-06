$(function () {
    echart_1();
    echart_2();
    echart_3();
    echart_4();

    function echart_1() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('chart_1'));
        var metrodates = server.categorys;
        var figures = server.positive;
        var result = metrodates.map((name,i) => ({name, value: figures[i]}));
        option = {
            title: {
                text: '今日积极情感占比统计',
                top: 8,
                left: 20,
                textStyle: {
                    fontSize: 18,
                    color: '#fff'
                }
            },
    toolbox: {
        show: true,
        feature: {
            dataView: {show: true, readOnly: false},
            // magicType: {show: true, type: ['line', 'bar']},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)",

            },
            legend: {
                orient: 'vertical',
                left: 'left',
                right: 20,
                top: 35,
                data: [1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12],
                textStyle: {
                    color: '#fff'
                }
            },
            series: [{
                name: '设备状态',
                type: 'pie',
                radius: ['0', '60%'],
                center: ['50%', '60%'],
                color: ['#cd8586', '#557b03', '#008af5','#0a82c7', '#0063ff', '#e1e9ea','#e72325', '#98e002', '#2ca3fd','#b4dbf3', '#cafa68', '#628db1'],
                label: {
                    normal: {
                        formatter: '{b}\n{d}%'
                    },

                },
                data: result
                //     [
                //     {
                //         value: 8,
                //         name: 'category1'
                //     },
                //     {
                //         value: 10,
                //         name: 'category2',
                //     },{
                //         value: 6,
                //         name: 'category3'
                //     },
                //     {
                //         value: 50,
                //         name: 'category4',
                //     },{
                //         value: 12,
                //         name: 'category5'
                //     },
                //     {
                //         value: 22,
                //         name: 'category6',
                //     },{
                //         value: 61,
                //         name: 'category7'
                //     },
                //     {
                //         value: 45,
                //         name: 'category8',
                //     },{
                //         value: 26,
                //         name: 'category9'
                //     },
                //     {
                //         value: 42,
                //         name: 'category10',
                //     },{
                //         value: 26,
                //         name: 'category11'
                //     },
                //     {
                //         value: 50,
                //         name: 'category12',
                //     }
                // ]
            }]
        };
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function echart_2() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('chart_2'));
        var data = {
            id: 'multipleBarsLines',
            title: '分类情感倾向',
            legendBar: ['积极', '消极'],
            symbol: '', //数值是否带百分号        --默认为空 ''
            legendLine: ['总'],
            toolbox: {
                    show: true,
                 feature: {
                dataView: {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'bar']},
                restore: {show: true},
                saveAsImage: {show: true}
                 }
            },
            xAxis:
            //     ['category1', 'category2', 'category3','category4', 'category5'
            // , 'category6', 'category7', 'category8', 'category9','category10', 'category11', 'category12'],
                server.categorys,
                // ['一月', '二月', '三月', '四月', '五月', '六月','一月', '二月', '三月', '四月', '五月', '六月'],
            yAxis: [
                server.positive,
                server.negative
                // [2, 4, 5, 5, 1, 7,3, 6, 6, 1, 1, 3],
                // [6, 6, 5, 6, 3, 6,5, 4, 4, 10, 3, 10]
            ],
            lines: [
                server.num
                // [8, 10, 10, 11, 4, 13,8, 10, 10, 11, 4, 13]
            ],
            barColor: ['#b4dbf3', '#0063ff', '#e1e9ea'], //柱子颜色 必填参数
            lineColor: ['#f52a0f'], // 折线颜色

        };
        /////////////end/////////

        var myData = (function test() {
            var yAxis = data.yAxis || [];
            var lines = data.lines || [];
            var legendBar = data.legendBar || [];
            var legendLine = data.legendLine || [];
            var symbol = data.symbol || ' ';
            var seriesArr = [];
            var legendArr = [];
            yAxis && yAxis.forEach((item, index) => {
                legendArr.push({
                    name: legendBar && legendBar.length > 0 && legendBar[index]
                });
                seriesArr.push({
                    name: legendBar && legendBar.length > 0 && legendBar[index],
                    type: 'bar',
                    barGap: '0.5px',
                    data: item,
                    barWidth: data.barWidth || 12,
                    label: {
                        normal: {
                            show: true,
                            formatter: '{c}' + symbol,
                            position: 'top',
                            textStyle: {
                                color: '#fff',
                                fontStyle: 'normal',
                                fontFamily: '微软雅黑',
                                textAlign: 'left',
                                fontSize: 11,
                            },
                        },
                    },
                    itemStyle: { //图形样式
                        normal: {
                            barBorderRadius: 4,
                            color: data.barColor[index]
                        },
                    }
                });
            });

            lines && lines.forEach((item, index) => {
                legendArr.push({
                    name: legendLine && legendLine.length > 0 && legendLine[index]
                })
                seriesArr.push({
                    name: legendLine && legendLine.length > 0 && legendLine[index],
                    type: 'line',
                    data: item,
                    itemStyle: {
                        normal: {
                            color: data.lineColor[index],
                            lineStyle: {
                                width: 3,
                                type: 'solid',
                            }
                        }
                    },
                    label: {
                        normal: {
                            show: false, //折线上方label控制显示隐藏
                            position: 'top',
                        }
                    },
                    symbol: 'circle',
                    symbolSize: 10
                });
            });

            return {
                seriesArr,
                legendArr
            };
        })();


        option = {
            title: {
                show: true,
                top: '10%',
                left: '3%',
                text: data.title,
                textStyle: {
                    fontSize: 18,
                    color: '#fff'
                },
                subtext: data.subTitle,
                link: ''
            },
            toolbox: {
                show: true,
                feature: {
            mark: {show: true},
            dataView: {show: true, readOnly: false},
            restore: {show: true},
            saveAsImage: {show: true}
                     }
            },
            tooltip: {
                trigger: 'axis',
                formatter: function (params) {
                    var time = '';
                    var str = '';
                    for (var i of params) {
                        time = i.name.replace(/\n/g, '') + '<br/>';
                        if (i.data == 'null' || i.data == null) {
                            str += i.seriesName + '：无数据' + '<br/>'
                        } else {
                            str += i.seriesName + '：' + i.data + symbol + '%<br/>'
                        }

                    }
                    return time + str;
                },
                axisPointer: {
                    type: 'none'
                },
            },
            legend: {
                right: data.legendRight || '30%',
                top: '12%',
                right: '5%',
                itemGap: 16,
                itemWidth: 10,
                itemHeight: 10,
                data: myData.legendArr,
                textStyle: {
                    color: '#fff',
                    fontStyle: 'normal',
                    fontFamily: '微软雅黑',
                    fontSize: 12,
                }
            },
            grid: {
                x: 30,
                y: 80,
                x2: 30,
                y2: 60,
            },
            xAxis: {
                type: 'category',
                data: data.xAxis,
                axisTick: {
                    show: false,
                },

                axisLine: {
                    show: true,
                    lineStyle: {
                        color: '#1AA1FD',
                    },
                    symbol: ['none', 'arrow']
                },
                axisLabel: {
                    show: true,
                    interval: '0',
                    textStyle: {
                        lineHeight: 16,
                        padding: [2, 2, 0, 2],
                        height: 50,
                        fontSize: 12,
                    },
                    rich: {
                        Sunny: {
                            height: 50,
                            // width: 60,
                            padding: [0, 5, 0, 5],
                            align: 'center',
                        },
                    },
                    formatter: function (params, index) {
                        var newParamsName = "";
                        var splitNumber = 5;
                        var paramsNameNumber = params && params.length;
                        if (paramsNameNumber && paramsNameNumber <= 4) {
                            splitNumber = 4;
                        } else if (paramsNameNumber >= 5 && paramsNameNumber <= 7) {
                            splitNumber = 4;
                        } else if (paramsNameNumber >= 8 && paramsNameNumber <= 9) {
                            splitNumber = 5;
                        } else if (paramsNameNumber >= 10 && paramsNameNumber <= 14) {
                            splitNumber = 5;
                        } else {
                            params = params && params.slice(0, 15);
                        }

                        var provideNumber = splitNumber; //一行显示几个字
                        var rowNumber = Math.ceil(paramsNameNumber / provideNumber) || 0;
                        if (paramsNameNumber > provideNumber) {
                            for (var p = 0; p < rowNumber; p++) {
                                var tempStr = "";
                                var start = p * provideNumber;
                                var end = start + provideNumber;
                                if (p == rowNumber - 1) {
                                    tempStr = params.substring(start, paramsNameNumber);
                                } else {
                                    tempStr = params.substring(start, end) + "\n";
                                }
                                newParamsName += tempStr;
                            }

                        } else {
                            newParamsName = params;
                        }
                        params = newParamsName;
                        return '{Sunny|' + params + '}';
                    },
                    color: '#1AA1FD',
                },

            },
            yAxis: {
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: '#1AA1FD',
                    },
                    symbol: ['none', 'arrow']
                },
                type: 'value',
                axisTick: {
                    show: false
                },
                axisLabel: {
                    show: false
                },
                splitLine: {
                    show: false,
                    lineStyle: {
                        color: '#1AA1FD',
                        type: 'solid'
                    },
                }
            },
            series: myData.seriesArr
        }
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function echart_3() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('chart_3'));

        var option;

        option = {
    // title: {
    //     text: '多雷达图'
    // },
    toolbox: {
                    show: true,
                 feature: {
                dataView: {show: true, readOnly: false},
                // magicType: {show: true, type: ['line', 'bar']},
                restore: {show: true},
                saveAsImage: {show: true}
                 }
            },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        left: 'center',
        data: ['sum', 'positive', 'negative'],
        textStyle: {
                    color: "#fff",
                    fontSize: 12
                },
    },
    radar: [
        {
            indicator: [
                {text: 'sum', max: server.numSum},
                {text: 'positive', max: server.positiveSum},
                {text: 'negative', max: server.negativeSum},
                // {text: '功能', max: 100}
            ],
            center: ['25%', '40%'],
            radius: 80
        },
        // {
        //     indicator: [
        //         {text: '外观', max: 100},
        //         {text: '拍照', max: 100},
        //         {text: '系统', max: 100}
        //     ],
        //     radius: 80,
        //     center: ['50%', '60%'],
        // },
        {
            indicator: (function (){
                var res = [];
                for (var i = 1; i <= 12; i++) {
                    res.push({text: 'category' +i , max: 20});
                }
                return res;
            })(),
            center: ['75%', '40%'],
            radius: 80
        }
    ],
    series: [
        {
            type: 'radar',
            tooltip: {
                trigger: 'item'
            },
            areaStyle: {},
            data: [
                {
                    value: server.num,
                        // [60, 73, 85, 40],
                    name: 'sum'
                }
            ]
        },
        // {
        //     type: 'radar',
        //     radarIndex: 1,
        //     areaStyle: {},
        //     data: [
        //         {
        //             value: [85, 90, 90, 95, 95],
        //             name: '某主食手机'
        //         },
        //         {
        //             value: [95, 80, 95, 90, 93],
        //             name: '某水果手机'
        //         }
        //     ]
        // },
        {
            type: 'radar',
            radarIndex: 1,
            areaStyle: {},
            data: [
                {
                    name: 'positive',
                    value: server.positive,
                        // [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 75.6, 82.2, 48.7, 18.8, 6.0, 2.3],
                },
                {
                    name: 'negative',
                    value: server.negative,
                        // [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 35.6, 62.2, 32.6, 20.0, 6.4, 3.3]
                }
            ]
        }
    ]
        };
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function echart_4() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('chart_4'));
        var data = server.negative;
            // [70, 34, 60, 78, 69,70, 34, 60, 78,70, 34, 60];
        var titlename =
            server.categorys;
            // ['category1', 'category2', 'category3','category4', 'category5'
            // , 'category6', 'category7', 'category8', 'category9','category10', 'category11', 'category12'];
        var valdata = server.num;
            // [702, 406, 664, 793, 505,702, 406, 664, 793, 505,702, 406];
        var myColor = ['#cd8586', '#557b03', '#008af5','#0a82c7', '#0063ff', '#e1e9ea','#e72325', '#98e002', '#2ca3fd','#b4dbf3', '#cafa68', '#628db1'];
        option = {
            title: {
                text: '消极情感占比',
                x: 'center',
                textStyle: {
                    color: '#FFF'
                },
                left: '6%',
                top: '10%'
            },
            //图标位置
            grid: {
                top: '20%',
                left: '32%'
            },
        toolbox: {
            show: true,
            feature: {
            dataView: {show: true, readOnly: false},
            magicType: {show: true, type: ['line', 'bar']},
            restore: {show: true},
            saveAsImage: {show: true}
                }
             },
            xAxis: {
                show: false
            },
            yAxis: [{
                show: true,
                data: titlename,
                inverse: true,
                axisLine: {
                    show: false
                },
                splitLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                axisLabel: {
                    color: '#fff',
                    formatter: (value, index) => {
                        return [

                            `{lg|${index+1}}  ` + '{title|' + value + '} '
                        ].join('\n')
                    },
                    rich: {
                        lg: {
                            backgroundColor: '#339911',
                            color: '#fff',
                            borderRadius: 15,
                            // padding: 5,
                            align: 'center',
                            width: 15,
                            height: 15
                        },
                    }
                },


            }, {
                show: true,
                inverse: true,
                data: valdata,
                axisLabel: {
                    textStyle: {
                        fontSize: 12,
                        color: '#fff',
                    },
                },
                axisLine: {
                    show: false
                },
                splitLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },

            }],
            series: [{
                name: '条',
                type: 'bar',
                yAxisIndex: 0,
                data: data,
                barWidth: 10,
                itemStyle: {
                    normal: {
                        barBorderRadius: 20,
                        color: function(params) {
                            var num = myColor.length;
                            return myColor[params.dataIndex % num]
                        },
                    }
                },
                label: {
                    normal: {
                        show: true,
                        position: 'inside',
                        formatter: '{c}%'
                    }
                },
            }, {
                name: '框',
                type: 'bar',
                yAxisIndex: 1,
                barGap: '-100%',
                data:
                    server.num,
                    // [100, 100, 100, 100, 100,100, 100, 100,100, 100, 100, 100],
                barWidth: 15,
                itemStyle: {
                    normal: {
                        color: 'none',
                        borderColor: '#00c1de',
                        borderWidth: 3,
                        barBorderRadius: 15,
                    }
                }
            }, ]
        };
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }
});