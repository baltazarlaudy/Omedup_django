let menu_toogle = document.getElementById('menu-toogle')
        let navbar_all = document.querySelector('.navbar-all')
        menu_toogle.addEventListener('click',function (){
            if(navbar_all.classList.contains('inactive')) {
                menu_toogle.classList.remove("inactive-menu")
                menu_toogle.classList.add("active-menu")
                navbar_all.classList.remove("inactive")
                navbar_all.classList.add('active')
            }else {
                menu_toogle.classList.remove("active-menu")
                menu_toogle.classList.add("inactive-menu")
                navbar_all.classList.remove("active")
                navbar_all.classList.add('inactive')
            }
        });
/*scroll navbar
 */
window.addEventListener('scroll', function () {
    let scroll = document.querySelector('.navigation')
    let navbar_left = document.querySelector('.navbar-left')
    scroll.classList.toggle("effect-scroll", window.scrollY > 0)
    navbar_left.classList.toggle("effect-scroll", window.scrollY > 0)
})

/* javascript for login form
 */

let email = document.getElementById('email')
let login_input = document.querySelector('.login-input')
    email.addEventListener('input', function () {
    let text_error = document.getElementById('text-error')
    let mailformat = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    let data = email.value
    if (data.match(mailformat)) {
        text_error.innerText = "";
        let button;
        button.desabled = false;
    } else {
        text_error.innerText = "Email invalid";
    }
})

/*image preview
 */

/*
let loadfile = function(event){
     let output = document.getElementById('output');

     /*let old = document.getElementById('old')
    output.src = URL.createObjectURL(event.target.files[0]);
    output.onload = function() {
      URL.revokeObjectURL(output.src) // free memory
    }
}*/
