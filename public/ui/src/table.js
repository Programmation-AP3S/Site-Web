function table_click() {
    $("tr[data-href]").on("click", function () {
        document.location = $(this).data("href");
    });
}

window.addEventListener("DOMContentLoaded", table_click);
