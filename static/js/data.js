$(function() {
    var dom = document.getElementById("container4");
    var myChart = echarts.init(dom);
    var app = {};
    option = null;
    var dataAxis =server.content1
var data = server.content2
option = {
    title: {
        subtext: '综合评分',
        show:false,
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['蒸发量', '降水量']
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
    calculable: true,
    xAxis: [
        {
            type: 'category',
            data: dataAxis
        }
    ],
    yAxis: [
        {
            type: 'value',
        }
    ],
    series: [
        {
            name: '综合评分',
            type: 'bar',
            data: data,
            markPoint: {
                data: [
                    {name: '最高', value: data[0], xAxis: 7, yAxis: 183},
                    {name: '最低', value: data[data.length-1], xAxis: 11, yAxis: 3}
                ]
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ]
            }
        }
    ]
};
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }
})