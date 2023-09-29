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
});