document.addEventListener('DOMContentLoaded', function() {
    function addPlayer(player) {
	const tmpusername = player.split(' ')[0]; // strip everything after the first space
        player = tmpusername;
        const playersDiv = document.getElementById('players');
        const playerElement = document.createElement('div');
        playerElement.classList.add('player');

        const avatarURL = `https://minotar.net/avatar/${player}`;
        const img = document.createElement('img');
        img.src = avatarURL;
        img.alt = `${player}'s avatar`;
        img.classList.add('avatar');
        playerElement.appendChild(img);
        playerElement.appendChild(document.createTextNode(player));
        playersDiv.appendChild(playerElement);
    }

    function fetchAndDisplayPlayers() {
        fetch('http://minecraft.server:5000/current_players')
            .then(response => response.json())
            .then(data => {
                const playersDiv = document.getElementById('players');
                if (data.players && data.players.length > 0) {
		    playersDiv.innerHTML = '';	
		    data.players.forEach(addPlayer);			

                } else {
		    playersDiv.innerHTML = '';	
                    playersDiv.innerHTML = '<br><br><div id="players">No players online right now!</div>' +
                                       '<img src="sleepingfox.png" alt="No players online">';
                }
            })
            .catch(error => {
                console.error('Error fetching player data:', error);
                document.getElementById('players').textContent = 'Error loading player data.';
            });
    }

    fetchAndDisplayPlayers();

    setInterval(fetchAndDisplayPlayers, 10000);

});

