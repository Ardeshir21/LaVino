/*********************************************************************************

	Template Name: Photohub - Creative Photography Template
	Template URI: https://themeforest.net/user/plus-theme
	Description: Photohub is a awesome, creative, and unique phptography template which mekes you build a beautiful template easily
	Author: Plus-Theme
	Author URI: https://hastech.company
	Version: 1.0

	Note: This is active js. Plugins activation code here.

**********************************************************************************/


/*===============================================================================
			[ INDEX ]
=================================================================================

	Carousel
		Banner
		Testimonial
		Partners
		Sidebar post
		Onepage Multislider
		Onepage Singleslide
		Onepage another slide
	Lightgallery
		Portfolio zoom
		Portfoio gallery
		Multislide popup
	Pie Chart
		Default pie chart
		Onepage navigation pie chart
	ScrollUp
	Portfolio
	Fake Loader

=================================================================================
			[ END INDEX ]
================================================================================*/
/*====== Fake Loader ======*/

(function($) {
	'use strict';

	/*====== Carousel ======*/
	// Testimonial
	$('.testimonials').owlCarousel({
		items: 1,
		loop: true,
		autoplay: false,
		nav: false,
		dots: false,
		fade: true,
		animateOut: 'fadeOut'
	});

	// Partners
	$('.partners').owlCarousel({
		items: 5,
		loop: true,
		autoplay: false,
		nav: false,
		dots: false,
		responsive : {
            0 : {
                items:1,
            },
            576:{
                items:2,
            },
            768 : {
                items:3,
            },
            992 : {
                items:4,
            },
            1201 : {
                items:5,
            }
        }
	});

	// Sidebar post
	$('.sidebar-post-carousel-active').owlCarousel({
		items: 1,
		loop: true,
		autoplay: false,
		nav: false,
		dots: true
	});


	// Onepage Multislider
	$('.banner__inner.onepage--banner-multislide').owlCarousel({
		items: 3,
		loop: true,
		autoplay: false,
		dots: false,
		nav: true,
		navText: ['<span class="ti-angle-left"></span>','<span class="ti-angle-right"></span>'],
		margin: 2,
		responsive : {
            0 : {
                items:1,
            },
            576:{
                items:1,
            },
            768 : {
                items:2,
            },
            992 : {
                items:2,
            },
            1201 : {
                items:3,
            }
        }
	});


	// Onepage Singleslide
	$('.banner__inner.onepage--banner-singleslide').owlCarousel({
		items: 1,
		loop: true,
		autoplay: false,
		dots: false,
		nav: true,
		navText: ['<span class="ti-angle-left"></span>','<span class="ti-angle-right"></span>']
	});


	// Onepage another slide
	$('.banner__inner.onepage-another-slider').owlCarousel({
		items: 1,
		loop: true,
		autoplay: false,
		dots: false,
		nav: true,
		navText: ['<span class="ti-angle-left"></span>','<span class="ti-angle-right"></span>'],
		fade: true,
		animateOut: 'fadeOut'
	});






	/*====== Lightgallery ======*/
	// Portfolio zoom
	$('.portfolios').lightGallery({
		 selector: '.portfolio-zoom-trigger a',
		 thumbnail: false
	});

	// Portfoio gallery
	$('.gallery-portfolios').lightGallery({
		selector: '.portfolio__image',
		thumbnail: false
	});

	// Multislide popup
	$('.onepage--banner-multislide').lightGallery({
		selector: 'a.multislide-zoom-trigger',
		thumbnail: false
	});




	/*====== Pie Chart ======*/
	// Default pie chart
	$('.pies .pie-chart').waypoint(function(){

		$('.pies .pie-chart').easyPieChart({
			lineWidth: 2,
			trackColor: false,
			scaleLength: 0,
			rotate: -45,
			barColor: function(percent) {
			    var ctx = this.renderer.getCtx();
			    var canvas = this.renderer.getCanvas();
			    var gradient = ctx.createLinearGradient(0,120.000,canvas.width,0);
			        gradient.addColorStop(0, "#c60de1");
			        gradient.addColorStop(1, "#e51515");
			    return gradient;
			}
		});

	}, {
		triggerOnce: true,
		offset: 'bottom-in-view'
	});


	// Onepage navigation pie chart
	$('.op-pies .op-pie-chart').easyPieChart({
		lineWidth: 2,
		trackColor: false,
		scaleLength: 0,
		rotate: -45,
		barColor: function(percent) {
		    var ctx = this.renderer.getCtx();
		    var canvas = this.renderer.getCanvas();
		    var gradient = ctx.createLinearGradient(0,120.000,canvas.width,0);
		        gradient.addColorStop(0, "#c60de1");
		        gradient.addColorStop(1, "#e51515");
		    return gradient;
		}
	});



	/*====== ScrollUp ======*/
	$.scrollUp({
	    scrollText: '<span class="ti ti-angle-up"></span>',
	    easingType: 'linear',
	    scrollSpeed: 900,
	    animation: 'slide'
	});



	/*====== Portfolio ======*/
	// Fluid portfolio
	$('.portfolios.layout-2').imagesLoaded( function() {

       var $grid = $('.portfolios.layout-2').isotope({
           itemSelector: '.portfolio',
           layoutMode: 'fitRows'
       });

       var $buttonGroup = $('.portfolio-filter.layout-2').on( 'click', 'button', function() {
           var filterValue = $(this).attr('data-filter');
           $grid.isotope({ filter: filterValue });
           $buttonGroup.find('.is-checked').removeClass('is-checked');
           $(this).addClass('is-checked');
       });

   });

	// Container portfolio
	$('.gallery-portfolios').imagesLoaded( function() {

       var $grid = $('.gallery-portfolios').isotope({
           itemSelector: '.portfolio',
           percentPosition: true,
           masonry: {
               columnWidth: 1
           }
       });

       var $buttonGroup = $('.portfolio-filter.layout-3').on( 'click', 'button', function() {
           var filterValue = $(this).attr('data-filter');
           $grid.isotope({ filter: filterValue });
           $buttonGroup.find('.is-checked').removeClass('is-checked');
           $(this).addClass('is-checked');
       });

   });


	 // :: Preloader Active Code
	 var $window = $(window);
	 $window.on('DOMContentLoaded', function () {
	 		$('#preloader').fadeOut('slow', function () {
	 					$(this).remove();
	 			});
	 });

	// WOW initial
	new WOW().init();

})(jQuery);
