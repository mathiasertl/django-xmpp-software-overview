function xmpp_software_overview_show_os_specific(platform) {
    /* TODO: apply_attrs() is only used for columns, can we get that dynamically?  */

    if (platform == 'any' || typeof platform == 'undefined') {
        $('[class^="os-"], [class*=" os-*]').show();
        apply_attrs('os-any');
    } else {   
        $('[class^="os-"], [class*=" os-*]').hide();
        $('.os-' + platform).show();
        apply_attrs('os-' + platform);

        if (platform == 'android' || platform == 'ios') {
            $('.os-mobile').show();
            apply_attrs('os-mobile');
        } else {
            apply_attrs('os-desktop');
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
