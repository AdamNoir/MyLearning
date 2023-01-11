$(document).ready(function(){
    console.log("02-Get.js")

    // GET
    $.get("https://reqres.in/api/users", {page: 2}, function(response){
        //console.log(response.data);
        response.data.forEach((element, index) => {
            $("#datos").append("<p>" + element.first_name + " " + element.last_name + "</p>");
        })
    });
});