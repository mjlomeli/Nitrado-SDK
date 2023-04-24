# Python Nitrado SDK

[![Testing](https://github.com/mjlomeli/NitradoAPI/actions/workflows/tests.yml/badge.svg)](#)


A Python based SDK for the [Nitrado RESTful API](https://doc.nitrado.net/) published at [PyPI](https://pypi.org/project/nitrado/).

# Installation
In your terminal install the nitrado package with pip.

```shell
pip install nitrado
```


# Overview

To have access to this application you must have an account created at [Nitrado](https://server.nitrado.net/)
and create an API key.

# [Wiki - Full documentation](https://github.com/mjlomeli/NitradoAPI/wiki)
### Table of contents
#### 1. [Generate API Key](https://github.com/mjlomeli/NitradoAPI/wiki/Generate-API-Key)
   > Shows how to get access to your API key.
#### 2. [Getting Started](https://github.com/mjlomeli/NitradoAPI/wiki/Getting-Started)
   > Shows how to log in to the client and use the basic code interface
#### 3. [Globals](https://github.com/mjlomeli/NitradoAPI/wiki/Globals)
   > Basic requests from Nitrado for health and maintenance checks.
#### 4. [Services](https://github.com/mjlomeli/NitradoAPI/wiki/Services)
   > Data provided outside of the game server. Like server status, user id, and auto extension plan.
#### 5. [GameServer](https://github.com/mjlomeli/NitradoAPI/wiki/GameServer)
   > Data directly related to the game server. This includes the player list, game settings, etc.
#### 6. [Games](https://github.com/mjlomeli/NitradoAPI/wiki/Games)
   > Custom game specific libraries.

<br />

# Examples

### [Globals](https://github.com/mjlomeli/NitradoAPI/wiki/Globals)
The basic maintanance tools from Nitrado API.

```python
from nitrado import Global

version = Global.version()
print(version)

'nitrapi-1201-wh2h4'

health = Global.health_check()
print(health)

<Global(success=True, data=None, message='All systems operate as expected.', status='success')>
```
<br />

### [Services](https://github.com/mjlomeli/NitradoAPI/wiki/Services)
This example highlights how to get the service.

```python
from nitrado import Service

services = Service.all()
print(services)
```
```python
[
    <Service(id=1011111, status='active', type_human='Publicserver 10 slots', suspend_date='2023-05-07T01:21:11')>,
    <Service(id=1022222, status='active', type_human='Publicserver 20 slots', suspend_date='2023-07-07T02:11:01')>,
    <Service(id=1033333, status='active', type_human='Publicserver 30 slots', suspend_date='2023-09-07T06:51:41')>
]
``` 
<br />

### [GameServer](https://github.com/mjlomeli/NitradoAPI/wiki/GameServer)
This example highlights how to get the gameserver.

```python
from nitrado import GameServer

gameservers = GameServer.all()
print(gameservers)
```
```python
[
    <GameServer(service_id=11111111, location='US', slots=10, ip='1.2.3.4', game_human='ARK: Survival Evolved (Xbox One)')>,
    <GameServer(service_id=22222222, location='US', slots=70, ip='11.22.33.44', game_human='ARK: Survival Evolved (Xbox One)')>
]
```

<br />

