const addMoreButtons = $('#add-more')
const photoFormList = $('#photo-form-list');

$(document).on("click", ".cancel-button" , function() {
    $(this).parent().parent().remove();
});

$(document).on('click', '.cancel-button-checkbox', function () {
    $(this).parent().parent().css('display', 'none');
});

addMoreButtons.click(function (e) {
    e.preventDefault();
    let totalForms = parseInt($('#id_form-TOTAL_FORMS').val());


    let emptyRow = $('#empty-form').clone();

    emptyRow.find('#id_form-__prefix__-photo').attr('id', `id_form-${totalForms}-photo`)
        .attr('name', `form-${totalForms}-photo`);
    emptyRow.find('label').attr('for', `id_form-${totalForms}-photo`);
    emptyRow.find('#image-preview').attr('id', `id_form-${totalForms}-photo-preview`);
    emptyRow.attr('id', `id_form-${totalForms}-photo`);
    emptyRow.attr('class', 'photo-form flex-column');
    emptyRow.css('display', 'inline-block');
    photoFormList.append(emptyRow);
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

function hidePhoto(event, element) {
    console.log('hello you have triggered me!');
    $(element).parent().parent().css('display', 'none');
    let photoID = ($(element).parent().parent().attr('id')).replace('-photo', '-DELETE');
    console.log(photoID);
    $(`#${photoID}`).prop('checked', true);
    console.log($(`#${photoID}`));
}

function removeFile(image) {

    let inputFieldID = image.id.replace("-delete", "");
    let otherInputImage = document.getElementById(inputFieldID);
    otherInputImage.value = "";
    $(`#${inputFieldID}-preview`).attr('src', '/static/admin_cms/logos/empty-photo.png');
}
