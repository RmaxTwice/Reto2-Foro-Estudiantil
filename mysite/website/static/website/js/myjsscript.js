$(document).ready(function(){
    $("a.icon").click(function(){

    	var x = document.getElementById("myTopnav");
    	var relleno = document.getElementsByClassName("relleno");
	    if (x.className === "topnav") {
	        x.className += " responsive";
	        relleno[0].className += " responsive";
	    } else {
	        x.className = "topnav";
	        relleno[0].className = "relleno"
	    }



    });
    	
    
});

function responsiveNav() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
} 