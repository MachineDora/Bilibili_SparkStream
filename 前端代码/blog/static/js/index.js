/**
 * Created by Administrator on 2018/10/30.
 */

var myChart = echarts.init(document.getElementById('chart'));
var myChart2 = echarts.init(document.getElementById('chart2'));

word = [];
count = [];
word1=[];
count1=[];

word_ = [];
count_ = [];
word1_=[];
count1_=[];

result=0;

option = {
    tooltip: {
        trigger: 'axis'
    },
    xAxis: {
        data: word,
        axisLabel:{  interval: 0}
    },
    yAxis: {
        splitLine: {
            show: false
        }
    },
    dataZoom: [{
        start: 0,
        end: 100,
    }, {

        type: 'inside'
    }],
    visualMap: {
        top: 10,
        right: 10,
        pieces: [{
            gt: 0,
            lte: 50,
            color: '#096'
        }, {
            gt: 50,
            lte: 100,
            color: '#ffde33'
        }, {
            gt: 100,
            lte: 150,
            color: '#ff9933'
        }, {
            gt: 150,
            lte: 200,
            color: '#cc0033'
        }, {
            gt: 200,
            lte: 300,
            color: '#660099'
        }, {
            gt: 300,
            color: '#7e0023'
        }],
        outOfRange: {
            color: '#999'
        }
    },
    series: {
        name: '数量',
        type: 'bar',
        data: count,
        markLine: {
            silent: true,
            data: [{
                yAxis: 50
            }, {
                yAxis: 100
            }, {
                yAxis: 150
            }, {
                yAxis: 200
            }, {
                yAxis: 300
            }]
        }
    }
};
myChart.setOption(option);
myChart2.setOption(option);
setInterval(function () {
    item1=[];
    item2=[];
    $.ajaxSettings.async = false;
    $.getJSON('get_count/', function (ret) {
        word.slice(0,word.length);
        count.slice(0,count.length);
        $.each(ret, function (key, value) {
            item1.push(key);
            item2.push(value)
        });
    });
    if(item1.length===0){
        item1=word1;
        item2=count1;
    }
    $.ajaxSettings.async = true;
    word=item1;
    word1=item1;
    console.log(word1);
    count=item2;
    count1 = item2;
    myChart.setOption({
        xAxis: {
            data: word
        },
        series: {
            data: count
        }
    });

    item1_=[];
    item2_=[];
    $.ajaxSettings.async = false;
    $.getJSON('get_count2/', function (ret) {
        word_.slice(0,word_.length);
        count_.slice(0,count_.length);
        $.each(ret, function (key, value) {
            item1_.push(key);
            item2_.push(value)
        });
    });
    if(item1_.length===0){
        item1_=word1_;
        item2_=count1_;
    }
    $.ajaxSettings.async = true;
    word_=item1_;
    word1_=item1_;
    count_=item2_;
    count1_ = item2_;

    myChart2.setOption({
        xAxis: {
            data: word_
        },
        series: {
            data: count_
        }
    });
}, 4000);