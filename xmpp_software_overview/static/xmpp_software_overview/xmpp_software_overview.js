$(document).ready(function() {
    $('select#os-selector').change(function(e) {
        var selected = $(e.target).val();
        show_os_specific(selected);

        var url = new URL(document.location);
        url.searchParams.set('os', selected);
        history.pushState({}, 'foo', url.href);
    });
});
