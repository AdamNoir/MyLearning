$(document).ready(function(){
    //SLIDER
    // https://bxslider.com/examples/image-slideshow-captions/
    if(window.location.href.indexOf("index") > -1){
      $(function(){
        $('.bxslider').bxSlider({
          mode: 'fade',
          captions: true,
          slideWidth: 1200,
          responsive: true
        });
      });
    }


      // Post
      // Moment - Para fechas 
      /* https://momentjs.com/ */
      if(window.location.href.indexOf("index") > -1){
        var posts = [
          {
            title: "Prueba de Titulo",
            date: moment().format('LL'),
            content: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur laboriosam totam ipsum sed rem harum quia non quisquam possimus error ducimus dolorem omnis ex sit, voluptatem doloremque quam animi explicabo. Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur laboriosam totam ipsum sed rem harum quia non quisquam possimus error ducimus dolorem omnis ex sit, voluptatem doloremque quam animi explicabo."
          },
          {
            title: "Prueba de Titulo 2",
            date: moment().format('LL'),
            content: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur laboriosam totam ipsum sed rem harum quia non quisquam possimus error ducimus dolorem omnis ex sit, voluptatem doloremque quam animi explicabo. Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur laboriosam totam ipsum sed rem harum quia non quisquam possimus error ducimus dolorem omnis ex sit, voluptatem doloremque quam animi explicabo."
          },
          {
            title: "Prueba de Titulo 3",
            date: moment().format('LL'),
            content: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur laboriosam totam ipsum sed rem harum quia non quisquam possimus error ducimus dolorem omnis ex sit, voluptatem doloremque quam animi explicabo. Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur laboriosam totam ipsum sed rem harum quia non quisquam possimus error ducimus dolorem omnis ex sit, voluptatem doloremque quam animi explicabo."
          },
          {
            title: "Prueba de Titulo 4",
            date: moment().format('LL'),
            content: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur laboriosam totam ipsum sed rem harum quia non quisquam possimus error ducimus dolorem omnis ex sit, voluptatem doloremque quam animi explicabo. Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur laboriosam totam ipsum sed rem harum quia non quisquam possimus error ducimus dolorem omnis ex sit, voluptatem doloremque quam animi explicabo."
          },
          {
            title: "Prueba de Titulo 5",
            date: moment().format('LL'),
            content: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur laboriosam totam ipsum sed rem harum quia non quisquam possimus error ducimus dolorem omnis ex sit, voluptatem doloremque quam animi explicabo. Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur laboriosam totam ipsum sed rem harum quia non quisquam possimus error ducimus dolorem omnis ex sit, voluptatem doloremque quam animi explicabo."
          }
        ];

        /* Recorremos el array de Json y con una plantilla damos forma al contenido.
        Despues lo agregamos a la caja correspondiente. */
        posts.forEach((item, inde) => {
          var post = `
              <article class="post">
                <h2>${item.title}</h2>
                <span class="date">${item.date}</span>
                <p>${item.content}</p>
                <a href="#" class="button-more">Leer Mas</a>
              </article>
          `;
          $("#posts").append(post);
        });
      }
      // Cambiar Tema
      /* Tenemos dos hojas de estilos, la principal y la que da los colores.
      La de los colores tiene un ID, y cambiamos el contenido de su href al dar click. */
      var theme = $("#theme");

      $("#to-green").click(function(){
        theme.attr("href", "css/green.css");
      });

      $("#to-red").click(function(){
        theme.attr("href", "css/red.css");
      });

      $("#to-blue").click(function(){
        theme.attr("href", "css/blue.css");
      });

      // Scroll arriba de la web
      $(".subir").click(function(e){
        e.preventDefault();

        $("html, body").animate({
          scrollTop: 0
        }, 500);
        return false;
      });

      // Login Falso
      $("#login form").submit(function(){
        var form_name = $("#form_name").val();

        localStorage.setItem("form_name", form_name);
      });

      var form_name = localStorage.getItem("form_name");

      if(form_name != null && form_name != "undefined"){
        var about_parrafo = $("#about p");

        about_parrafo.html("<br><strong>Bienvenido, " + form_name + "</strong>");
        about_parrafo.append("<a href='#' id= 'logout'>Cerrar Session</a>");
        
        $("#login").hide();

        $("#logout").click(function(){
          localStorage.clear();
          location.reload();
        });
      }

      // Acordoeon
      if(window.location.href.indexOf("about") > -1){
        $("#acordeon").accordion();
      }

      // REloj
      if(window.location.href.indexOf("reloj") > -1){

        setInterval(function(){
          var reloj = moment().format('h:mm:ss');
          $("#reloj").html(reloj);
        }, 1000);
      }

      // Validacion de EMial.
      if(window.location.href.indexOf("contacto") > -1){
        $("form input[name='date'").datepicker({
          dateFormat: 'dd/mm/yy'
        });
        $.validate({
          lang: 'es'
        });
      }

});