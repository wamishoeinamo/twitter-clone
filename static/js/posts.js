//////////////////////////
///Java Script for posts page
/////////////////////////////
 $(function() {
     //Excuted when js-menu-incon js Clicked
      $('.js-menu-icon').click(function() {
       //$(this): Self element, namely div.js-menu-icon
        //next() : Next to div.js-menu-icon, namely div.menu
        //toggle() : Switch show and hide
        $(this).next().toggle();
        
   })
})