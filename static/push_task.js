$(document).ready(function () {
    $("#viewOldData td[contenteditable=true]").on("contextmenu", function (e) {
        e.preventDefault();
        $(this).attr("contenteditable", "true");
    });

    $("#viewOldData td[contenteditable=true]").on("blur", function () {
        var newContent = $(this).text();
        var columnIndex = this.cellIndex;
        var id = $(this).siblings().first().text();

        $.ajax({
            url: '/task-summary/update_task',  // update this with your update url
            type: 'POST',
            data: {
                'id': id,
                'columnIndex': columnIndex,
                'new_content': newContent,
            },
            success: function (response) {
                // handle success
            },
            error: function (response) {
                // handle error
                alert(response.responseText);
            }
        });
    });
    $('#viewOldData .deadline').datepicker({
        format: 'yyyy-mm-dd',
        autoclose: true
    }).on('changeDate', function (e) {
        var now = new Date();
        var hours = now.getHours();
        var minutes = now.getMinutes();

        // Format current time as HH:MM
        var currentTime = (hours < 10 ? '0' : '') + hours + ':' + (minutes < 10 ? '0' : '') + minutes;

        // Combine the selected date with the current time
        var dateTime = e.format() + ' ' + currentTime;

        // Fill the cell with the new date and time
        $(this).text(dateTime);

        console.log('Deadline changed: ' + dateTime);
    });
    $("#insertNewData td[contenteditable=true]").on("click", function () {
        // Auto-fill tomorrow's date in the 4th cell when clicked
        var tomorrowDate = new Date();
        tomorrowDate.setDate(tomorrowDate.getDate() + 1);

        var formattedDate = formatDate(tomorrowDate);
        $(this).siblings(".auto-fill-date").text(formattedDate);
    });
});

function updateTaskCode(taskId, newCode) {
    $.ajax({
        url: '/task-summary/update_task_code',  // URL of your Django view
        type: 'POST',
        data: {
            'task_id': taskId,
            'new_code': newCode,
        },
        success: function (data) {
            // Handle success (optional)
        },
        error: function (data) {
            // Handle error (optional)
        }
    });
}
function formatDate(date) {
    var year = date.getFullYear();
    var month = ('0' + (date.getMonth() + 1)).slice(-2);
    var day = ('0' + date.getDate()).slice(-2);
    var hours = ('0' + date.getHours()).slice(-2);
    var minutes = ('0' + date.getMinutes()).slice(-2);

    return year + '-' + month + '-' + day + ' ' + hours + ':' + minutes;
}