$(document).ready(function () {
    $("#addrow").on("click", function () {
        let newRow = $("<tr>");
        let cols = "";
        cols += '<th class="num-increment" scope="row"></th>';
        cols += '<td></td>';
        cols += '<td>' + $('.select-action')[0].clone() + '</td>';

        cols += '<td><input type="button" class="ibtnDel btn btn-md btn-danger "  value="Save"></td>';
        newRow.append(cols);
        $("#stages-table").append(newRow);

    });

});






    //
    //
    // // https://www.c-sharpcorner.com/article/dynamically-append-rows-to-the-table-with-jquery/
    //
    // function addRow()
    // {
    //     var table = document.getElementById("tbl"); //get the table
    //     var rowcount = table.rows.length; //get no. of rows in the table
    //     //append the controls in the row
    //     var tblRow = '
    //     <tr id="row' + rowcount + '">
    //         <td>
    //             <label id="lblID' + rowcount + '">' + rowcount + '</label>' +
    //         '
    //         </td>
    //         <td>
    //             <input type="text" class="form-control" placeholder="Enter Ticket No" id="txtTicketNo' + rowcount + '" />
    //         </td>' +
    //         '
    //         <td>
    //             <input type="text" class="form-control" placeholder="Enter Price" id="txtPrice' + rowcount + '" />
    //         </td>' +
    //         '
    //         <td>
    //             <input type="button" class="btn btn-info" id="btnSave' + rowcount + '" onclick="SaveTicket(' + rowcount + ')" value="Save" />
    //         </td>
    //     </tr>'
    //         //append the row to the table.
    //     $("#tbl").append(tblRow);
    // }
    //
    // function SaveTicket(id)
    // {
    //     var id = $("#lblID" + id).html();
    //     var tcktNo = $("#txtTicketNo" + id).val();
    //     var Price = $("#txtPrice" + id).val();
    //     //remove current selected row
    //     $("#row" + id).remove();
    //     //append new row
    //     var tblRow = '
    //     <tr id="row' + id + '">
    //         <td>
    //             <label id="lblID' + id + '">' + id + '</label>
    //         </td>
    //         <td>
    //             <label id="lblTicketNo' + id + '">' + tcktNo + '</label>' +
    //         '
    //         </td>
    //         <td>
    //             <label id="lblPrice' + id + '" >' + Price + '</label>
    //         </td>
    //         <td>' +
    //         '
    //             <input type="button" class="btn btn-warning" id="btnEdit' + id + '" onclick="EditTicket(' + id + ')" value="Edit" />' +
    //             ' |
    //             <input type="button" class="btn btn-danger" id="btnDelete' + id + '" onclick="DeleteTicket(' + id + ')" value="Delete" />
    //         </td>
    //     </tr>'
    //     $("#tbl").append(tblRow);
    // }
    //
    // function EditTicket(id)
    // {
    //     var id = $("#lblID" + id).html();
    //     var tcktNo = $("#lblTicketNo" + id).html();
    //     var Price = $("#lblPrice" + id).html();
    //     $("#row" + id).remove();
    //     var tblRow = '
    //     <tr id="row' + id + '">
    //         <td>
    //             <label id="lblID' + id + '">' + id + '</label>
    //         </td>' +
    //         '
    //         <td>
    //             <input type="text" class="form-control" placeholder="Enter Ticket No" value=' + tcktNo + ' id="txtTicketNo' + id + '" />
    //         </td>' +
    //         '
    //         <td>
    //             <input type="text" class="form-control" placeholder="Enter Price" value=' + Price + ' id="txtPrice' + id + '" />
    //         </td>' +
    //         '
    //         <td>
    //             <input type="button" class="btn btn-info" id="btnUpdate' + id + '" onclick="UpdateTicket(' + id + ')" value="Update" />
    //         </td>
    //     </tr>'
    //   $("#tbl").append(tblRow);
    // }
    //
    // function UpdateTicket(id)
    // {
    //     var id = $("#lblID" + id).html();
    //     var tcktNo = $("#txtTicketNo" + id).val();
    //     var Price = $("#txtPrice" + id).val();
    //     $("#row" + id).remove();
    //     var tblRow = '
    //     <tr id="row' + id + '">
    //         <td>
    //             <label id="lblID' + id + '">' + id + '</label>
    //         </td>
    //         <td>
    //             <label id="lblTicketNo' + id + '">' + tcktNo + '</label>
    //         </td>' +
    //         '
    //         <td>
    //             <label id="lblPrice' + id + '" >' + Price + '</label>
    //         </td>' +
    //         '
    //         <td>
    //             <input type="button" class="btn btn-warning" id="btnEdit' + id + '" onclick="EditTicket(' + id + ')" value="Edit" /> ' +
    //             '|
    //             <input type="button" class="btn btn-danger" id="btnDelete' + id + '" onclick="DeleteTicket(' + id + ')" value="Delete" />
    //         </td>
    //     </tr>'
    //     $("#tbl").append(tblRow);
    // }
    //
    // function DeleteTicket(id)
    // {
    //     $("#row" + id).remove();
    // }