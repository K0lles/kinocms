const addMoreButtons = $('#add-more')
const photoFormList = $('#photo-form-list');
const cancelButton = $('.cancel-button');

$(document).on("click", "button.cancel-button" , function() {
        $(this).parent().remove();
});




addMoreButtons.click(function (e) {
    e.preventDefault();
    let totalForms = parseInt($('#id_form-TOTAL_FORMS').val());


    let emptyRow = $('#empty-form').clone();

    emptyRow.find('#id_form-__prefix__-photo').attr('id', `id_form-${totalForms}-photo`)
        .attr('name', `form-${totalForms}-photo`);
    emptyRow.find('label').attr('for', `id_form-${totalForms}-photo`);
    emptyRow.find('#image-preview').attr('id', `id_form-${totalForms}-photo-preview`)
    emptyRow.attr('id', `id_form-${totalForms}-photo`);
    emptyRow.attr('class', 'photo-form flex-column')
    emptyRow.css('display', 'inline-block');
    photoFormList.append(emptyRow)
    $('#id_form-TOTAL_FORMS').val(totalForms + 1);
});

function loadFile(event, id) {
    event.preventDefault();

    let image = $(`#${id}-preview`);
    image.attr('src', URL.createObjectURL(event.target.files[0]));
    image.onload = function() {
        URL.revokeObjectURL(image.src);
    };
}
