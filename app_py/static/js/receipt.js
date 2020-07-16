$(document).ready(function () {

    function addSubmit(e) {
        e.preventDefault();

        // Display the question
        var datas =  $(this).serializeArray()
        var dataInput = datas[0]
        textZone(dataInput.value, false)

        $('#mess-user').val('')

        // Return the response GrandPy Bot
        function getTheResponse() {
            $.ajax({
                method: 'POST',
                url: '/get_response/',
                data: dataInput.value,
            }).done(function (data) {
                var address = JSON.parse(data);
                var lastText = ''

                if (!address) {
                    lastText = 'Mmm, je suis embêté, je ne trouve pas l\'endroit que tu cherches.';
                    textZone(lastText, true);
                } else {
                    lastText = 'Bien sûr mon poussin ! La voici : ' + address.formatted_address;
                    textZone(lastText, true);

                    // Map management
                    if ($('#map').length) {
                        $('#map').replaceWith('<div class="old-research"><span>Ancienne recherche</span></div>');
                    } 
                    var $parent = $('.container-tchat');
                    var mapStructure = $('<div id="map"></div>');
                    $parent.append(mapStructure);

                    latMap = address.geometry.lat;
                    lngMap = address.geometry.lng;
                    initMap(latMap, lngMap);
                }
            })
        }
        
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