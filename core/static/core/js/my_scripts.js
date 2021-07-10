$(document).ready(function(){
    $('#id_idProducto').attr('readonly','readonly')
});

$(document).ready(function() {
    $("#texto_buscado").on("keyup", function() {
        var texto = $(this).val().toLowerCase();
        $("#datos_tabla tr").filter (function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(texto) > -1)
        });
    });
});