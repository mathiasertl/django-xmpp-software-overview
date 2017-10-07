/**
 * Bare function to detect the operating system platform.
 *
 * Will return either 'linux', 'android', 'win', 'osx', 'ios' or an empty string, in which
 * case detection failed.
 */
function xmpp_software_overview_detect_platform() {
    /** 
     * According to https://github.com/bestiejs/platform.js/blob/1.3.4/platform.js#L1141:
     *
     * Common values include:
     * "Windows", "Windows Server 2008 R2 / 7", "Windows Server 2008 / Vista",
     * "Windows XP", "OS X", "Ubuntu", "Debian", "Fedora", "Red Hat", "SuSE",
     * "Android", "iOS" and "Windows Phone"
     */

    let family = platform.os.family.toLowerCase();

    if (/^android/i.test(family)) {
        return 'android';
    } else if (family === 'ios') {
        return 'ios';
    } else if (/^(linux|ubuntu|debian|fedora|red hat|suse)/i.test(family)) {
        return 'linux';
    } else if (/^windows/i.test(family)) {
        return 'win';
    } else if (/^osx/i.test(family)) {
        return 'osx';
    }
    return 'any';
};

function xmpp_software_overview_show_os_specific(platform) {
    if (typeof platform === 'undefined') {
        // first get any os=value query parameter (...?os=linux)
        var url = new URL(document.location);
        var platform = url.searchParams.get('os');

        // If nothing was requested via query string, try to detect platform
        if (! platform) {
            var platform = xmpp_software_overview_detect_platform();
        }

        if (typeof platform !== 'undefined') {
            $('select#os-selector').val(platform);
        }
    }   

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
    xmpp_software_overview_show_os_specific();

    $('select#os-selector').change(function(e) {
        var selected = $(e.target).val();
        xmpp_software_overview_show_os_specific(selected);

        var url = new URL(document.location);
        url.searchParams.set('os', selected);
        history.pushState({}, 'foo', url.href);
    });
});
