$(document).ready(function() {
    $('.favorite_player').change(function() {
        var  game_player_name= $(this).data('game-player-name');
        var isFavorite = $(this).is(':checked');

        $.ajax({
            url: '/search-game-player/',
            method: 'POST',
            data: {
                'game_player_name': game_player_name,
                'csrfmiddlewaretoken': getCookie('csrftoken')
            },
            success: function(response) {
                console.log('Favorite toggled successfully.');
            },
            error: function(xhr, status, error) {
                console.error('Error toggling favorite:', error);
            }
        });
        });
    });

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}