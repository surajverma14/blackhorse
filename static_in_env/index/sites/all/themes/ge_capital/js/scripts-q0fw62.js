/*******************************************************************************
**
** GE Digital Industrial Scripts
**
*******************************************************************************/
(function ($, Drupal) {
	Drupal.behaviors.ge_capital = {
		attach: function (context, settings) {
			var baseUrl = settings.path.baseUrl;
			var themeUrl = baseUrl+"sites/all/themes/ge_capital/";
            var geCapital_features = {
            initialization: function() {
              geCapital_features.initGeneralFeatures();
              geCapital_features.initMapMarkers();
              geCapital_features.initSectionSpacing();
            }, 
        initGeneralFeatures: function() {
		  var iv = null;

		// Mobile menu
		$('.side-menu-trigger, .sidebar-menu--trigger').click(function() {
			if ($('.sidebar-menu').hasClass('is-active')) {
				$('.sidebar-menu').removeClass('is-active');
			} else {
				$('.sidebar-menu').addClass('is-active');
			}
		});

		$('.sidebar-menu__item--has-children').click(function(e) {
			e.stopPropagation();
			$('.sidebar-menu__title').text($(e.currentTarget).children('.sidebar-menu__link').text());
			$(e.currentTarget).children('.sidebar-menu__list').addClass('is-active');
		});

		$('.sidebar-menu__item--back').click(function(e) {
			e.preventDefault();
			e.stopPropagation();
			var currentElement = $(e.target).closest('.sidebar-menu__list')
			currentElement.removeClass('is-active');
			var parentElement = currentElement.parent().closest('.sidebar-menu__list')
			if (!parentElement.siblings().hasClass('sidebar-menu__header')) {
				$('.sidebar-menu__title').text(parentElement.siblings().text());
			} else {
				$('.sidebar-menu__title').text('Explore');
			}
		});

		// Mega Menu Dropdown
		$('.mega-dropdown-menu .menu-content-header .nav-tabs li a').mouseover( function(){
			$(this).click();
		});

		// Functions to show the dropdown menu
		$('.dropdown').hover(function() {
			$('.dropdown-menu', this).stop(true, true).fadeIn('fast');
			$(this).toggleClass('open');
		}, function() {
			$('.dropdown-menu', this).stop(true, true).fadeOut('fast');
			$(this).toggleClass('open');
		});

		// Functions to show the dropdown menu
		$('.dropdown').focusin(function(e) {
			if ($(e.currentTarget).hasClass('open') === false) {
				$('.dropdown-menu', this).stop(true, true).fadeIn('fast');
				$(this).toggleClass('open');
			}
		});
		
		$("#password-str").hide();
		$("#password1").keyup(function() {
			$("#password-str").fadeIn();
			  passwordStrength(jQuery(this).val());
		});
		
		  // Masonry script
          $(window).on('load', function () {
              $('.stack').masonry({
              });
          });
		  
          // map script
      $( "#regions" ).accordion({
        header: "span.region",
        heightStyle: "content",
        active: true,
        collapsible: true,
        event: "mouseover"
        }).on('mouseleave', function () {
          $(this).accordion("option", "active", false);
        });

            // Search script
            // Scripts for Show/Hide of Search Bar upon clicking the search Icon in the Main Navigation
			var $searchlink = $('#search-icon');
			var $searchbar = $('.header-searchBlock');
			var $closesearchbar = $('.close-search');
			var $width = $(window).width();

			$searchbar.hide();

			$searchlink.on('click', function() {
				$searchbar.slideToggle('show');
			});

			$closesearchbar.on('click', function() {
				$searchbar.slideUp();
			});
			window.onscroll = function() {addhomenav()};
		
			function addhomenav() {
				if (document.body.scrollTop > 120 || document.documentElement.scrollTop > 120) {
					$(".home-header-wrapper").addClass("transparent-reverse");
					$(".home-header-wrapper .navigation-wrapper").addClass("transparent-reverse");
					$(".home-header-searchBlock").addClass("transparent-reverse");
					$(".header-wrapper.transparent-reverse").removeClass("home-header-wrapper");
					$(".header-searchBlock").removeClass("home-header-searchBlock");
					
				} 
				if($(window).scrollTop() == 0) {
					$(".header-wrapper.transparent-reverse").addClass("home-header-wrapper");
					$(".header-searchBlock.transparent-reverse").addClass("home-header-searchBlock");
					$(".home-header-wrapper").removeClass("transparent-reverse");
					$(".home-header-wrapper .navigation-wrapper").removeClass("transparent-reverse");
					$(".home-header-searchBlock").removeClass("transparent-reverse");
				}
			}	
		
		// Make sure footer is showing copyright year
		$('.copyright-bottom').text($('.copyright-bottom').text().replace('©', '© ' + (new Date).getFullYear()));

		//Press Release
		$('#products .item').addClass('list-group-item');
		$('.read-more').hide();
		$('.glyphicon-th').css('color', '#d3d3d3');

		//$('.form-select').selectpicker();

		$('#list').click(function (event) {
			event.preventDefault();
			$('#products .item').removeClass('grid-group-item');
			$('#products .item').addClass('list-group-item');
			$('.read-more').hide();
			$('.glyphicon-th-list').css('color', '#595959');
			$('.glyphicon-th').css('color', '#d3d3d3');

			//Bind to Load and Resize
			$(window).bind("load resize", function() {
				if ($(window).width() > 991){
					$('.list-group').css('margin-left', '-15px');
				} else {
					$('.list-group').css('margin-left', '-75px');
				}
			}).resize();
		});
		
		$('#grid').click(function (event) {
			event.preventDefault();
			$('#products .item').removeClass('list-group-item');
			$('#products .item').addClass('grid-group-item');
			$('.read-more').show();
			$('.list-group').css('margin-left', '-35px');
			$('.glyphicon-th-list').css('color', '#d3d3d3');
			$('.glyphicon-th').css('color', '#595959');
		});

		//Filter By Date
	/*	$('.press-release .select-wrapper select').unbind().change(function() {
			$('.press-release .row.heading .form-actions button.js-form-submit').click();
		});

		loadmore(); //function
		IsVisible(); */// Animation function call

		//Load More Function
		$('section.portfolio-block div.portfolio-item-wrapper').slice(0, 4).show();
		$('button#loadmore').on('click',function(e) {
			e.preventDefault();
			$('section.portfolio-block div.portfolio-item-wrapper:hidden').slice(0, 3).slideDown(750);
			imgScaling(".portfolio-block .portfolio-item-wrapper .halfwidth-img-wrapper", "img.halfwidth-bg");
			if($('section.portfolio-block div.portfolio-item-wrapper:hidden').length == 0) {
				$('section.portfolio-block > div.container:last-child').fadeOut('slow');
			}
		});

		//ReadMore / ReadLess
		var $parentElem = $('.portfolio-item-wrapper .content-wrapper');
		$parentElem.each(function() {
			$(this).find('article.article-wrapper').expander({
				slicePoint: 250,
				expandText: 'Show More',
				expandPrefix: '',
				userCollapseText: 'Show Less',
				userCollapsePrefix: '',
				expandSpeed: 400,
				collapseSpeed: 400,
				expandEffect: 'slideDown',
				collapseEffect: 'slideUp',
				moreClass: 'read-more-wrapper',
				lessClass: 'read-less-wrapper'
			});

			$(this).find('article.article-wrapper a').addClass("link-custom sliding-u-l-r");
			$(this).find('article.article-wrapper > .summary span').before(" [...]");
		});
	

		$('#loadmore').unbind().click(function() { 
			$('.press-release #products .item:hidden').slice(0, 1).slideDown();
			if ($('.press-release #products .item:hidden').length == 0) { 
				$('#loadmore').fadeOut('slow');
			}
		});

		//Bind to Load and Resize
		$(window).bind("load resize", function() {
			imgScaling(".hero-block", ".hero-bg"); 
			imgScaling(".content-block", "img.banner-bg")
			imgScaling(".content-half-image-filled-section .background-wrapper", ".banner-bg"); 
			imgScaling(".content-half-image-filled-section .col-override", ".banner-bg");  
			imgScaling(".content-one-two-cards-section .box-content", "img.box-bg");
			imgScaling(".content-halfwidth-image-section .halfwidth-image-wrapper", "img.banner-bg");
			imgScaling(".content-cards-with-image-section .card-wrapper .img-wrapper", "img.card-thumbnail");
			imgScaling(".content-halfwidth-video-fit-section .video-wrapper", "img.video-thumbnail");
			imgScaling(".content-halfwidth-image-fit-section .image-wrapper", "img.image-thumbnail");
			imgScaling(".portfolio-block .portfolio-item-wrapper .halfwidth-img-wrapper", "img.halfwidth-bg");

			if(iv !== null) {
				window.clearTimeout(iv);
			}

			iv =  setTimeout(function() {
				if($(window).width() >= 752) {
					equalizeHeights($('#carousel-cards .cards-wrapper h4'));
					equalizeHeights($('#carousel-cards .cards-wrapper p'));

					equalizeHeights($('.content-cards-with-image-section .card-wrapper .content-wrapper h4'));
					equalizeHeights($('.content-cards-with-image-section .card-wrapper .content-wrapper p'));
				} else {
					$('#carousel-cards .cards-wrapper h4').removeAttr('style');
					$('#carousel-cards .cards-wrapper p').removeAttr('style');

					$('.content-cards-with-image-section .card-wrapper .content-wrapper h4').removeAttr('style');
					$('.content-cards-with-image-section .card-wrapper .content-wrapper p').removeAttr('style');
				}
			}, 120);
		}).resize();

/*		//Trigger on Scroll Function
		$(window).scroll(function(){
			IsVisible();
		});  */

		//Play/Stop Youtube video on Modal Open / Close
		var sitetypeHref = $('iframe.embed-responsive-item').attr('src');
		var sitetypeHrefAuto = sitetypeHref + "?autoplay=1"
		$('a[data-target="#customModal"]').click(function () {			
			$('iframe.embed-responsive-item').attr('src', sitetypeHrefAuto);
		});

		$("#customModal").on('hidden.bs.modal', function () {
			var iFrame = $(this).find("iframe");
			iFrame.attr("src", sitetypeHref);
		});

		//Bootstrap Nav Tab fix related to double tap issues on ios devices.
		$('.nav-tabs a').on("click touchend", function(){
			$(this).tab('show');
		});
	},
	initMapMarkers: function() {
		//Initialize Tooltip's Default Settings
		/** Map Names 
		** 1. image-map-world
		** 2. image-map-na 
		** 3. image-map-eu
		** 4. image-map-latam
		** 5. image-map-asia 
		**/

		$.tooltipster.setDefaults({ 
			interactive: true, 
			trackTooltip: true, 
			trackerInterval: 1, 
 			distance: 1, 
 			trigger: 'custom',
			triggerOpen: {
				click: true,
				tap: true,
				touchstart: true
			}, triggerClose: {
				click: true,
				tap: true,
				touchleave: true,
				scroll: true
			}
		});

		$('.custom-tooltip').tooltipster({
			functionBefore: function(instance, helper) {
				//Customize Tooltip's Look and Feel
				var $element=$(helper.origin),
					$title='<h5><strong>' + $element.data('title') + '</strong></h5>',
					$location='<h6>(' + $element.data('location') + ')</h6>',
					$description = '<ul class="description-list">',
					$tooltipContent;

				var initdescription= $element.data('description');
				var initiconsurl= $element.data('iconsurl');

				if(initdescription && initiconsurl) {
					var splitdescription= initdescription.split('|');
					var spliticonsurl = initiconsurl.split('|');
					var countarray = splitdescription.length || spliticonsurl;

					for (var i=0; i<=(countarray-1); i++) {
						$description += '<li style="background: url(' + spliticonsurl[i] + ') no-repeat left center">' + splitdescription[i] + '</li>'; 
					}

					$description += '</ul>';
				}

				$tooltipContent = '<div class="tooltip_container">';
					$tooltipContent += '<div class="tooltip_header-block">' + $title + $location + '</div>';
					$tooltipContent += '<div class="tooltip_content-block">' + $description +'</div>';
				$tooltipContent += '</div>';

				instance.content($tooltipContent);
			},
			functionReady: function(instance, helper){
				$('.tooltipster-base').css('height', ''); 

				var $element = $(helper.origin);
				var $buttonElement  = $('button[data-location="' + $element.data('location') + '"]');
				$buttonElement.addClass('active');

				//Adding Map Markers
				var leftpos = '';
				leftpos = parseInt($('.tooltipster-arrow')[0].style.left);
				$('.marker').remove();
				$('.tooltipster-base').append(
					$('<div class="marker hidden-xs"><img src="images/marker.png" class="icon-marker"></div>').css({
						position: 'absolute', 
						height: '40px', 
						top: '-55px', 
						left: (leftpos - 19)
					})
				);
			},
			functionAfter: function(instance, helper) {
				var $element = $(helper.origin);
				var $buttonElement  = $('button[data-location="' + $element.data('location') + '"]');
				$buttonElement.removeClass('active');
			},
			theme: ['tooltipster-shadow', 'tooltipster-shadow-customized'],
			multiple: true, 
			contentCloning: true, 
			contentAsHTML: true, 
			minWidth: 300,
			maxWidth: 300,
			side: ['bottom','bottom','bottom','bottom'],
		});

		$('img[usemap]').imageMap(); /** This script is used for the responsiveness of the area coordinates **/

		//Buttons Location Initialized functions
		$('.content-with-tabs-section .custom-tab-content .buttons-wrapper').addClass('showcontent');
		$('.content-with-tabs-section .custom-tab-content .buttons-wrapper button.custom-btn').addClass('showcontent');
		locationbutton_Trigger('.content-with-tabs-section .custom-tab-content .buttons-wrapper button.custom-btn');

		//Initialize the Markers per Region
		$('.custom-nav-tab li a').on('shown.bs.tab', function(event){
			var x = ''; 
			x = $(event.target).text().toLowerCase();
			var mapElement = $('.map-wrapper img');
			$('.custom-radio input:radio[name="optradio"]').prop('checked', false); //uncheck all radio button on resize

			if (x == "europe") {

				mapElement.attr('usemap','#image-map-eu');
				hotspots_Allocation(".custom-tab-content #panecontainer2");
				locationbutton_Display('button[data-region="Europe"]');

			} else if (x == "latin america") {

				mapElement.attr('usemap','#image-map-latam');
				hotspots_Allocation(".custom-tab-content #panecontainer3");
				locationbutton_Display('button[data-region="Latin America"]');

			} else if (x == "asia") {

				mapElement.attr('usemap','#image-map-asia');
				hotspots_Allocation(".custom-tab-content #panecontainer4");
				locationbutton_Display('button[data-region="Asia"]');

			} else if (x == "north america") {

				mapElement.attr('usemap','#image-map-na');
				hotspots_Allocation(".custom-tab-content #panecontainer1");
				locationbutton_Display('button[data-region="North America"]');

			} else {

				mapElement.attr('usemap','#image-map-world');
				hotspots_Allocation(".custom-tab-content #panecontainer0");
				locationbutton_Display('button.custom-btn');

			}

			$('img[usemap]').imageMap();
		});

	
		$(window).bind("load resize", function() {
			//Hotspots Plotting
			$('.custom-radio input:radio[name="optradio"]').prop('checked', false); //uncheck all radio button on resize
			hotspots_Allocation(".custom-tab-content .custom-pane");

			var activeTabNav = $('ul.custom-nav-tab > li.active > a').text();

			if (activeTabNav != 'All') { 
				locationbutton_Display('button[data-region="' + activeTabNav + '"]');
			} else {
				locationbutton_Display('button.custom-btn');
			}
			
			//extension to Responsive Tabs to put the buttons-wrapper always at the bottom of the radio buttons
			$('div.buttons-wrapper').appendTo('.custom-tab-content');
		}).resize();

		//Radio Buttons Sorting - Location Section
		/*** #panecontainer - this is the ID of the tab pane **/
		radiobutton_Toggle('#panecontainer1');
		radiobutton_Toggle('#panecontainer2');
		radiobutton_Toggle('#panecontainer3');
		radiobutton_Toggle('#panecontainer4');
	},
	initSectionSpacing: function() {
		var $section = $("main.main-content-wrapper > section.content-block");
		$.each($section, function(key, value) {
			var nextElement = $section[key+1];
			var prevElement = $section[key-1]; 

			if((typeof prevElement == 'undefined') && (
				$(value).hasClass('content-with-fullwidth-carousel-section') || 
				$(value).hasClass('content-fullwidth-image-section') || 
				$(value).hasClass('content-with-tabs-section') || 
				$(value).hasClass('content-half-image-filled-section') || 
				$(value).hasClass('full-block') || 
				$(value).hasClass('content-fullwidth-filled-section')
			)) {
				// Only add top margin
				$(value).css('padding-top', '80px');
			}

			if(
				$(nextElement).hasClass('content-with-fullwidth-carousel-section') || 
				$(nextElement).hasClass('content-fullwidth-image-section') || 
				$(nextElement).hasClass('content-with-tabs-section') || 
				$(nextElement).hasClass('content-half-image-filled-section') || 
				$(nextElement).hasClass('full-block') || 
				$(nextElement).hasClass('content-fullwidth-filled-section')
			){
				$(value).attr('data-paragraph-key', key);
				$('[data-paragraph-key="' + key +'"] .inner-line').css('padding-bottom', '80px');
			}

			// No more elements, this is the last element
			if(typeof nextElement == 'undefined'){
				$(value).attr('data-paragraph-key', key);
				$('[data-paragraph-key="' + key +'"] .inner-line').css('padding-bottom', '80px');
			}
		});
	}
};
$(function() {
	geCapital_features.initialization();
});
		}
	};
})(jQuery, Drupal);



