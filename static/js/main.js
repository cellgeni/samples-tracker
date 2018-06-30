$(document).ready(function () {
            $('#samples-search').on(
                'keypress', function () {

        let sample_id = $("#samples-search").val();
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
    $("#samples-search").autocomplete({
        source: "/api/samples-search/",
        minLength: 1,
    });
});
