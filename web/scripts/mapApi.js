//var coords = {lat: null, lng: null};
//var coords = {lat: -25.363, lng: 131.044};

function initMap() {
    var coords = {lat: Number(document.getElementById('latIn').value),
                  lng: Number(document.getElementById('lngIn').value)};
    var map = new google.maps.Map(document.getElementById('map'), {
                                  zoom: 4,
                                  center: coords});
    var marker = new google.maps.Marker({position: coords,
                                         map: map })
}