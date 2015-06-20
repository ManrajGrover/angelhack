window.onload = function () {
	navigator.geolocation.getCurrentPosition(function (position) {
		var latitude  = position.coords.latitude;
		var longitude = position.coords.longitude;
		//alert(latitude); 
		document.getElementById("lat").innerHTML = 28.449381;
	});
 }