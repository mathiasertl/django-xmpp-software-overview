function xmpp_software_overview_show_os_specific(platform) {
    /* TODO: apply_attrs() is only used for columns, can we get that dynamically?  */

    if (platform == 'any' || typeof platform == 'undefined') {
        $('.os-specific').addClass('os-shown');
    } else {   
        $('.os-specific').removeClass('os-shown');
        $('.os-' + platform).addClass('os-shown');

        if (platform == 'android' || platform == 'ios') {
            $('.os-mobile').addClass('os-shown');
            $('#xep-header').attr('colspan', "9")
        } else {
            $('.os-mobile').removeClass('os-shown');
            $('#xep-header').attr('colspan', "7")
        }
    }
};

$(document).ready(function() {
    $('select#os-selector').change(function(e) {
        var selected = $(e.target).val();
        xmpp_software_overview_show_os_specific(selected);

        var url = new URL(document.location);
        url.searchParams.set('os', selected);
        history.pushState({}, 'foo', url.href);
    });
});