function imgScaling(elem, img) {
	jQuery(elem).each(function() {
		var ratio_cont = jQuery(this).width()/jQuery(this).height();
		var $img = jQuery(this).find(img);
		var ratio_img = $img.width()/$img.height();
	
		if (ratio_cont > ratio_img) {
			$img.css({"width": "100%", "height": "auto"});
		} else if (ratio_cont < ratio_img) {
			$img.css({"width": "auto", "height": "100%"});
		}
	});
}

function equalizeHeights(selector) {
	var heights = new Array();

	// Loop to get all element heights
	jQuery(selector).each(function() {

		// Need to let sizes be whatever they want so no overflow on resize
		jQuery(this).css('min-height', '0');
		jQuery(this).css('max-height', 'none');
		jQuery(this).css('height', 'auto');

		// Then add size (no units) to array
 		heights.push(jQuery(this).height());
	});

	// Find max height of all elements
	var max = Math.max.apply( Math, heights );

	// Set all heights to max height
	jQuery(selector).each(function() {
		jQuery(this).css('height', max + 'px');
	});	
}

function hotspots_Allocation(elem) {
	var mapTag = '', 
		areaTag = '', 
		hotspot_coords = '';

	mapTag = jQuery(elem).find("map");
	areaTag = jQuery(mapTag).find("area");

	setTimeout(function() {
		jQuery(areaTag).each(function() {
			hotspot_coords = jQuery(this).attr("coords");
			var split_coords = hotspot_coords.split(',');
			var leftpost = parseInt(split_coords[0]) + 12;
			var bottompost = parseInt(split_coords[1])  + 5;
			jQuery(this).css({
				position: 'absolute',
				'z-index': 5, 
				width: 0,
				height: 0,
				border: '4px solid #C75332',
				'border-radius': '50%',
				left: leftpost,
				bottom: '-' + bottompost + 'px',
				display: 'block'
			});
		});
	}, 200);
}

