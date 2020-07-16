var map;
function initMap(latMap, lngMap) {
    if (latMap && lngMap) {
        var coord = {lat: latMap, lng: lngMap}
        map = new google.maps.Map(
            document.getElementById('map'), {center: coord, zoom: 12});

        var marker = new google.maps.Marker({position: coord, map: map})
    }
}
