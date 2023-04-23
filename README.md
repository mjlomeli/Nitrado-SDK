# Python Nitrado SDK

[![Testing](https://github.com/mjlomeli/NitradoAPI/actions/workflows/tests.yml/badge.svg)](#) tests need a Nitrado subscription account 


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
#### 1. [Introduction](https://github.com/mjlomeli/NitradoAPI/wiki#introduction)
   > Shows how to get access to your API key.
#### 2. [Getting Started](https://github.com/mjlomeli/NitradoAPI/wiki/Getting-Started)
   > Shows how to log in to the client and use the basic code interface
#### 3. [Services](https://github.com/mjlomeli/NitradoAPI/wiki/Services)
   > Data provided outside of the game server. Like server status, user id, and auto extension plan.
#### 4. [GameServer](https://github.com/mjlomeli/NitradoAPI/wiki/GameServer)
   > Data directly related to the game server. This includes the player list, game settings, etc.
#### 5. [Games](https://github.com/mjlomeli/NitradoAPI/wiki/Games)
   > Custom game specific libraries.

<br />

# Examples

### Connect the Client
To begin using the API you must have the API key saved as an environment variable.
The identifer must be labeled as `NITRADO_API_KEY`.

```text
NITRADO_API_KEY=123456789abcdefghijklmnop
```

### Saving your API key
If you don't know how to save your API key as an environment variable, run this 
to save it in a `.env` file locally. 

If you already have a `.env` file, this will append the key to the file.

An important rule of thumb is to never save this file publicly. Add it to your 
`.gitignore` file before attempting to upload changes to your repository.

```python
from nitrado import initialize

initialize("your-api-key")
```

### Services
This example highlights how to get the service.

```python
from nitrado import Service

services = Services.all()
print(services)
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