function radiobutton_Toggle(ID) {
	jQuery(ID + ' .custom-radio input:radio[name="optradio"]').change(function() {
		if (jQuery(this).is(':checked')) {
			var radio_val = jQuery(this).val();

			locationbutton_Display('button[data-country="' + radio_val + '"]');

			jQuery('.custom-tab-content ' + ID + ' map > area').each(function() {
				var country = jQuery(this).data("country");
				jQuery(this).hide();
				if(radio_val == country) {
					jQuery(this).fadeIn('400');
				}
			});
      		}
	});
}

function locationbutton_Trigger(buttonElem) {
	jQuery(buttonElem).click(function() {
		var button_datalocation = '';
		var mapfinder = '';
		var areafinder = '';
		button_datalocation = jQuery(this).data('location');
		mapfinder = jQuery('.custom-pane.active').find('map');
		areafinder = mapfinder.find('area[data-location="' + button_datalocation + '"]');
		areafinder.trigger('click');
	});
}

function locationbutton_Display(buttonElem) {
	jQuery('.content-with-tabs-section .custom-tab-content .buttons-wrapper').removeClass('showcontent');
	jQuery('.content-with-tabs-section .custom-tab-content .buttons-wrapper').addClass('showcontent');
	jQuery('.content-with-tabs-section .custom-tab-content .buttons-wrapper button.custom-btn').removeClass('showcontent');
	jQuery('.content-with-tabs-section .custom-tab-content .buttons-wrapper ' + buttonElem).addClass('showcontent');
}

