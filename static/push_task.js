$(document).ready(function () {
    $("td[contenteditable=true]").on("contextmenu", function (e) {
        e.preventDefault();
        $(this).attr("contenteditable", "true");
    });

    $("td[contenteditable=true]").on("blur", function () {
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
    $('.deadline').datepicker({
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