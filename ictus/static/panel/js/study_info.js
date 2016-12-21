queue()
    .defer(d3.json, "/study/"+study_id+"/json/")
    .await(makeGraphs);


var ndx;

//Grupos
var numByUser;
var numByHospital;
var numByClips;

//Charts
var usersRowChart;
var hospitalRowChart;
var clipsPieChart;

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
	//Clean data
	for (var i = 0; i < datos.length; i++){
		var d = datos[i];
		d.id = i;


		if (d.clips == 0){
			d.clips = "Control group";
		} else if (d.clips == 1){
			d.clips = "Treatment group";
		} else{
			d.clips = "Undefined";
		}
		console.log(d);

	}

	return datos;
}


function makeGraphs(error, datos, galiciaJson) {
	datos = cleanData(datos);

	//Create a Crossfilter instance
	ndx = crossfilter(datos);

	var doctorDim = ndx.dimension(function(d) { 
		return d["doctor"];
	});

	var hospitalDim = ndx.dimension(function(d) { 
		return d["hospital"];
	});

	var clipsDim = ndx.dimension(function(d) { 
		return d["clips"];
	});

	numByUser = doctorDim.group();
	numByHospital = hospitalDim.group();
	numByClips = clipsDim.group();

	//Charts
	usersRowChart = dc.rowChart("#user-bar-chart");
	hospitalRowChart= dc.rowChart("#hospital-bar-chart");
	clipsPieChart = dc.pieChart("#clips-pie-chart");

	usersRowChart
        .width(500)
        .height(300)
        .dimension(doctorDim)
        .group(numByUser)    
        .cap(11)
        .ordering(function(d){ return d.calls;})
        .elasticX(true)	
        .othersGrouper(false) //Removes "Other" from the list
        /*
        .colors(d3.scale.ordinal().domain(["user","other"])
                                .range(["#FF0000","#6BAED6"]))
        .colorAccessor(function(d) { 
            if(d.key == 'Tom'){
            	console.log("--TOM!!");
                return 0
            } else{
            	console.log("---NOT TOM: ");
	            console.log(d.key);
	            return 1;
            }            
        })
		*/
        .xAxis().ticks(4);

    hospitalRowChart
        .width(500)
        .height(300)
        .dimension(hospitalDim)
        .group(numByHospital)    
        .cap(11)
        .ordering(function(d){ return d.calls;})
        .elasticX(true)	
        .othersGrouper(false) //Removes "Other" from the list
        .xAxis().ticks(4);

    clipsPieChart
        .width(500)
        .height(300)
        .dimension(clipsDim)
        .group(numByClips)    
        .slicesCap(3)
        .ordering(function(d){ return d.calls;});

    charts.push(usersRowChart);
    charts.push(hospitalRowChart);
    charts.push(clipsPieChart);

    for (var i = 0; i < charts.length; i++){
		charts[i].originalDuration = [charts[i].transitionDuration()].slice(0);
	}

    resizeCharts();

}