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
