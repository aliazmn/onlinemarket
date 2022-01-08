/*--------------------- Copyright (c) 2021 -----------------------
[Master Javascript]
Project: Shopmartio - Responsive HTML Template 
Version: 1.0.0
Assigned to: Theme Forest
-------------------------------------------------------------------*/
(function ($) {
	"use strict";
	/*-----------------------------------------------------
		Function  Start
	-----------------------------------------------------*/
		var Ecommerce = {
			initialised: false,
			version: 1.0,
			mobile: false,
			init: function () {
				if (!this.initialised) {
					this.initialised = true;
				} else {
					return;
				}
				/*-----------------------------------------------------
					Function Calling
				-----------------------------------------------------*/
				this.preloader();
				this.nice_select();
				this.search_box();
				this.cart_box();
				this.nav_menu();
				this.e_banner();
				this.isotop_gallery();
				this.bsaller_slider();
				this.top_button();
				this.category_grid();
				this.pdetails_gallery();
				this.quantity();
				this.popup_video();
				this.offer_counter();
				this.product_remove();
			},

			/*-----------------------------------------------------
				Preloader
			-----------------------------------------------------*/
			preloader: function () {
				$(window).on('load', function () {
					$(".preloader-wrapper").removeClass('preloader-active');
				});
				$(window).on('load', function () {
					setTimeout(function () {
						$('.preloader-open').addClass('loaded');
					}, 100);
				});
			},
			/*-----------------------------------------------------
				Nice Select
			-----------------------------------------------------*/
			nice_select : function () {
                if ($('select').length > 0) {
                    $('select').niceSelect();
                }				
			},
			/*-----------------------------------------------------
				Search Bar
			-----------------------------------------------------*/
			search_box: function () {
				$('.hs-search-cart-list').on("click", ".c-search-btn", function (e) {
				    e.stopPropagation();
					$('.search-main-wrap').addClass('show');
				});
				$('.c-search-close').on("click", function () {
					$('.search-main-wrap').removeClass('show');
				});
				$('.search-main-wrap').on("click", function () {
					$('.search-main-wrap').removeClass('show');
				});
				$(".search-box").on('click', function (e) {
					e.stopPropagation();
				});
			},
			/*-----------------------------------------------------
				Cart Box
			-----------------------------------------------------*/
			cart_box: function () {
				$('.cmn-cart-tgl').on("click", function (e) {
					e.stopPropagation();
					$('body').toggleClass('open-cart');
				});
				$('.close-box').on("click", function () {
					$('body').removeClass('open-cart');
				});
				$(".sb-cartbox").on('click', function (e) {
					e.stopPropagation();
				});
				$(document).on("click",function() {
					$('body').removeClass('open-cart');
				});
			},
			/*-----------------------------------------------------
				 Mobile Menu 
			-----------------------------------------------------*/
			nav_menu: function () {
				// mobile toggle
				$(".c-toggle-btn").on('click', function (e) {
					e.stopPropagation();
					$("body").toggleClass("menu-open");
				});

				var w = window.innerWidth;
				if (w <= 1199) {
					$('.main-menu-wraper').on('click', '.menu-list > li', function (e) {
					    e.stopPropagation();
						$('.menu-list > li').not($(this)).closest('li').find('.drop-menu, .super-sub-menu').slideUp();
						$('.menu-list > li').not($(this)).closest('li').removeClass('open');
						$(this).closest('li').find('.drop-menu').slideToggle();
						$(this).toggleClass('open');
					});
					$('.drop-menu').on('click', '.sub-menu > li', function (e) {
						e.stopPropagation();
						$('.sub-menu > li').not($(this)).closest('li').find('.super-sub-menu').slideUp();
						$('.sub-menu > li').not($(this)).closest('li').removeClass('open');
						$(this).closest('li').find('.super-sub-menu').slideToggle();
						$(this).toggleClass('open');
					});
				}
			},
			/*-----------------------------------------------------
				Banner Slider 
			-----------------------------------------------------*/
			e_banner: function () {
				if($('.e-banner-wrapper .swiper-container').length > 0){
					var ebannerSliderr = new Swiper('.e-banner-wrapper .swiper-container', {
						autoHeight: false,
						autoplay: true,
						loop: true,
						spaceBetween: 0,
						centeredSlides: false,
						speed: 1500,
						autoplay: {
							delay: 8000,
						},
						keyboard: {
							enabled: true,
						},
						navigation: {
							nextEl: '.swiper-button-next',
							prevEl: '.swiper-button-prev',
						},
						pagination: {
							el: '.swiper-pagination',
							clickable: true,
						},
					});
				}
			},
			/*-----------------------------------------------------
				isotop gallery
			-----------------------------------------------------*/
			isotop_gallery: function() {
				if($('.gallery-grid').length > 0){
					$('.gallery-grid').isotope({
						itemSelector: '.grid-item',
						filter: '*'
					});
					$('.e-gallery > .gallery-nav > ul > li').on( 'click', 'a', function() {
						// filter button click
						var filterValue = $( this ).attr('data-filter');
						$('.gallery-grid').isotope({ filter: filterValue });

						//active class added
						$('a').removeClass('gallery-active');
						$(this).addClass('gallery-active');
					});
				}
			},
			/*-----------------------------------------------------
				Best saller Slider 
			-----------------------------------------------------*/
			bsaller_slider: function () {
				if($('.e-best-slr-wrap .swiper-container').length > 0){
					var bestSlider = new Swiper('.e-best-slr-wrap .swiper-container', {
						autoHeight: false,
						spaceBetween: 30,
						slidesPerView: 4,
						loop: true,
						autoplay: true,
						speed: 1500,
						centeredSlides: false,
						autoplay: {
							delay: 1000,
						},
						navigation: {
							nextEl: '.swiper-button-next',
							prevEl: '.swiper-button-prev',
						},
						breakpoints: {
							0: {
								slidesPerView: 1,
								spaceBetween: 15,
							},
							500: {
								slidesPerView: 2,
								spaceBetween: 15,
							},
							768: {
								slidesPerView: 2,
								spaceBetween: 30,
							},
							992: {
								slidesPerView: 3,
								spaceBetween: 30,
							},
							1200: {
								slidesPerView: 4,
								spaceBetween: 30,
							},
						},
					});
				}
			},

			/*-----------------------------------------------------
				Go To Top Button
			-----------------------------------------------------*/
			top_button: function () {
				var scrollTop = $("#scroll");
				$('#scroll').on('click', function(){
					$("html, body").animate({
						scrollTop: 0
					}, 2000);
					return false;
				});

				$(function() {
					$('.go_to_demo').on('click', function(){
						$('html, body').animate({scrollTop: $('#go_to_demo').offset().top }, 'slow');
						return false;
					});
				});
			},

			/*-----------------------------------------------------
				Category List Grid View 
			-----------------------------------------------------*/
			category_grid: function() {
				$('.e-filter-list > li > a').on('click', function(){
					$('.e-filter-list > li > a').removeClass('active');
					$(this).addClass('active');
				});
				$('.Category-list-btn').on('click', function(){
					$('.e-procategory-inner').addClass('list-view');
				});
				$('.Category-grid-btn').on('click', function(){
					$('.e-procategory-inner').removeClass('list-view');
				});
			},
			/*-----------------------------------------------------
				Products details Slider 
			-----------------------------------------------------*/
			pdetails_gallery: function () {
				 if($('.pd-gallery-wrap').length > 0){
					$(document).on('click', '.pro_thumb', function(){
						$('.pd-img').find('img').attr('src', $(this).data('source'));
						$('.pd-thumb-list > li').not($(this)).closest('li').removeClass('active');
						$(this).closest('li').addClass('active');
					});
				 }
			},
			/*-----------------------------------------------------
				Products Quantity  
			-----------------------------------------------------*/
			quantity: function(){
				var quantity=0;
				$('.quantity-plus').on('click', function(e){
					e.preventDefault();
					var quantity = Number($(this).siblings('.quantity').val());
					$(this).siblings('.quantity').val(quantity + 1);            

				});
				$('.quantity-minus').on('click', function(e){
					e.preventDefault();
					var quantity = Number($(this).siblings('.quantity').val());
					if(quantity>0){
						$(this).siblings('.quantity').val(quantity - 1);
					}
				});				
			},
			/*-----------------------------------------------------
				Video Popup
			-----------------------------------------------------*/
			popup_video: function () {
				if($('.popup-youtube').length > 0){
					$('.popup-youtube').magnificPopup({
						type: 'iframe',
						iframe: {
							markup: '<div class="mfp-iframe-scaler">' +
								'<div class="mfp-close"></div>' +
								'<iframe class="mfp-iframe" frameborder="0" allowfullscreen></iframe>' +
								'<div class="mfp-title">بعضی از گزینه ها</div>' +
								'</div>',
							patterns: {
								youtube: {
									index: 'youtube.com/',
									id: 'v=',
									src: 'https://www.youtube.com/embed/wCMukPOGt1g'
								}
							}
						}
					});
				}
			},
			/*-----------------------------------------------------
				offer_counter
			-----------------------------------------------------*/
			offer_counter: function () {
				if($('#countdown').length > 0){
					(function () {
						const second = 1000,
							  minute = second * 60,
							  hour = minute * 60,
							  day = hour * 24;
					  
						let offer = "july 20, 2021 11:53:00",
							countDown = new Date(offer).getTime(),
							x = setInterval(function() {    
					  
							  let now = new Date().getTime(),
								  distance = countDown - now;
					  
							  document.getElementById("days").innerText = Math.floor(distance / (day)),
								document.getElementById("hours").innerText = Math.floor((distance % (day)) / (hour)),
								document.getElementById("minutes").innerText = Math.floor((distance % (hour)) / (minute)),
								document.getElementById("seconds").innerText = Math.floor((distance % (minute)) / second);
					  
							  //do something later when date is reached
							  if (distance < 0) {
								let headline = document.getElementById("headline"),
									countdown = document.getElementById("countdown");
					  
								headline.innerText = "Offer is End!";
								countdown.style.display = "none";
					  
								clearInterval(x);
							  }
							  //seconds
							}, 0)
						}());
				}
			},
			/*-----------------------------------------------------
				Product remove button
			-----------------------------------------------------*/
			product_remove: function () {
				if($('.e-remove-product').length > 0){
					$(document).on('click', '.e-remove-product', function () {
						$(this).parents("tr").hide('500');
					});
				}
			},
			

		};

		Ecommerce.init();

})(jQuery);

