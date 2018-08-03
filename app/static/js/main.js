$(document).ready(function () {
    $('#stages-search').on(
        'change', function () {

            let sample_id = $("#stages-search").val();
            $.ajax({
                type: "GET",
                url: "/api/samples/" + sample_id + "/stages",
                success: function (data) {
                    $(".object-list").replaceWith(data)
                },
                dataType: 'html'
            });
        });
});

$(document).ready(function () {
    $('#samples-search').on(
        'keyup', function () {

            let sample_stub = $("#samples-search").val();
            $.ajax({
                type: "GET",
                url: "/api/samples-search/?q=" + sample_stub,
                success: function (data) {
                    $(".object-list").replaceWith(data)
                },
                dataType: 'html'
            });
        });
});

$(document).ready(function () {
    $("#samples-search").autocomplete({
        source: "/api/samples-autocomplete/",
        minLength: 1,
    });
});

$(document).ready(function () {
    $("#stages-search").autocomplete({
        source: "/api/samples-autocomplete/",
        minLength: 1,
    });
});


$(document).ready(function () {
    $(document.body).on("click", "#save-stage", function () {

            let frm = $('#stage-form');

            frm.submit(function (e) {

                e.preventDefault();
                let confirmation = confirm("Confirm saving this stage?");
                if (confirmation) {
                    $.ajax({
                        type: frm.attr('method'),
                        url: frm.attr('action'),
                        data: frm.serialize(),
                        success: function (data) {
                            console.log('Submission was successful.');
                            $.ajax({
                                type: "GET",
                                url: "/api/samples/" + $("#sample_id").val() + "/stages",
                                success: function (data) {
                                    $(".object-list").replaceWith(data)
                                },
                                dataType: 'html'
                            });
                        },
                        error: function (data) {
                            console.log('An error occurred.');
                            console.log(data);
                        },
                    })
                }
            });

        });


});

