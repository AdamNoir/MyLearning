$(document).ready(function(){
    console.log("widgets");

    //tooltip
    $(document).tooltip();

    // dialog
    $("#lanzar-popup").click(function(){
        $("#popup").dialog();
    });

    // date picker
    $("#date-picker").datepicker();

    //Tabs
    $("#pestanas").tabs();
});