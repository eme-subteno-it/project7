$(document).ready(function () {

    function addSubmit(e) {
        e.preventDefault();

        // Display the question
        var datas =  $(this).serializeArray()
        var dataInput = datas[0]
        textZone(dataInput.value, false)

        $('#mess-user').val('')
    }
    $('#question').on('submit', addSubmit);

    function textZone(lastText, isBot) {
        var $parent = $('.container-tchat')
        var response = $('<p class="result"></p>');
        var iconBot = $('<img src="static/img/tchat-bot.png" class="icon-bot"/>');
        
        if (isBot) {
            var $container = $('<div class="d-flex message"></div>');
            $container.append(iconBot);
        } else {
            var $container = $('<div class="d-flex message text-right ml-5"></div>');
        }

        $container.append(response);
        $parent.append($container);
        response.text(lastText);

        var containerChat = document.getElementById('container-tchat');
        containerChat.scrollTop = containerChat.scrollHeight;
    }
});