

$(function() {
    $('#ticket_status').val(status);
});

$("form[name=signup_form]").submit(function (e) {
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/signup_user",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (resp) {
            window.location.href = "/";
        },
        error: function (resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    })

    e.preventDefault();
});

$("form[name=login_form]").submit(function (e) {
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/login_user",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (resp) {
            window.location.href = "/";
        },
        error: function (resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    })

    e.preventDefault();
});

$("form[name=create_ticket]").submit(function (e) {
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/tickets/create",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (resp) {
            //console.log(resp);
            window.location.href = "/tickets/";
        },
        error: function (resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    })

    e.preventDefault();
});

$("form[name=edit_ticket]").submit(function (e) {
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/tickets/edit/",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (resp) {
            console.log(resp);
            window.location.href = "/tickets/";
        },
        error: function (resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    })

    e.preventDefault();
});

$("form[name=create_catalog_item]").submit(function (e) {
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/catalog/create",
        type: "POST",
        data: data,
        dataType: "json",

        success: function (resp) {
            //console.log(resp);
            window.location.href = "/catalog/";
        },
        error: function (resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    })

    e.preventDefault();
});

$("form[name=isbn_autofill]").submit(function (e) {
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/catalog/create",
        type: "POST",
        data: data,
        dataType: "json",

        success: function (resp) {

            console.log(resp);

            if (resp.redirect) {
                window.location.href = resp.redirect;
            }
        },
        error: function (resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    })

    e.preventDefault();
});