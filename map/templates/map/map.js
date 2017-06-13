var lats = [{% for bin in latest_trash_list %} "{{bin.latitude}}", {% endfor %}];
var longs= [{% for bin in latest_trash_list %} "{{bin.longitude}}", {% endfor %}];
var i;
var homebase = {lat: 37.724930, lng: -122.156077};

function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 11,
    center: homebase
  });
  var marker = new google.maps.Marker({
    position: homebase,
    map: map
  });
  for(i=0; i < lats.length; i++){
    new google.maps.Marker({
      position: {lat: parseFloat(lats[i]), lng: parseFloat(longs[i])},
      map: map
    });
  }
}


 // get the fills
 var fills = [{% for bin in latest_trash_list %} "{{bin.fillLevel}}", {% endfor %}];

 var i;
 for(i = 0; i < fills.length; i++){
  var col;
  var colVal = 100 - parseFloat(fills[i]);
  if(colVal < 40){
    col = '#800000'
  }else if(colVal< 60){
    col = '#58BF00'; 
  }else if(colVal< 80){
    col = '#3A7F00';
  }else{  
    col = '#1D4000';
  }

  //Make an SVG Container
  var svgContainer = d3.select("#trashDisplays").append("svg")
                                     .attr("width", 100)
                                     .attr("height", 100)
                                     .attr("padding", "20px 20px 20px 20px");

    //Draw the Rectangle
  svgContainer.append("rect")
                 .attr("width", 51)
                 .attr("y", function(d){
                  return 100 - parseFloat(fills[i]);
                 })
                 .attr("height", function(d){
                  return parseFloat(fills[i]);})
                 .attr("fill", col);
  

  svgContainer.append("text")
         .attr('class', 'TrashCan' + i)
               .attr('text-anchor', 'middle')
               .attr("x", 25)
               .attr("y", 15)
        .text('T.C.' + (i+1));
  }