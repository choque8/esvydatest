

 $(document).ready(function() {
    var table = $('#dataTable').DataTable({
        "language": {
                url: "/static/localizacion/es_ES.json"
        }});
     
    $('#dataTable tbody').on('click', 'tr', function () {

        var data = table.row( this ).data();
        //alert( 'You clicked on '+data[0]+'\'s row' );
        
        
    } );
 } );





function getDate() {
    var d = new Date();
    var day = addZero(d.getDate());
    var month = addZero(d.getMonth()+1);
    var year = addZero(d.getFullYear());
    var h = addZero(d.getHours());
    var m = addZero(d.getMinutes());
    var s = addZero(d.getSeconds());
    return day + "-" + month + "-" + year + " " + h + ":" + m;
}


// AJAX
function sendAjax(url, params, myCallback, args) {
    if (typeof args === "undefined") {
        load_elem = "#load";
    } else {
        load_elem = args.load_elem;
    }
    /*$(load_elem).show().html('<img src="/static/img/load16.gif" />');*/
    $(load_elem).show().html('Cargando...');
    if (typeof args === "undefined" || args.met === "get") {
        $.get(url, params).done(function(data) {
            myCallback(data);
            $(load_elem).fadeOut();
        }).fail(function(error) {
            console.log(error);
        });
    } else if (args.met === "post") {
        $.post(url, params).done(function(data) {
            myCallback(data);
            $(load_elem).fadeOut();
        }).fail(function(error) {
            console.log(error);
        });
    }
}



function abrir_modal(url)
{
    $('#popup').load(url, function()
    {
            $(this).modal('show');
    });
    return false;
}


function cancel_appointment(url) {
    $.getJSON(url, function (data) {
        console.log(data)
        location.reload();
        alert("Se ha cancelado la cita");
    });   
}


function cerrar_modal()
{
        $('#popup').modal('hide');
        return false;
}


$(document).ready(function()
{
    var table = $('#dataTables').dataTable(  );
});