function loadmore(){
	jQuery(".press-release #products .item").slice(0, 2).show();
	if (jQuery('.press-release #products .item:hidden').length == 0) {
		jQuery('#loadmore').fadeOut('slow');
	} else { 
		jQuery('#loadmore').show();
	}
}

/*function IsVisible(){
	jQuery('.is-visible').each(function(){
		if (jQuery(this).visible(true)) {
		   	jQuery(this).addClass('visible-element');
		}
	})
} */



/* Password strength indicator */
function passwordStrength(password) {
	var desc = [{'width':'0px'}, {'width':'20%'}, {'width':'40%'}, {'width':'60%'}, {'width':'80%'}, {'width':'100%'}];
	var descClass = ['', 'progress-bar-danger', 'progress-bar-danger', 'progress-bar-warning', 'progress-bar-success', 'progress-bar-success'];
	var score = 0;

	//if password bigger than 6 give 1 point
	if (password.length > 6) score++;

	//if password has both lower and uppercase characters give 1 point	
	if ((password.match(/[a-z]/)) && (password.match(/[A-Z]/))) score++;

	//if password has at least one number give 1 point
	if (password.match(/d+/)) score++;

	//if password has at least one special caracther give 1 point
	if ( password.match(/.[!,@,#,$,%,^,&,*,?,_,~,-,(,)]/) )	score++;

	//if password bigger than 12 give another 1 point
	if (password.length > 10) score++;
	
	// display indicator
	jQuery("#pass_pstrength").removeClass(descClass[score-1]).addClass(descClass[score]).css(desc[score]);
	
	if (score==5){
		jQuery("#pass_pstrength span").text("VERY STRONG");
	}
	else if(score==4){
		jQuery("#pass_pstrength span").text("STRONG");
	}
	else if(score==3){
		jQuery("#pass_pstrength span").text("GOOD");
	}
	else if(score<3){
		jQuery("#pass_pstrength span").text("WEAK");
	}
	
}

		
// Forum start discussion 
jQuery('.topic-start-btn').on('click',function(){
  jQuery('.start-topic').slideUp('slow');
  jQuery('.start-discussion-wrapper').slideDown('slow');
})

jQuery('.post-options-btn').on('click',function(){
  jQuery('.start-topic').slideDown('slow');
  jQuery('.start-discussion-wrapper').slideUp('slow');
})

// newsroom template
if(jQuery('ul.filtering li.active #news_tab').length !=0) {
  jQuery('div #tab2').show();
  jQuery('div #tab1').hide();
  jQuery('div #tab3').hide();
}
   
jQuery('ul.filtering li a#news_tab').click(function () { 
  jQuery('div #tab2').show();
  jQuery('div #tab1').hide();
  jQuery('div #tab3').hide();
});

jQuery('ul.filtering li a#all_tab').click(function () { 
  jQuery('div #tab1').show();                                   
  jQuery('div #tab2').hide();
  jQuery('div #tab3').hide();
   
});

jQuery('ul.filtering li a#reports_tab').click(function () { 
  jQuery('div #tab3').show();
  jQuery('div #tab1').hide();
  jQuery('div #tab2').hide();
});

   



/* GECAS contact-us page*/
// changes for select dropdown
jQuery(document).on('change', '.div-toggle', function() {
  var target = jQuery(this).data('target');
  var show = jQuery("option:selected", this).data('show');
  jQuery(target).children().addClass('hide');
  jQuery(show).removeClass('hide');
});
jQuery(document).ready(function(){
	jQuery('.div-toggle').trigger('change');
});

//changes for accordian
	jQuery(".content .accordion span").hide();
  jQuery(".content .accordion .question").click(function(){
	if(false == jQuery(this).next().is(':visible'))
   {
    jQuery('.content .accordion span').slideUp(300);
		}
    jQuery(this).next().slideToggle(300);
    jQuery('.content .accordion.current').removeClass('current');
    jQuery(this).parent().addClass('current');
});


/*
 jQuery( "#solutions" ).accordion({
        header: "span.solution",
        heightStyle: "content",
        active: true,
        collapsible: true,
    });
    */
/* GECAS contact-us page ends here*/ 

/* Contact Us page dropdown changes starts here*/
jQuery(document).ready(function(){

 jQuery('#drop').change(function(){ 
 var myMod = this.selectedIndex ;
    if (myMod !== 0) {
        window.location.href = this.value;
    }
 })
});

 
/* Contact Us page dropdown changes ends here*/

/*    Evidon Script   */
(function ($) {
 $(document).ready(function() {
   $( ".evidon_cookie" ).click(function() {
     event.preventDefault();
     window.evidon.notice.showConsentTool();
   });
 });
}(jQuery));
/*    End Evidon Script   */