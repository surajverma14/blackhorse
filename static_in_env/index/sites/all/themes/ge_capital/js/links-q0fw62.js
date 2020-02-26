// JavaScript Document
(function ($) {
  //Internal or external links
  $(document).ready(function() {
    $(document).on("click", "a[href^=http], a[href^='//']", function(e){
        e.stopPropagation();
        // NEW - excluded domains list
        var excludes = [
        'www.gecapital.com',
		'gecapital.corporate.ge.com',
		'dev-gecapital.corporate.ge.com',
        'stage.gecapital.com'
        ];
        for(i=0; i<excludes.length; i++) {
          if(this.href.indexOf(excludes[i]) != -1) {
            return true; // continue each() with next link
          }
        }

        if(this.href.indexOf(location.hostname) == -1) {
          // attach a do-nothing event handler to ensure we can 'trigger' a click on this link
          $(this).attr({
            target: "_blank",
            title: "Opens in a new window",
            rel: "noopener noreferrer"
          });
        }
    });
  });
  //End Drupal behavior
}(jQuery));
