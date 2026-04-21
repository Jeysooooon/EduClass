document.addEventListener("DOMContentLoaded", function () {
    if (!window.jQuery || !jQuery.fn.DataTable) {
        return;
    }

    jQuery(".datatable").each(function () {
        const noSortable = [];

        jQuery(this)
            .find("thead th")
            .each(function (index) {
                if (jQuery(this).attr("data-sortable") === "false") {
                    noSortable.push(index);
                }
            });

        jQuery(this).DataTable({
            pageLength: 5,
            lengthMenu: [
                [5, 10, 25, 50, -1],
                [5, 10, 25, 50, "Todos"],
            ],
            autoWidth: false,
            order: [],
            columnDefs: noSortable.length
                ? [{ orderable: false, targets: noSortable }]
                : [],
            language: {
                lengthMenu: "Mostrar _MENU_ registros",
                zeroRecords: "No se encontraron resultados",
                info: "Mostrando _START_ a _END_ de _TOTAL_ registros",
                infoEmpty: "Mostrando 0 a 0 de 0 registros",
                infoFiltered: "(filtrado de _MAX_ registros totales)",
                search: "Buscar:",
                paginate: {
                    first: "Primero",
                    last: "Ultimo",
                    next: "Siguiente",
                    previous: "Anterior",
                },
            },
        });
    });
});
