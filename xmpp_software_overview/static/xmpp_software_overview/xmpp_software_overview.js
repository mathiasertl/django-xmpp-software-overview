function xmpp_software_overview_show_os_specific(platform) {
    if (platform == 'any' || typeof platform == 'undefined') {
        $('.os-specific').addClass('os-shown');
    } else {   
        $('.os-specific').removeClass('os-shown');
        $('.os-' + platform).addClass('os-shown');

        if (platform == 'android' || platform == 'ios') {
            $('.os-mobile').addClass('os-shown');
        } else {
            $('.os-mobile').removeClass('os-shown');
        }
    }

    /* set colspan on the "XEPs" header cell */
    let colspan = $('.xmpp-software-overview-table tr.os-shown:first td:visible').length - 2;
    $('#xep-header').attr('colspan', colspan)
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
