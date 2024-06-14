$(document).ready(function() {
    $('.favorite_player').change(function() {
        let game_player_name = $(this).data('game-player-name');
        console.log(game_player_name)
        let isFavorite = $(this).is(':checked');

        $.ajax({
            url: '/search-game-player/',
            method: 'POST',
            data: {
                'game_player_name': game_player_name,
                'is_favorite': isFavorite,
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
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}