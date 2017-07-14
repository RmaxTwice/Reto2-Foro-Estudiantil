$(document).ready(function(){

    $("a.icon").click(function(){
    	var x = document.getElementById("myTopnav");
    	var relleno = document.getElementsByClassName("relleno");
	    if (x.className === "topnav") {
	        x.className += " responsive";
            $("a#h-link-perfil").toggleClass("invisible")
            $("a#h-link-logout").toggleClass("invisible")
            $("a#h-link-admin-sol").toggleClass("invisible")
	        relleno[0].className += " responsive";
	    } else {
            $("a#h-link-perfil").toggleClass("invisible")
            $("a#h-link-logout").toggleClass("invisible")
            $("a#h-link-admin-sol").toggleClass("invisible")
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