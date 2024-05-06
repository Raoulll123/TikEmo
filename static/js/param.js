$(function() {
    var dom = document.getElementById("chart_2");
    var myChart = echarts.init(dom);
    var app = {};
    var metrodates = server.content1;
    var figures = server.content2;
    let result = metrodates.map((name,i) => ({name, value: figures[i]}));
    option = null;
option = {
legend: {
    show: true,
        orient: 'vertical',
        left: 'right',
textStyle: {
                    color: "#d5fffe",
                    fontSize: 14
                },
    },
    toolbox: {
        show: true,
        feature: {
            mark: {show: true},
            dataView: {show: true, readOnly: false},
            // magicType: {show: true, type: ['stack','tiled']},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    series: [
        {
            name: 'DBI指数',
            type: 'pie',
            radius: [15, 60],
            center: ['50%', '50%'],
            roseType: 'area',
            itemStyle: {
                borderRadius: 8
            },
            data:
            result
            //     [
            //     {value: 0.3609, name: '24岁及以下'},
            //     {value: 0.2148, name: '25-30岁'},
            //     {value: 0.3124, name: '31-35岁'},
            //     {value: 0.0872, name: '36-40岁'},
            //     {value: 0.0247, name: '40岁以上'}
            // ]
        }
    ]
};


    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }
});