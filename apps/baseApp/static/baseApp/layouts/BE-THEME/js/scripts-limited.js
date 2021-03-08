(function($) {


    "use strict";


    /* ---------------------------------------------------------------------------
	 * Global vars
	 * --------------------------------------------------------------------------- */

    var scrollticker;	// Scroll Timer | don't need to set this in every scroll

    var rtl 			= $('body').hasClass('rtl');
    var simple			= $('body').hasClass('style-simple');

    var top_bar_top 	= '61px';
    var header_H 		= 0;

    var pretty 			= false;
	 var mobile_init_W 	=  1240;


	/* ---------------------------------------------------------------------------
	 * WP Gallery
	 * --------------------------------------------------------------------------- */
	jQuery('.gallery-icon > a').wrap('<div class="image_frame scale-with-grid"><div class="image_wrapper"></div></div>').prepend('<div class="mask"></div>').attr('rel', 'prettyphoto[gallery]').attr('data-rel', 'prettyphoto[gallery]').children('img').css('height', 'auto').css('width', '100%');

	/* ---------------------------------------------------------------------------
	 * PrettyPhoto
	 * --------------------------------------------------------------------------- */
	if ((typeof(window.mfn_prettyphoto) !== 'undefined' && !window.mfn_prettyphoto.disable)) {
		jQuery('a[rel^="prettyphoto"],a.woocommerce-main-image.zoom, .prettyphoto, a[data-rel^="prettyPhoto[product-gallery]"]').prettyPhoto({
			default_width: window.mfn_prettyphoto.width ? window.mfn_prettyphoto.width : 500,
			default_height: window.mfn_prettyphoto.height ? window.mfn_prettyphoto.height : 344,
			show_title: false,
			deeplinking: false,
			social_tools: false
		});
	}


	/* ---------------------------------------------------------------------------
	 * Black & White
	 * --------------------------------------------------------------------------- */
	jQuery('.greyscale .image_wrapper > a, .greyscale .client_wrapper .gs-wrapper, .greyscale.portfolio-photo a').has('img').BlackAndWhite({
		hoverEffect: true,
		intensity: 1 // opacity: 0, 0.1, ... 1
	});


	/* ---------------------------------------------------------------------------
	 * IE fixes
	 * --------------------------------------------------------------------------- */
	function checkIE() {
		// IE 9
		var ua = window.navigator.userAgent;
		var msie = ua.indexOf("MSIE ");
		if (msie > 0 && parseInt(ua.substring(msie + 5, ua.indexOf(".", msie))) == 9) {
			jQuery("body").addClass("ie");
		}
	}
	checkIE();

	/* ---------------------------------------------------------------------------
	 * Parallax Backgrounds
	 * --------------------------------------------------------------------------- */
	var ua = navigator.userAgent,
		isMobileWebkit = /WebKit/.test(ua) && /Mobile/.test(ua);
	if (!isMobileWebkit && jQuery(window).width() >= 768) {
		$.stellar({
			horizontalScrolling: false,
			responsive: true
		});
	}

	/* ---------------------------------------------------------------------------
	 * Ajax | Load More
	 * --------------------------------------------------------------------------- */
	jQuery('.pager_load_more').click(function(e) {
		e.preventDefault();
		var el = jQuery(this);
		var pager = el.closest('.pager_lm');
		var href = el.attr('href');
		// index | for many items on the page
		var index = jQuery('.lm_wrapper').index(el.closest('.isotope_wrapper').find('.lm_wrapper'));
		el.fadeOut(50);
		pager.addClass('loading');
		$.get(href, function(data) {
			// content
			var content = jQuery('.lm_wrapper:eq(' + index + ')', data).wrapInner('').html();
			if (jQuery('.lm_wrapper:eq(' + index + ')').hasClass('isotope')) {
				// isotope
				jQuery('.lm_wrapper:eq(' + index + ')').append(jQuery(content)).isotope('reloadItems').isotope({
					sortBy: 'original-order'
				});
			} else {
				// default
				jQuery(content).hide().appendTo('.lm_wrapper:eq(' + index + ')').fadeIn(1000);
			}
			// next page link
			href = jQuery('.pager_load_more:eq(' + index + ')', data).attr('href');
			pager.removeClass('loading');
			if (href) {
				el.fadeIn();
				el.attr('href', href);
			}
			// refresh some staff -------------------------------
			mfn_jPlayer();
			iframesHeight();
			mfn_sidebar();
			// isotope fix: second resize


				jQuery('.lm_wrapper.isotope').imagesLoaded().progress( function() {
					jQuery('.lm_wrapper.isotope').isotope('layout');
				});

//				setTimeout(function(){
//					$('.lm_wrapper.isotope').isotope( 'layout');
//				},1000);

		});
	});

	/* ---------------------------------------------------------------------------
	 * Blog & Portfolio filters
	 * --------------------------------------------------------------------------- */
	jQuery('.filters_buttons .open').click(function(e) {
		e.preventDefault();
		var type = jQuery(this).closest('li').attr('class');
		jQuery('.filters_wrapper').show(200);
		jQuery('.filters_wrapper ul.' + type).show(200);
		jQuery('.filters_wrapper ul:not(.' + type + ')').hide();
	});
	jQuery('.filters_wrapper .close a').click(function(e) {
		e.preventDefault();
		jQuery('.filters_wrapper').hide(200);
	});

	/* ---------------------------------------------------------------------------
	 * Portfolio List - next/prev buttons
	 * --------------------------------------------------------------------------- */
	jQuery('.portfolio_next_js').click(function(e) {
		e.preventDefault();
		var stickyH = jQuery('#Top_bar.is-sticky').innerHeight();
		var item = jQuery(this).closest('.portfolio-item').next();
		if (item.length) {
			jQuery('html, body').animate({
				scrollTop: item.offset().top - stickyH
			}, 500);
		}
	});
	jQuery('.portfolio_prev_js').click(function(e) {
		e.preventDefault();
		var stickyH = jQuery('#Top_bar.is-sticky').innerHeight();
		var item = jQuery(this).closest('.portfolio-item').prev();
		if (item.length) {
			jQuery('html, body').animate({
				scrollTop: item.offset().top - stickyH
			}, 500);
		}
	});

	/* ---------------------------------------------------------------------------
	 * Smooth scroll
	 * --------------------------------------------------------------------------- */
	jQuery('li.scroll > a, a.scroll').click(function() {
		var url = jQuery(this).attr('href');
		var hash = '#' + url.split('#')[1];
		var stickyH = jQuery('.sticky-header #Top_bar').innerHeight();
		var tabsHeaderH = jQuery(hash).siblings('.ui-tabs-nav').innerHeight();
		if (hash && jQuery(hash).length) {
			jQuery('html, body').animate({
				scrollTop: jQuery(hash).offset().top - stickyH - tabsHeaderH
			}, 500);
		}
	});


	/* ---------------------------------------------------------------------------
	 * Section navigation
	 * --------------------------------------------------------------------------- */
	jQuery('.section .section-nav').click(function() {
		var el = jQuery(this);
		var section = el.closest('.section');
		if (el.hasClass('prev')) {
			// Previous Section -------------
			if (section.prev().length) {
				jQuery('html, body').animate({
					scrollTop: section.prev().offset().top
				}, 500);
			}
		} else {
			// Next Section -----------------
			if (section.next().length) {
				jQuery('html, body').animate({
					scrollTop: section.next().offset().top
				}, 500);
			}
		}
	});


	/* ---------------------------------------------------------------------------
	 * Debouncedresize
	 * --------------------------------------------------------------------------- */
	jQuery(window).bind("debouncedresize", function() {
		iframesHeight();
		jQuery('.masonry.isotope,.isotope').isotope();
		// carouFredSel wrapper Height set
		mfn_carouFredSel_height();
		// Sidebar Height
		mfn_sidebar();
		// Sliding Footer | Height
		mfn_footer();
		// Header Width
		mfn_header();
		// Full Screen Section
		mfn_sectionH();
		// Full Screen Intro
			mfn_introH();

		// niceScroll | Padding right fix for short content
		niceScrollFix();
	});

	/* ---------------------------------------------------------------------------
	 * Isotope
	 * --------------------------------------------------------------------------- */
	// Isotope | Fiters
	function isotopeFilter(domEl, isoWrapper) {
		var filter = domEl.attr('data-rel');
		isoWrapper.isotope({
			filter: filter
		});
	}
	// Isotope | Fiters | Click
	jQuery('.isotope-filters .filters_wrapper').find('li:not(.close) a').click(function(e) {
		e.preventDefault();
		var filters = jQuery(this).closest('.isotope-filters');
		var parent = filters.attr('data-parent');
		if (parent) {
			parent = filters.closest('.' + parent);
			var isoWrapper = parent.find('.isotope').first()
		} else {
			var isoWrapper = jQuery('.isotope');
		}
		filters.find('li').removeClass('current-cat');
		jQuery(this).closest('li').addClass('current-cat');
		isotopeFilter(jQuery(this), isoWrapper);
	});
	// Isotope | Fiters | Reset
	jQuery('.isotope-filters .filters_buttons').find('li.reset a').click(function(e) {
		e.preventDefault();
		jQuery('.isotope-filters .filters_wrapper').find('li').removeClass('current-cat');
		isotopeFilter(jQuery(this), jQuery('.isotope'));
	});
	// carouFredSel wrapper | Height
	mfn_carouFredSel_height();
	// Sidebar | Height
	mfn_sidebar();
	// Sliding Footer | Height
	mfn_footer();
	// Header | Width
	mfn_header();
	// Full Screen Section
	mfn_sectionH();
	// Navigation | Hash
	hashNav();
	// Equal Columns | Height
	//mfn_equalH();
});


