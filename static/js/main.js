$(document).ready(function () {

    // $('#samples-search').keyup(function () {
    //     $.ajax({
    //         type: "GET",
    //         url: "/api/samples-search/",
    //         data: {
    //             'q': $('#samples-search').val(),
    //             'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
    //         },
    //         success: function (data) {
    //             $(".object-list").replaceWith(data)
    //         },
    //         dataType: 'html'
    //     });
    // });

    $("#samples-select").change(function() {
          // alert( "Handler for .change() called." );

        let sample_id = $("#samples-select").val();
                $.ajax({
            type: "GET",
            url: "/api/samples/" + sample_id + "/stages",
            // data: {
            //     // 'q': $('#samples-search').val(),
            //     // 'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            // },
            success: function (data) {
                $(".object-list").replaceWith(data)
            },
            dataType: 'html'
        });
    });
});




//
// $(document).ready(function () {
//     $("#samples-list").autocomplete({
//         source: "/samples-search/",
//         minLength: 1,
//     });
// });