var json_data = '{"csharp":100,"python":50,"java":70,"linux":30,"windows":1,"php":45,"css":87,"html":31,"announced":21,"birthday":5,"excitement":27,"scent":45,"almonds":55,"always":31,"him":21,"her":4,"and":37,"love":45,"way":34,"toward":31,"hair":31,"fair":12,"magnificence":27,"special":45,"announced":34,"he":24,"she":21,"apple":1,"banana":27,"of":45,"party":87,"with":4,"an":21,"study":32,"way":12,"boy":23,"girl":87,"table":6,"desk":21,"dark":21,"dust":27,"cat":45,"dog":67,"fate":7,"himself":21,"adventures":32,"bitter":27,"would":45,"surprise":6,"talk":6,"speech":21,"test":1,"magnificence":27,"no":45,"yes":31,"can":45,"c++":27,"python":98}';

var max_size = 60; //一次显示的最大数值
var timeout = 1000000000; //刷新图片的时间
var width = 500; //高度
var height = 500; //宽度


function wordCloud(selector) {

    var fill = d3.scale.category20();

    var svg = d3.select(selector).append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

    function draw(words) {
        var cloud = svg.selectAll("g text")
            .data(words, function (d) {
                return d.text;
            })

        cloud.enter()
            .append("text")
            .style("font-family", "Impact")
            .style("fill", function (d, i) {
                return fill(i);
            })
            .attr("text-anchor", "middle")
            .attr('font-size', 1)
            .text(function (d) {
                return d.text;
            });

        cloud
            .transition()
            .duration(600)
            .style("font-size", function (d) {
                return d.size + "px";
            })
            .attr("transform", function (d) {
                return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
            })
            .style("fill-opacity", 1);

        cloud.exit()
            .transition()
            .duration(200)
            .style('fill-opacity', 1e-6)
            .attr('font-size', 1)
            .remove();
    }


    return {
        update: function (words) {
            d3.layout.cloud().size([width, height])
                .words(words)
                .padding(5)
                .rotate(function () {
                    return ~~(Math.random()) * 90 - 45;
                })
                .font("Impact")
                .fontSize(function (d) {
                    return d.size;
                })
                .on("end", draw)
                .start();
        }
    }

}

json_data = json_data.slice(1, json_data.length - 1)

//		function getWordsRandom(raw_arr, size) {
//			if(size >= raw_arr) return raw_arr;
//			var arr = [];
//			var flag = new Array(raw_arr.length);
//			var cnt = 0;
//			while(1) {
//				pos = parseInt(raw_arr.length*Math.random());
//				if(flag[pos] == 1) continue;
//				arr.push(raw_arr[pos]);
//				flag[pos] = 1;
//				cnt = cnt + 1;
//				if(cnt == size) break;
//			};
//
//			return arr;
//		}

function getWordsSort(raw_arr, size) {
    for (var i = 0; i < raw_arr.length; i++) {
        for (var j = i + 1; j < raw_arr.length; j++) {
            if (raw_arr[i].size < raw_arr[j].size) {
                var t = raw_arr[i];
                raw_arr[i] = raw_arr[j];
                raw_arr[j] = t;
            }
        }
    }
    var arr = raw_arr.slice(0, size);
    for (i = arr.length - 1; i >= 0; i--) {
        arr[i].size = arr[i].size * 99 / arr[0].size;
    }
    return arr;
}

function getWords(size) {

    return getWordsSort(
        json_data
            .split(',')
            .map(function (d) {
                t = (d.split(":"))[0];
                t = t.slice(1, t.length - 1);
                s = (d.split(":"))[1];
                return {text: t, size: parseInt(s)};
            }), size);
}

function showNewWords(vis) {
    vis.update(getWords(max_size))
    setTimeout(function () {
        showNewWords(vis)
    }, timeout)
}

var myWordCloud = wordCloud('svg');

showNewWords(myWordCloud);