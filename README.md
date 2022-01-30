# Python Nitrado API


This API accesses the Nitrado API found at [Nitrado API](https://api.nitrado.net/)


# Overview

To have access to the Nitrado you must have an account created at [Nitrado](https://server.nitrado.net/)
and create an API key.

## Creating the API Key
### Login
Login and go into your account.

<img src="./images/dropdown.png" alt="login" /><br />

### Account
From your account, head over to the options. Click on the
**Developer Portal**.

<img src="./images/account.png" alt="account" /><br />

### Developer Portal
In the **Developer Portal** you'll want to create a long-life token.

<img src="./images/developer.png" alt="developer"/><br />


### Long Life Token
Add a description for your token and check the areas of access you'd
want your token to be granted.

<img src="./images/token.png" alt="token" /><br />


# Introduction

### Connect to Client
To begin using the API the Client must first be connected to your Nitrado account.

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

### Using the API
Once connected to the client, you should have access to any of the API calls in these examples.
These two examples show how to get the service and game server data.

#### Services
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



