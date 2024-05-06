$(function() {
var chartDom = document.getElementById('main');
var myChart = echarts.init(chartDom);
    var app = {};
    // var data1= server.content1
    // var data2 = server.content2
    option = null;
var option;

// option = {
//     tooltip: {
//         trigger: 'axis',
//         axisPointer: {
//             type: 'cross',
//             crossStyle: {
//                 color: '#999'
//             }
//         }
//     },
//     toolbox: {
//         feature: {
//             dataView: {show: true, readOnly: false},
//             magicType: {show: true, type: ['line', 'bar']},
//             restore: {show: true},
//             saveAsImage: {show: true}
//         }
//     },
//     legend: {
//         data: ['播放量', '综合评分','弹幕量' ]
//     },
//     xAxis: [
//         {
//             type: 'category',
//             data:x_data.content3,
//             axisPointer: {
//                 type: 'shadow'
//             }
//         }
//     ],
//     yAxis: [
//         {
//             type: 'value',
//             name: '数量',
//             min: 0,
//             max: 4200000,
//             interval: 120000,
//             axisLabel: {
//                 formatter: '{value}'
//             }
//         },
//         {
//             type: 'value',
//             name: '分数',
//             min: 0,
//             max: 12000,
//             interval: 600,
//             axisLabel: {
//                 formatter: '{value} 分'
//             }
//         }
//     ],
//     series: [
//         {
//             name: '播放量',
//             type: 'bar',
//             data: x_data.content1
//         },
//         {
//             name: '综合评分',
//             type: 'bar',
//             data: x_data.content4
//         },
//         {
//             name: '弹幕量',
//             type: 'line',
//             yAxisIndex: 1,
//             data: x_data.content2
//         }
//     ]
// };
var colors = ['#9eafff', '#91CC75', '#EE6666'];

option = {
    color: colors,

    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'cross'
        }
    },
    grid: {
        right: '20%'
    },
    toolbox: {
        show: false,
        feature: {
            dataView: {show: true, readOnly: false},
            magicType: {show: true, type: ['line', 'bar']},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    legend: {
        data: ['点赞量', '弹幕量','播放量' ],
        show:false,
    },
    xAxis: [
        {
            type: 'category',
            axisTick: {
                alignWithLabel: true
            },
            data: x_data.content3,
        }
    ],
    yAxis: [
        {
            type: 'value',
            name: '点赞量',
            min: 0,
             max: 5200000,
            interval: 120000,
            position: 'left',
            axisLine: {
                show: true,
                lineStyle: {
                    color: colors[0]
                }
            },
            axisLabel: {
                formatter: '{value} 分'
            }
        },
                {
            type: 'value',
            name: '弹幕量',
            min: 0,
            max: 12000,
            interval: 600,
            position: 'right',
            offset: 80,
            axisLine: {
                show: true,
                lineStyle: {
                    color: colors[1]
                }
            },
            axisLabel: {
                formatter: '{value} 条'
            }
        },
        {
            type: 'value',
            name: '播放量',
            min: 0,
            max: 300000,
            interval: 10000,
            position: 'right',
            axisLine: {
                show: true,
                lineStyle: {
                    color: colors[2]
                }
            },
            axisLabel: {
                formatter: '{value} ml'
            }
        },
    ],
    series: [
        {
            name: '综合评分',
            type: 'bar',
            data: server.content2
            // x_data.content4
        },{
            name: '弹幕量',
            type: 'line',
            yAxisIndex: 1,
            data: x_data.content2
        },
         {
            name: '播放量',
            type: 'bar',
            data: x_data.content1
        }
    ]
};
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }
});