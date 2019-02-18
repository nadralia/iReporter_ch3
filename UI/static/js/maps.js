let mymap = L.map('google-map').setView([0.287560, 32.616670], 15);;

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1IjoibmFkcmFsaWEiLCJhIjoiY2pzYTY1ZXhsMDA3eDQzbG1vNHJpZndudiJ9.N0NL8KnjzAbwjAtl43GCuQ'
}).addTo(mymap);

var popup = L.popup();

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(mymap);
		document.getElementById('latitude').value = (e.latlng.lat);
		document.getElementById('longitude').value = (e.latlng.lng);
}

mymap.on('click', onMapClick);