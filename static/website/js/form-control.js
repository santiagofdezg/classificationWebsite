$('#one').change(function() {
    $('#two').prop('disabled', true);
    if ($(this).val() == 'car') {
        $('#two').prop('disabled', false);
    }
});