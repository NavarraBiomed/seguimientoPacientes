queue()
    .defer(d3.json, "/data.json")
    .await(makeGraphs);


var ndx;

//Grupos
var numByHour;
var numByDay;
var numByTOAST;

//Charts
var hoursLineChart;
var dayRowChart;
var toastPieChart;

var charts = [];

$( window ).resize(function() {
	resizeCharts();
});

function endall(transition, callback) {
    if (transition.size() === 0) { callback() }
    var n = 0;
    transition
        .each(function() { ++n; })
        .each("end", function() { if (!--n) callback.apply(this, arguments); });
  }

function resetDuration(chart, duration){
	console.log("Reset duration of: " + chart);
	//chart.transitionDuration(duration)
}

function getChartByAnchor(anchor){
	var anchor = "#"+$(anchor).attr("id");
	for (var i = 0; i < charts.length; i++){
		if (charts[i].anchor() == anchor){
			return charts[i];
		}
	}
}

function resizeCharts(){

	for (var i = 0; i < charts.length; i++){
		margin = 0.85;
		var width = $(charts[i].anchor()).parent().width();
		var height = $(charts[i].anchor()).parent().height();
		height *= margin;
		charts[i].width(width);
		charts[i].height(height);
		charts[i].transitionDuration(0);
		//Reset animation to original value when the instant transtion ends
		d3.select(charts[i].anchor()).transition().each( "end", function() {
	            var chart = getChartByAnchor(this);
	            chart.transitionDuration(chart.originalDuration);
	    });
	}
	dc.renderAll();
}

function cleanData(datos){
    var weekday = new Array(7);
        weekday[1] = "Monday";
        weekday[2] = "Tuesday";
        weekday[3] = "Wednesday";
        weekday[4] = "Thursday";
        weekday[5] = "Friday";
        weekday[6] = "Saturday";
        weekday[7] =  "Sunday";


	//Clean data
	for (var i = 0; i < datos.length; i++){
		var d = datos[i];
		d.id = i;

        //Get day of the week
        var splitDate = d["fecha"].split("-");
        var date = new Date(splitDate[0], splitDate[1], splitDate[2])
        var dayN = date.getDay();
        if (dayN == 0){ dayN = 7; }
        d.day = weekday[dayN];

        //Get hour
        d.hora  = d["hora"].split(":")[0];
        if (d["hora_indet"] == true){
            d.hora = -1;
        }

	}

	return datos;
}


var data;
function makeGraphs(error, datos, galiciaJson) {
	datos = cleanData(datos);
    data = datos;
	//Create a Crossfilter instance
	ndx = crossfilter(datos);

	var hourDim = ndx.dimension(function(d) {
		return d["hora"];
	});

	var dayDim = ndx.dimension(function(d) {
		return d["day"];
	});

	var toastDim = ndx.dimension(function(d) {
        if (d["toast"] != -1){
            return d["toast"];
        }

	});

	numByHour = hourDim.group();
	numByDay = dayDim.group();
	numByTOAST = toastDim.group();

	//Charts
	hoursLineChart = dc.lineChart("#hour-line-chart");
	dayRowChart= dc.rowChart("#day-bar-chart");
	toastPieChart = dc.pieChart("#toast-pie-chart");

    hoursLineChart
        .width(500)
		.height(200)
		.margins({top: 10, right: 50, bottom: 30, left: 50})
		.dimension(hourDim)
		.group(numByHour)
		.x(d3.scale.linear().domain([0,23]))
		.elasticY(true)
		.renderLabel(true)
		.yAxis().ticks(3);

    dayRowChart
        .width(500)
        .height(300)
        .dimension(dayDim)
        .group(numByDay)
        .cap(10)
        .ordering(function(d){ return days.indexOf(d.key);})
        .elasticX(true)
        .othersGrouper(false) //Removes "Other" from the list
        .xAxis().ticks(4);

/*
    hoursLineChart
        .width( 500)
        .height(300)
        .dimension(dayDim)
        .group(numByDay)
        .x(d3.scale.linear().domain([0,23]))
        .elasticY(true)
        .renderLabel(true)
        .yAxis().ticks(3);
*/

    toastPieChart
        .width(500)
        .height(300)
        .dimension(toastDim)
        .group(numByTOAST)
        .slicesCap(7)
        .ordering(function(d){ return d.calls;});

    charts.push(hoursLineChart);
    charts.push(dayRowChart);
    charts.push(toastPieChart);

    for (var i = 0; i < charts.length; i++){
		charts[i].originalDuration = [charts[i].transitionDuration()].slice(0);
	}

    resizeCharts();

}
