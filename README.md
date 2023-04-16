# Python Nitrado SDK

[![Testing](https://github.com/mjlomeli/NitradoAPI/actions/workflows/tests.yml/badge.svg)](#) tests need a Nitrado subscription account 


A Python based SDK for the [Nitrado RESTful API](https://doc.nitrado.net/) published at [PyPI](https://pypi.org/project/nitrado/).


# Overview

To have access to this application you must have an account created at [Nitrado](https://server.nitrado.net/)
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

<br />

# Installation
In your terminal install the nitrado package with pip.

```shell
pip install nitrado
```

<br />

# Examples

### Connect to Client
To begin using the API the Client must first be connected to your Nitrado account.
Once connected to the client, you should have access to any of the API calls.


```python
from nitrado import NitradoAPI

api = NitradoAPI("your-api-key")
```

### Services
This example highlights how to get the service.

```python
from nitrado import NitradoAPI

api = NitradoAPI("your-api-key")

api.services()
```
```python
[
    <Service(id=1011111, status='active', type_human='Publicserver 10 slots', suspend_date='2023-05-07T01:21:11')>,
    <Service(id=1022222, status='active', type_human='Publicserver 20 slots', suspend_date='2023-07-07T02:11:01')>,
    <Service(id=1033333, status='active', type_human='Publicserver 30 slots', suspend_date='2023-09-07T06:51:41')>
]
``` 

#### GameServer
This example highlights how to get the gameserver.

```python
from nitrado import NitradoAPI

api = NitradoAPI("your-api-key")

gameserver = api.game_servers()
```
```python
[
    <GameServer(service_id=11111111, location='US', slots=10, ip='1.2.3.4', game_human='ARK: Survival Evolved (Xbox One)')>,
    <GameServer(service_id=22222222, location='US', slots=70, ip='11.22.33.44', game_human='ARK: Survival Evolved (Xbox One)')>
]
```



