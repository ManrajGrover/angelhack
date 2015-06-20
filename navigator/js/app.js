window.onload = function () {
   navigator.geolocation.getCurrentPosition(function (position) {var latitude  = position.coords.latitude;
var longitude = position.coords.longitude;
             alert(latitude); 
                //document.getElementById("lat").innerHTML = 28.449381;
//  var wo=77.2863689;
//                   position.coords.latitude ;
                //document.getElementById("long").innerHTML = 77.284119;
                
//                document.getElementById("lat").style.display = "block";
            }
  );
 }