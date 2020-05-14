// console.log(window)

var divs = document.getElementsByTagName("div");
for(var i = 0; i < divs.length; i++){
    //do something to each div like
    console.log(divs[i]);
 }

console.log(document.getElementById('mapid'));

var mymap = L.map('mapid').setView([51.505, -0.09], 13);
// L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={pk.eyJ1IjoiamZnMzg4IiwiYSI6ImNrYTVtZ3pkMjAxbGkzc25vZmRqZzYxejgifQ.d7_9OMz3M1pERzLAfbK3ew}', {
//     attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
//     maxZoom: 18,
//     id: 'mapbox/streets-v11',
//     tileSize: 512,
//     zoomOffset: -1,
//     accessToken: 'pk.eyJ1IjoiamZnMzg4IiwiYSI6ImNrYTVtZ3pkMjAxbGkzc25vZmRqZzYxejgifQ.d7_9OMz3M1pERzLAfbK3ew'
// }).addTo(mymap);