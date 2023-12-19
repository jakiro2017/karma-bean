window.onload = function () {
    var date = new Date(), y = date.getFullYear(), m = date.getMonth();
    var firstDay = new Date(y, m, 1);
    var lastDay = new Date(y, m + 1, 0);

    document.getElementById('start_date').valueAsDate = firstDay;
    document.getElementById('end_date').valueAsDate = lastDay;

    document.getElementById('toggleSections').addEventListener('click', function () {
        var viewOldData = document.getElementById('viewOldData');
        var insertNewData = document.getElementById('insertNewData');

        if (viewOldData.style.display === 'none') {
            viewOldData.style.display = 'block';
            insertNewData.style.display = 'none';
        } else {
            viewOldData.style.display = 'none';
            insertNewData.style.display = 'block';
        }
    });
}