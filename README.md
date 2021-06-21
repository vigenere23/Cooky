# Cooky

Welcome to Cooky, the amazing recipe sharing app that let's you buy ingredients on the go!

![cooky](https://user-images.githubusercontent.com/32545895/78456681-1858a280-7673-11ea-9ddd-ba089f6616f3.png)

## Database

### Preparing and executing

**Windows (on bash only)**:

```bash
./scripts/win-start-docker.sh
```

**Linux / Mac**

```bash
./scripts/start-docker.sh
```

### Populating (on bash only)

```bash
./scripts/init-database.sh
```

## Server

### Preparing

```bash
cd app
pip3 install -r requirements.txt
```

### Executing

```bash
gunicorn app:app -b 0.0.0.0:5000 -w 1 --log-level debug
```

#### Without async support (NOT RECOMMENDED)

```bash
flask run
```

> WARNING : This methods will not work with the UI since it is based on multiple asynchroneous calls, which is not supported with the basic Flask server. 

## UI

### Peparing

```bash
cd ui
yarn install
```

> Note: This might take a while since some of the packages are quite huge. 

### Executing

```bash
cd ui
yarn serve
```

## Using Docker

With docker, the setup should be way easier, especially since it runs on Linux so it supports Gunicorn. All you have to do is running `docker-compose up` inside the root folder of the project. 

### Exposed ports

* MySQL DB : 32000
* Flask API : 8090
* VueJS UI : 8000

You can connect to those with localhost, 0.0.0.0, 127.0.0.1 or your docker-machine IP (depending or your OS).

### Connecting the UI

For now, only the server and the database are (successfully) connected inside the docker network. However, you can still use the UI like you normally would, outside the container. Just replace `yarn serve` by `yarn serve-docker` once the container is up. 

### Known problems

* The database initiation process fails on Windows, which means it will not be usable on that platform.

## Team members

* Gabriel St-Pierre (me)
* Olivier Gingras

## Screenshots

![Cooky screenshot 1](https://user-images.githubusercontent.com/32545895/72568296-d2ffb280-3885-11ea-8338-9c9d1f03b47c.png)
![Cooky screenshot 2](https://user-images.githubusercontent.com/32545895/72568223-a055ba00-3885-11ea-84c2-daaf5780dd19.png)
![Cooky screenshot 3](https://user-images.githubusercontent.com/32545895/72568425-1f4af280-3886-11ea-9a93-9b5053651ffd.png)
![Cooky screenshot 4](https://user-images.githubusercontent.com/32545895/72568500-499cb000-3886-11ea-8934-d37a8fdbb822.png)
