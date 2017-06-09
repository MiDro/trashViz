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