/* --------------------------------------------------------------------------------------------------------------------------
 * jQuery(window).load
 * ----------------------------------------------------------------------------------------------------------------------- */
jQuery(window).load(function() {

	/* ---------------------------------------------------------------------------
	 * Isotope
	 * --------------------------------------------------------------------------- */
	// Portfolio - Isotope
	jQuery('.portfolio_wrapper  .isotope:not(.masonry-flat)').isotope({
		itemSelector: '.portfolio-item',
		layoutMode: 'fitRows'
	});
	// Portfolio - Masonry Flat
	jQuery('.portfolio_wrapper .masonry-flat').isotope({
		itemSelector: '.portfolio-item',
		masonry: {
			columnWidth: 1
		}
	});
	// Blog & Portfolio - Masonry
	jQuery('.masonry.isotope').isotope({
		itemSelector: '.isotope-item',
		layoutMode: 'masonry',
	});
	// Blog & Portfolio - Masonry
		$('.isotope.masonry, .isotope.masonry-hover, .isotope.masonry-minimal').isotope({
			itemSelector	: '.isotope-item',
			layoutMode		: 'masonry',
		})
});



jQuery(window).load(function(){
	jQuery('.isotope').isotope('layout');
	/* ---------------------------------------------------------------------------
	 * TwentyTwenty [ before_after ]
	 * --------------------------------------------------------------------------- */
	jQuery('.before_after.twentytwenty-container').twentytwenty();
});
