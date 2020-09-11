$(document).ready(function () {

    function addSubmit(e) {
        e.preventDefault();

        // Display the question
        var datas =  $(this).serializeArray()
        var dataInput = datas[0]
        textZone(dataInput.value, false)

        $('#mess-user').val('')
        // The bot search...
        var i = 3
        var loop = setInterval(searchBot, 500);

        function searchBot() {
            i--;
            if (i == 0) {
                clearInterval(loop)
                $("#divOverlayLoad").addClass('d-none');
                getTheResponse();
            } else {
                $("#divOverlayLoad").removeClass('d-none');
            }
        }

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
                } else if (address.error){
                    textZone(address.error, true);
                } else {
                    var street = address.address_components;
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

                    if (street) {
                        getStory(street);
                    } else {
                        getStory(address.formatted_address);
                    }
                }
            })
        }

        // GrandPy Bot is telling a story about the address...
        function getStory(address) {
            $.ajax({
                method: 'POST',
                url: '/get_story/',
                data: address,
            }).done(function (data) {
                var json = JSON.parse(data)

                try {
                    var story = json.extract
                    var url = json.url
                    var textUrl = 'Voici un lien pour en savoir plus : '
                    var link = '<a target="_blank" href="' + url + '">Clique ici</a>';

                    
                    var response = 'Mais t\'ai-je déjà raconté l\'histoire de ce quartier qui m\'a vu en culottes courtes ? <br/>' + story + '<br/>' + textUrl + link
                    textZone(response, true)
                } catch (error) {
                    textZone(error.message, true)
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
        response.html(lastText);

        var containerChat = document.getElementById('container-tchat');
        containerChat.scrollTop = containerChat.scrollHeight;
    }
});