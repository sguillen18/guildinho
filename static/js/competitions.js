$(document).ready(function() {
    // Fetch and populate competitions
    $.getJSON('/competitions', function(data) {
        var options = '';
        for (var i = 0; i < data.length; i++) {
            var comp = data[i];
            options += '<option value="' + comp.competition_id + '">' + comp.competition_name + ' - ' + comp.season_name + '</option>';
        }
        $('#comp_id').html(options);
    });
});