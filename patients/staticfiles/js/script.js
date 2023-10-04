"use strict";

setInterval(function () {
    const date = new Date();
    const formattedTime =
        (date.getHours() < 10 ? "0" : "") + date.getHours() + ":" +
        (date.getMinutes() < 10 ? "0" : "") + date.getMinutes() + ":" +
        (date.getSeconds() < 10 ? "0" : "") + date.getSeconds();
    $("#clock").html(formattedTime);
}, 500);

function validateEmail(email) {
    const regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email)
};

function validateAll() {
    const name = $("#name").val();
    const phone = $("#phone").val();
    const email = $("#email").val();
    const age = $("#age").val();
    const gender = $("#gender").val();

    if (name == "") {
        swal("Opsss!", "Name field cannot be empty.", "error");
        return false;
    } else if (name == name.toUpperCase()) {
        swal("Opsss!", "Name cannot be uppercased.", "error");
        $("#name").val("");
        return false;
    } else if (name == name.toLowerCase()) {
        swal("Opsss!", "Name cannot be lowercased.", "error");
        $("#name").val("");
        return false;
    } else if (name.split(" ").length < 2) {
        swal("Opsss!", "Put at least the last name", "info");
        return false;
    } else if (phone == "") {
        swal("Opsss!", "Phone field cannot be empty.", "error");
        return false;
    } else if (!(validateEmail(email))) {
        swal("Opsss!", "Put a valid email address.", "error");
        $("#email").val("");
        return false;
    } else if (age == "") {
        swal("Opsss!", "Age field cannot be empty.", "error");
        return false;
    } else if (gender == "") {
        swal("Opsss!", "Gender field cannot be empt.y", "error");
        return false;
    } else {
        return true;
    }
}

$("#btn-add").bind("click", validateAll);

// else if (age > 100) {
//     swal("Denied!", "The maximum age is 100", "error");
//     $("#age").val("")
//     return false;
// } 

$(document).ready(function () {
    jQuery("input[name='name']").keyup(function () {
        const letter = jQuery(this).val();
        const allow = letter.replace(/[^a-zA-z _]/g, "");
        jQuery(this).val(allow);
    });
    $("input").on("keypress", function (e) {
        if (e.which === 32 && !this.value.length) {
            e.prevenDefault();
        }
    });
});

$(document).ready(function () {
    $("#name").keyup(function () {
        var name = $("#name").val();
        if (name.split(' ').length == 3) {
            swal("Opsss!", "Only name and last name", "info");
            $("#name").val("")
            return false;
        }
    })
})

$("#name").keyup(function () {
    const txt = $(this).val();
    $(this).val(txt.replace(/^(.)|\s(.)/g, function ($1) {
        return $1.toUpperCase();
    }))
})

$(document).ready(function () {
    $("#phone").inputmask("(+383) 99999-999", {
        "onincomplete": function () {
            swal("Opsss!", "Incomplete phone. Please review", "info");
            return false;
        }
    });
});

$(document).ready(function () {
    $("#email").keyup(function () {
        this.value = this.value.toLowerCase();
    })
})

$(document).ready(function () {
    $("#age").keyup(function () {
        const age = $("#age").val();
        if (age > 100) {
            $("#age").val("");
            return false;
        }
    })
})

$("#age").keyup(function () {
    if (!/^[0-9]*$/.test(this.value)) {
        this.value = this.value.split(/[^0-9]/).join('');
    }
})

$("#age").on("input", function () {
    if (/^0/.test(this.value)) {
        this.value = this.value.replace(/^0/, "");
    }
})