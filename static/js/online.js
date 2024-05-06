$(function() {
    var dom = document.getElementById("container2");
    var myChart = echarts.init(dom);
    var app = {};
    // var metrodates = server.content3;
    // var figures = x_data.content2;
    // let result = metrodates.map((name,i) => ({name, value: figures[i]}));
    option = null;
option = {
legend: {
        orient: 'vertical',
        left: 'left',
        show:false
    },
toolbox: {
        show: false,
        feature: {
            dataView: {show: true, readOnly: false},
            // magicType: {show: true, type: ['line', 'bar']},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    series: [
        {
            name: '使用人群年龄占比',
            type: 'pie',
            radius: [15, 60],
            center: ['35%', '30%'],
            roseType: 'area',
            itemStyle: {
                borderRadius: 8
            },
            data:
            // result
                [
                {value: 0.3609, name: '24岁及以下'},
                {value: 0.2148, name: '25-30岁'},
                {value: 0.3124, name: '31-35岁'},
                {value: 0.0872, name: '36-40岁'},
                {value: 0.0247, name: '40岁以上'}
            ]
        }
    ]
};


    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }
});