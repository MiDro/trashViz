function initMap() {
  var uluru = {lat: 37.724930, lng: -122.156077};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 11,
    center: uluru
  });
  var marker = new google.maps.Marker({
    position: uluru,
    map: map
  });    
}