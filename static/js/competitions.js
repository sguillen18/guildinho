$(document).ready(function() {
    // Fetch and populate competitions
    $.getJSON('/competitions', function(data) {
        var options = '';
        for (var i = 0; i < data.length; i++) {
            var comp = data[i];
            var value = comp.competition_id + ',' + comp.season_id; // Combine IDs with comma delimiter
            options += '<option value="' + value + '">' + comp.competition_name + ' - ' + comp.season_name + '</option>';
        }
        $('#comp_id').html(options);
    });
});