$(document).ready(function(){
    console.log("03 Animaciones cargado.");

    var caja = $("#caja");

    $("#animar").click(function(){
        caja.animate({marginLeft: "500px",
                      fontSize: "40px",
                      height: "110px"         
                    }, "slow")
            .animate({
                borderRadius: "900px",
                marginTop: "90px"
            }, "slow")
            .animate({
                borderRadius: "0px",
                marginLeft: "0px"
            }, "slow")
            .animate({
                borderRadius: "100px",
                marginTop: "0px"
            }, "slow")
            .animate({
                borderRadius: "900px",
                marginTop: "90px"
            }, "slow");
            
    });
});