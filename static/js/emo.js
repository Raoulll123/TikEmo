$(function() {
        var chartDom = echarts.init(document.getElementById('main0'));
var myChart = echarts.init(chartDom);
var option;
// var num = server.content1;
//         var positive = server.content2;
//         var negative =server.content3;
option = {
    legend: {
        top: 'bottom'
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
    series: [
        {
            name: '面积模式',
            type: 'pie',
            radius: [50, 250],
            center: ['50%', '50%'],
            roseType: 'area',
            itemStyle: {
                borderRadius: 8
            },
            data: [
                // {value: negative, name: 'negative'},
                // {value: positive, name: 'positive'},
                // {value: num, name: 'num'},
                 {value: 40, name: 'rose 1'},
                {value: 38, name: 'rose 2'},
                {value: 32, name: 'rose 3'},
                {value: 30, name: 'rose 4'},
                {value: 28, name: 'rose 5'},
                {value: 26, name: 'rose 6'},
                {value: 22, name: 'rose 7'},
                {value: 18, name: 'rose 8'}
            ]
        }
    ]
};

option && myChart.setOption(option);
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }
});