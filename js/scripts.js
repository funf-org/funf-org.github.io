$(function(){

/*-----------------------------------------------------------------------------------*/
/*	Slider - http://slidesjs.com/
/*-----------------------------------------------------------------------------------*/
				if ($().slides) {
			
					$('#slider').css({ display : 'block' });
						
					$("#slider").slides({
						preload: true,
						preloadImage: 'images/slider/loading.gif',
						play: 6000, //Auto play time. Set to 0 to stop auto rotate.
						width: 960,
						pause: 4500,
						slideSpeed: 1000, //Slide rotation speed.
						generatePagination: true,
						hoverPause: true,
						autoHeight: true
					});	
					
				}
				
/*-----------------------------------------------------------------------------------*/
/*	Fading Buttons - http://greg-j.com/2008/07/21/hover-fading-transition-with-jquery/
/*-----------------------------------------------------------------------------------*/		

	$('.fadeThis').append('<span class="hover"></span>').each(function () {
	  var $span = $('> span.hover', this).css('opacity', 0);
	  $(this).hover(function () {
	    $span.stop().fadeTo(500, 1);
	  }, function () {
	    $span.stop().fadeTo(500, 0);
	  });
	});
	
	
/*-----------------------------------------------------------------------------------*/
/*	Show/Hide Content - http://rpardz.com/blog/show-hide-content-jquery-tutorial/
/*-----------------------------------------------------------------------------------*/	
	
    $('.open-content').hide().before('<div class="container_12"><a href="#" id="toggle-content" class="button"><div id="expand-button" ></div></a></div><div id="toggle-top" style="width:100%"></div>');
	$('a#toggle-content').click(function() {
		$('.open-content').slideToggle(1000);
		return false;
	});
	
	
/*-----------------------------------------------------------------------------------*/
/*	FancyBox  - http://fancybox.net/
/*-----------------------------------------------------------------------------------*/	
			$("#various1").fancybox({
				'titlePosition'		: 'inside',
				'transitionIn'	: 'elastic',
				'transitionOut'	: 'elastic'
			});
			
			$("a.portfolio").fancybox();
			
			
/*-----------------------------------------------------------------------------------*/
/*	Mosaic Image Hover   - http://buildinternet.com/project/mosaic/1.0/
/*-----------------------------------------------------------------------------------*/	
				$('.circle').mosaic({
					opacity : 0.8	//Opacity for overlay (0-1)
				});
				
				$('.fade').mosaic();
				
/*-----------------------------------------------------------------------------------*/
/*	Add Class to Tag Cloud (WP prep work) - http://www.simplethemes.com/blog/entry/style-wordpress-tags/
/*-----------------------------------------------------------------------------------*/					
		$('p.tags a').wrap('<span class="jg-tags" />');


/*-----------------------------------------------------------------------------------*/
/*	Navigation Drop Down  - http://plugins.jquery.com/project/droppy
/*-----------------------------------------------------------------------------------*/		
		$('#nav').droppy({speed: 200});

	
});

/*-----------------------------------------------------------------------------------*/
/*	Clear input field on click
/*-----------------------------------------------------------------------------------*/	
			function clearText(field){
	
			if (field.defaultValue == field.value) field.value = '';
			else if (field.value == '') field.value = field.defaultValue;

			}
			