const addMoreButtons = $('#add-more')
const photoFormList = $('#photo-form-list');

const mainBannerFormList = $('#main-banner-list');
const newsBannerFormList = $('#news-banner-list');
const addMoreMainBanner = $('#add-more-main_banner');
const addMoreNewsBanner = $('#add-more-news_banner');

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

addMoreMainBanner.click(function(e) {
    e.preventDefault();


    let totalForms = parseInt($('#id_form-TOTAL_FORMS').val());
    let emptyRow = $('#empty-form').clone();

    emptyRow.find('#id_form-__prefix__-photo').attr('id', `id_form-${totalForms}-photo`)
        .attr('name', `form-${totalForms}-photo`)
    emptyRow.find('#id_form-__prefix__-url').attr('id', `id_form-${totalForms}-url`)
        .attr('name', `form-${totalForms}-url`);
    emptyRow.find('#id_form-__prefix__-text').attr('id', `id_form-${totalForms}-text`)
        .attr('name', `form-${totalForms}-text`);
    emptyRow.attr('id', `id_form-${totalForms}-banner`);
    emptyRow.find('#image-preview').attr('id', `id_form-${totalForms}-photo-preview`);
    emptyRow.attr('class', 'flex-column');
    emptyRow.css('display', 'inline-block');
    mainBannerFormList.append(emptyRow);
    $('#id_form-TOTAL_FORMS').val(totalForms + 1);
})


addMoreNewsBanner.click(function(e) {
    e.preventDefault();

    let totalForms = parseInt($('#id_news-TOTAL_FORMS').val());
    let emptyRow = $('#empty-news-form').clone();

    emptyRow.find('#id_news-__prefix__-photo').attr('id', `id_news-${totalForms}-photo`)
        .attr('name', `news-${totalForms}-photo`)
    emptyRow.find('#id_news-__prefix__-url').attr('id', `id_news-${totalForms}-url`)
        .attr('name', `news-${totalForms}-url`);
    emptyRow.attr('id', `id_news-${totalForms}-banner`);
    emptyRow.find('#image-preview').attr('id', `id_news-${totalForms}-photo-preview`);
    emptyRow.attr('class', 'flex-column');
    emptyRow.css('display', 'inline-block');
    newsBannerFormList.append(emptyRow);
    $('#id_news-TOTAL_FORMS').val(totalForms + 1);
})

function loadFile(event, id) {
    event.preventDefault();

    let image = $(`#${id}-preview`);
    image.attr('src', URL.createObjectURL(event.target.files[0]));
    image.onload = function() {
        URL.revokeObjectURL(image.src);
    };
}

// function hideMainBanner(event, element) {
//     $(element).parent().parent().css('display', 'none');
//     let photoID = ($(element).parent().parent().attr('id')).replace('-photo', '-DELETE');
//     $(`#${photoID}`).prop('checked', true);
// }

function hidePhoto(event, element) {
    $(element).parent().parent().css('display', 'none');
    let photoID = ($(element).parent().parent().attr('id')).replace('-photo', '-DELETE');
    $(`#${photoID}`).prop('checked', true);
}

function removeFile(image) {

    let inputFieldID = image.id.replace("-delete", "");
    let otherInputImage = document.getElementById(inputFieldID);
    otherInputImage.value = "";
    $(`#${inputFieldID}-preview`).attr('src', '/static/admin_cms/logos/empty-photo.png');
}

function deleteHall(element) {
    $(element).parent().parent().css('display', 'none');
    let hallID = ($(element).attr('id')).replace('number-to-delete', 'DELETE');
    $(`#${hallID}`).prop('checked', true);
}



