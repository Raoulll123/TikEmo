$(function() {
	var dom = document.getElementById("container");
	var myChart = echarts.init(dom);
	var app = {};
	option = null;
	app.title = '用户性别';
	
	option = {
	    tooltip: {
	        trigger: 'item',
	        formatter: "{a} <br/>{b}: {c} ({d}%)"
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
	    legend: {
	        orient: 'horizontal',
	        x: 'center',
	        data:['女性','男性'],
	        itemWidth: 8,
	        itemHeight: 8,
	        textStyle:{//图例文字的样式
	            color:'#fff',
	            fontSize:12
	        }
	    },
	    color:['#37a2da','#ffd85c'],
	    series: [
	        {
	            name:'女性',
	            type:'pie',
	            radius: ['50%', '70%'],
	            avoidLabelOverlap: false,
	            label: {
	                normal: {
	                    show: false,
	                    position: 'center'
	                },
	                emphasis: {
	                    show: true,
	                    textStyle: {
	                        fontSize: '24',
	                        color:'#00fcff',
	                        fontWeight: 'bold'
	                    }
	                }
	            },
	            labelLine: {
	                normal: {
	                    show: false,
	                }
	            },
	            data:[
	                {value:0.4708, name:'女性'},
	                {value:0.5292, name:'男性'}
	            ]
	        }
	    ]
	};

	if (option && typeof option === "object") {
	    myChart.setOption(option, true);
	}
});