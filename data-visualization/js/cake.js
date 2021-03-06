var json_data = '{"csharp":180,"python":50,"java":70,"linux":30,"windows":1,"php":45,"css":87,"html":31,"announced":21,"birthday":5,"excitement":27,"scent":45,"almonds":55,"always":31,"him":21,"her":4,"and":37,"love":45,"way":34,"toward":31,"hair":31,"fair":12,"magnificence":27,"special":45,"announced":34,"he":24,"she":21,"apple":1,"banana":27,"of":45,"party":87,"with":4,"an":21,"study":32,"way":12,"boy":23,"girl":87,"table":6,"desk":21,"dark":21,"dust":27,"cat":45,"dog":67,"fate":7,"himself":21,"adventures":32,"bitter":27,"would":45,"surprise":6,"talk":6,"speech":21,"test":1,"magnificence":27,"no":45,"yes":31,"can":45,"c++":27,"python":98}';

var width = 500; //高度
var height = 500; //宽度


var json_data = json_data.slice(1, json_data.length - 1)

function getWordsSort(raw_arr) {
    for (var i = 0; i < raw_arr.length; i++) {
        for (var j = i + 1; j < raw_arr.length; j++) {
            if (raw_arr[i].value < raw_arr[j].value) {
                var t = raw_arr[i];
                raw_arr[i] = raw_arr[j];
                raw_arr[j] = t;
            }
        }
    }
    if (raw_arr.length < 10) return raw_arr;
    return raw_arr.slice(0, 10);
}

function getWords() {
    return getWordsSort(
        json_data
            .split(',')
            .map(function (d) {
                t = (d.split(":"))[0];
                t = t.slice(1, t.length - 1);
                s = (d.split(":"))[1];
                return {label: t, value: parseInt(s)};
            }));


    colors = ["#7e3838", "#7e6538", "#7c7e38", "#587e38", "#387e45", "#387e6a", "#386a7e", "#FFA500", "#FFD700", "#FF4040"]
    for (var i = 0; i < words.length; i++) {
        words[i].color = colors[i];
    }
    return words;
}


var pie = new d3pie("pieChart", {
    "size": {
        "canvasHeight": height,
        "canvasWidth": width,
        "pieOuterRadius": "80%"
    },
    "data": {
        "content": getWords()
    },
    "labels": {
        "outer": {
            "pieDistance": 32
        },
        "inner": {
            "format": ""
        },
        "mainLabel": {
            "color": "#000000",
            "font": "微软雅黑"
        },
        "percentage": {
            "color": "#e1e1e1",
            "font": "verdana",
            "decimalPlaces": 0
        },
        "value": {
            "color": "#e1e1e1",
            "font": "verdana"
        },
        "lines": {
            "enabled": true,
            "color": "#cccccc"
        },
        "truncation": {
            "enabled": true
        }
    },
    "effects": {
        "pullOutSegmentOnClick": {
            "effect": "linear",
            "speed": 400,
            "size": 8
        }
    }
});