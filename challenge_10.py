#
# Llamar a una API es una de las tareas más comunes en programación.
#
# Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
# resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
#
# Aquí tienes un listado de posibles APIs: 
# https://github.com/public-apis/public-apis
#

import requests
import json

URL = "https://api.clashroyale.com/v1"
CLAN = "clanpeyo"

CLASH_ROYALE_TOKEN = "Jijijija"


class ClashRoyaleAPI:
    def __init__(self, url: str, token: str) -> None:
        self.url = url
        self.token = token
        
        
class Player(ClashRoyaleAPI):
    def __init__(self, url: str, token: str, tag: str) -> None:
        super().__init__(url, token)
        self.tag = tag
        
    
    def player_info(self) -> requests.Response:
        # https://api.clashroyale.com/v1/players/%23YYLOCLRC
        endpoint = "/players/%23" + self.tag
        request = requests.get(self.url + endpoint, {"Authorization": "Bearer " + self.token})
        print(request.status_code)
        print(self.url + endpoint)
        response = request.json()
        
        return response
    

class Clan(ClashRoyaleAPI):
    def __init__(self, url: str, token: str, name: str) -> None:
        super().__init__(url, token)
        self.name = name
    
    
    def clan_info(self) -> requests.Response:
        endpoint = "/clans?name=" + self.name
        request = requests.get(self.url + endpoint, {"Authorization": "Bearer " + self.token})
        response = request.json()
        
        return response


def main():
    # request simple
    print(type(CLASH_ROYALE_TOKEN))
    player = Player(URL, CLASH_ROYALE_TOKEN, tag="YYL0CLRC")
    clan = Clan(URL, CLASH_ROYALE_TOKEN, name="clanpeyo")

    print(player.player_info())
    print(clan.clan_info())


if __name__ == '__main__':
    main()