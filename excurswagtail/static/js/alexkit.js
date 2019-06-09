jQuery(function($) {
    $(window).scroll(function(){
        if($(this).scrollTop()>140){
            $('#main-menu').addClass('f-nav');
        }
        else if ($(this).scrollTop()<140){
            $('#main-menu').removeClass('f-nav');
        }
    });
    $(".am__button-tour").click(function (e) {
        e.preventDefault();
    $(".am__button-tour").removeClass('active');
        $(this).toggleClass("active");
      });
});

var scrolled;
window.onscroll = function() {
    scrolled = window.pageYOffset || document.documentElement.scrollTop;
    if ($( document ).width() > 280 && scrolled > 200){
        $(".navbar").css({"background": "#ebd081"})
    }
    if(200 > scrolled){
        $(".navbar").css({"background": "none"})         
    }

}

AOS.init();