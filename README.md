# Python Nitrado API


This API accesses the Nitrado API found at [Nitrado API](https://api.nitrado.net/)


# Overview

To have access to the Nitrado you must have an account created at [Nitrado](https://server.nitrado.net/)
and create an API key.

# [Wiki - Full documentation](https://github.com/mjlomeli/NitradoAPI/wiki)
### Table of contents
#### 1. [Introduction](https://github.com/mjlomeli/NitradoAPI/wiki#introduction)
   > Shows how to get access to your API key.
#### 2. [Getting Started](https://github.com/mjlomeli/NitradoAPI/wiki/Getting-Started)
   > Shows how to log in to the client and use the basic code interface
#### 3. [Services](https://github.com/mjlomeli/NitradoAPI/wiki/Services)
   > Data provided outside of the game server. Like server status, user id, and auto extension plan.
#### 4. [GameServer](https://github.com/mjlomeli/NitradoAPI/wiki/GameServer)
   > Data directly related to the game server. This includes the player list, game settings, etc.




### Connect to Client
To begin using the API the Client must first be connected to your Nitrado account.
Once connected to the client, you should have access to any of the API calls.

```python
from nitrado_api import NitradoAPI

NitradoAPI.initialize_client("https://api.nitrado.net/", "your-api-key")
api = NitradoAPI()
```

**or**

```python
from nitrado_api import NitradoAPI

api = NitradoAPI("https://api.nitrado.net/", "your-api-key")
```

### Services
This example highlights how to get the service.
```python
from nitrado_api import NitradoAPI

api = NitradoAPI("https://api.nitrado.net/", "your-api-key")

services = api.services
print(services)
```
```python
[
    <Service(id=1011111, username='ni11111_1', details={'address': '111.111.111.111:9996', 'name': '[API] My-Server-1', 'game': 'ARK: Survival Evolved (Xbox One)', 'portlist_short': 'arkxb', 'folder_short': 'arkxb', 'slots': 70})>,
    <Service(id=1011112, username='ni11111_1', details={'address': '111.111.111.112:9996', 'name': '[API] My-Server-2', 'game': 'ARK: Survival Evolved (Xbox One)', 'portlist_short': 'arkxb', 'folder_short': 'arkxb', 'slots': 70})>,
    <Service(id=1011113, username='ni11111_1', details={'address': '111.111.111.113:9996', 'name': '[API] My-Server-3', 'game': 'ARK: Survival Evolved (Xbox One)', 'portlist_short': 'arkxb', 'folder_short': 'arkxb', 'slots': 70})>
]
``` 

#### GameServer
This example highlights how to get the gameserver.
```python
from nitrado_api import NitradoAPI

api = NitradoAPI("https://api.nitrado.net/", "your-api-key")

gameserver = api.game_servers
print(gameserver)
```
```python
[
    <GameServer(service_id=11111111, status='started', query={'server_name': '[API] My-Server-1', 'connect_ip': '111.111.111.111:9996', 'map': 'LostIsland', 'version': '943.10', 'player_current': 0, 'player_max': 70, 'players': []})>,
    <GameServer(service_id=11111112, status='started', query={'server_name': '[API] My-Server-2', 'connect_ip': '111.111.111.112:9996', 'map': 'Ragnarok', 'version': '943.10', 'player_current': 0, 'player_max': 70, 'players': []})>,
    <GameServer(service_id=11111113, status='started', query={'server_name': '[API] My-Server-3', 'connect_ip': '111.111.111.113:9996', 'map': 'TheIsland', 'version': '943.10', 'player_current': 0, 'player_max': 70, 'players': []})>
]
```



