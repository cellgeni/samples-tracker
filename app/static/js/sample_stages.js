$(document).ready(function () {
    $("#addrow").on("click", function () {
        let newRow = $("<tr>");
        let cols = "";
        cols += '<th class="num-increment" scope="row"></th>';
        cols += '<td></td>';
        cols += '<td>' + $('.select-action')[0].clone() + '</td>';
        cols += '<td>' + $('.select-owner')[0].clone() + '</td>';

        cols += '<td><input type="button" class="ibtnDel btn btn-md btn-danger "  value="Save"></td>';
        newRow.append(cols);
        $("#stages-table").append(newRow);

    });

});
