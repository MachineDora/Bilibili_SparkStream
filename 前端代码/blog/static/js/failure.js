
function data(){
  return stream_layers(2,10+Math.random()*100,.1).map(function(data, i) {
console.log( data );
    return {
      key: 'Stream' + i,
      values: data
    };
  });
}

/* Inspired by Lee Byron's test data generator. */
function stream_layers(n, m, o) {
  if (arguments.length < 3) o = 0;
  function bump(a) {
    var x = 1 / (.1 + Math.random()),
        y = 2 * Math.random() - .5,
        z = 10 / (.1 + Math.random());
    for (var i = 0; i < m; i++) {
      var w = (i / m - y) * z;
      a[i] += x * Math.exp(-w * w);
    }
  }
  return d3.range(n).map(function() {
      var a = [], i;
      for (i = 0; i < m; i++) a[i] = o + o * Math.random();
      for (i = 0; i < 5; i++) bump(a);
      return a.map(stream_index);
    });
}

/* Another layer generator using gamma distributions. */
function stream_waves(n, m) {
  return d3.range(n).map(function(i) {
    return d3.range(m).map(function(j) {
        var x = 20 * j / m - i / 3;
        return 2 * x * Math.exp(-.5 * x);
      }).map(stream_index);
    });
}

function stream_index(d, i) {
  return {x: i, y: Math.max(0, d)};
}


nv.addGraph(function() {


    word = [];
    count = [];
    var chart = nv.models.multiBarChart();

    chart.xAxis
        .tickFormat(d3.format(',f'));

setInterval(function () {
    $.ajaxSettings.async = false;
    $.getJSON('get_count/', function (ret) {
        $.each(ret, function (key, value) {
            word.push(key);
            count.push(value)
        });
    });
    $.ajaxSettings.async = true;
    d3.select('#chart svg')
        .datum([{'key':'总体',values:[
{'x':"NNN",'y':count[4],'series':0},

 ]
 },
{'key':'过滤',values:[
{'x':count[3],'y':count[5],'series':1} ,

]}]

               )
        .transition().duration(500)
        .call(chart)
        ;

    nv.utils.windowResize(chart.update);

    return chart;
},5000);
 //   chart.yAxis
 //       .tickFormat(d3.format(',f'));


});