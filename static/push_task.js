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
    $("#submitData").click(function () {
        // Array to store the data
        var postData = [];
        console.log("Submit button clicked.");
        // Iterate through each row in the table body
        $("#insertNewData tbody tr").each(function () {
            // Check if the 'Name' column is not blank
            var name = $(this).find("td:eq(0)").text().trim();
            if (name !== "") {
                // If not blank, collect data from the row
                var code = $(this).find("select").val();
                var pointNeed = $(this).find("td:eq(2)").text().trim();
                var note = $(this).find("td:eq(3)").text().trim();
                var deadline = $(this).find("td:eq(4)").text().trim();

                // Add the data to the array
                postData.push({
                    name: name,
                    code: code,
                    pointNeed: pointNeed,
                    note: note,
                    deadline: deadline
                });
            }
        });

        // Check if there is any data to post
        if (postData.length > 0) {
            // Send the data to your Django server using AJAX
            $.ajax({
                url: '/api/tasks/',  // Replace with your Django endpoint
                type: 'POST',
                data: JSON.stringify(postData),
                contentType: 'application/json',
                success: function (response) {
                    console.log('Data posted successfully:', response);
                    // Optionally, you can handle the success response here
                },
                error: function (error) {
                    console.error('Error posting data:', error);
                    // Optionally, you can handle the error here
                }
            });
        } else {
            console.log('No data to post.');
        }
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