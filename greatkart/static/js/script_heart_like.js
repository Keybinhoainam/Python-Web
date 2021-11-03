jQuery(document).ready(function(){
        var isALike = false;
        jQuery("button").click(function() {
            isALike = !isALike;
            if (isALike) {
                
            }
            jQuery('img',this).toggle();
        });
    });