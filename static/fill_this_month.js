window.onload = function () {
    var date = new Date(), y = date.getFullYear(), m = date.getMonth();
    var firstDay = new Date(y, m, 1);
    var lastDay = new Date(y, m + 1, 0);

    document.getElementById('start_date').valueAsDate = firstDay;
    document.getElementById('end_date').valueAsDate = lastDay;
}