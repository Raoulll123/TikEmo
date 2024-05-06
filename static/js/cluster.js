$(function() {
    var app = {};
    // var metrodates = server.content3;
    // var figures = x_data.content2;
    // let result = metrodates.map((name,i) => ({name, value: figures[i]}));
    var chartDom = document.getElementById('Land_analysis');
var myChart = echarts.init(chartDom);
var option;

var data1 = server.content1
option = {
    xAxis: {
        scale: true,
                axisLine: {
                show: true,
                lineStyle: {
                    color: '#d0f1f0'
                }
            },
    },
    yAxis: {
        scale: true,
        axisLine: {
                show: true,
                lineStyle: {
                    color: '#cff1f0'
                }
            },
    },
    toolbox: {
        show: true,
        feature: {
            dataView: {show: true, readOnly: false},
            // magicType: {show: true, type: ['stack','tiled']},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    series: [{
        type: 'effectScatter',
        symbolSize: 20,
        data: [
            data1[0],
            // data1[10]
        ],
       itemStyle: {
           color: '#ee2266'
        },
    }, {
        type: 'scatter',
        data: data1,
    }]
};

option && myChart.setOption(option);
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }
});