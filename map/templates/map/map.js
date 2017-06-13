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
fills = [];
for(i=0; i < 40; i++){
    fills.push(Math.random()*100);
}
var i;

var cols = ['#BF0014','#c66100', '#ca9f00', '#ca9f00', '#bbce00', '#80d200', '#42d500', '#02d900']

var count = 0;

{% for bin in latest_trash_list %}
    count += 1;
    var colVal = 100 - parseFloat(fills[count-1]);
    if(colVal < 20){
        col = cols[0];
    }else if(colVal < 25){
        col = cols[1];
    }else if(colVal < 30){
        col = cols[2];
    }else if(colVal < 35){
        col = cols[3];
    }else if(colVal < 40){
        col = cols[4];
    }else if(colVal < 45){
        col = cols[5];
    }else{
        col = cols[6];
    }

    //Make an SVG Container
    var svgContainer = d3.select("#trashDisplays").append("svg")
        .attr("width", 100)
        .attr("height", 150)
        .attr("padding", "10px 10px 10px 10px");
    //Draw the Rectangle
    svgContainer.append("a")
        .attr("href", "{% url 'map:detail' bin.id %}")
        .append("rect")
        .attr("width", 50)
        .attr("x", 25)
        .attr("y", function(d){
            return 110 - parseFloat(fills[count-1]);
        })
        .attr("height", function(d){
            return parseFloat(fills[count-1]) + 10;})
        .attr("fill", col);
    //Append text
    svgContainer.append("text")
        .attr('class', 'TrashCan' + count)
        .attr('text-anchor', 'middle')
        .attr("x", 50)
        .attr("y", 10)
        .text('#' + count);
{% endfor %}