/*-----------------------------------------------------
	Contact Form Submission
-----------------------------------------------------*/
// Contact Form Submission
function checkRequire(formId , targetResp){
    targetResp.html('');
    var email = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/;
    var url = /(http|ftp|https):\/\/[\w-]+(\.[\w-]+)+([\w.,@?^=%&amp;:\/~+#-]*[\w@?^=%&amp;\/~+#-])?/;
    var image = /\.(jpe?g|gif|png|PNG|JPE?G)$/;
    var mobile = /^[\s()+-]*([0-9][\s()+-]*){6,20}$/;
    var facebook = /^(https?:\/\/)?(www\.)?facebook.com\/[a-zA-Z0-9(\.\?)?]/;
    var twitter = /^(https?:\/\/)?(www\.)?twitter.com\/[a-zA-Z0-9(\.\?)?]/;
    var google_plus = /^(https?:\/\/)?(www\.)?plus.google.com\/[a-zA-Z0-9(\.\?)?]/;
    var check = 0;
    $('#er_msg').remove();
    var target = (typeof formId === 'object')? $(formId):$('#'+formId);
    target.find('input , textarea , select').each(function(){
        if($(this).hasClass('require')){
            if($(this).val().trim()){
                $(this).removeClass('error');
                $(this).parent('div').removeClass('form_error');
            }
            if($(this).val().trim() === ''){
                check = 1;
                $(this).focus();
                $(this).parent('div').addClass('form_error');
                targetResp.html('فیلد های لازم را پر کنید.');
                $(this).addClass('error');
                return false;
            }
        }
        if($(this).val().trim()){
            var valid = $(this).attr('data-valid');
            if(typeof valid != 'undefined'){
                if(!eval(valid).test($(this).val().trim())){
                    $(this).addClass('error');
                    $(this).focus();
                    check = 1;
                    targetResp.html($(this).attr('data-error'));
                    return false;
                }else{
                    $(this).removeClass('error');
                }
            }
        }
    });
    return check;
}
$(".submitForm").on('click', function() {
    var _this = $(this);
    var targetForm = _this.closest('form');
    var errroTarget = targetForm.find('.response');
    var check = checkRequire(targetForm , errroTarget);
    
    if(check === 0){
       var formDetail = new FormData(targetForm[0]);
        formDetail.append('form_type' , _this.attr('form-type'));
        $.ajax({
            method : 'post',
            url : 'ajaxmail.php',
            data:formDetail,
            cache:false,
            contentType: false,
            processData: false
        }).done(function(r){
            let response = JSON.parse(r);
            if(response.res){
                targetForm.find('input').val('');
                targetForm.find('textarea').val('');
                errroTarget.html('<p style="color:green;">Mail has been sent successfully.</p>');
            }else{
                errroTarget.html('<p style="color:red;">Something went wrong please try again latter.</p>');
            }
        });
    }
});
