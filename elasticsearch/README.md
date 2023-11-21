# Instructions to setup Elasticsearch-Kibana-EnterpriseSearch in Local using docker

-----------------------------------------------------------------------------
The instructions in this file is following from instructions from this link, just in case there are some updates or more info needed.
https://www.elastic.co/guide/en/enterprise-search/current/docker.html#docker-compose-example


## Prerequisites:
- Docker engine and Docker compose are installed. Check if they are installed, open Terminal and try these commands
```
$docker -v
Docker version 20.10.13, build a224086

$docker-compose -v
docker-compose version 1.29.2, build 5becea4c
```

If these commands don't return a valid version then you can proceed to install them, which is not included in these instructions.


## Steps to install:
### 1/ .env file: 
- Create ".env" file in the same folder with docker-compose.yml file.
- Content of the ".env" file is in "env_sample.txt".
- Optionally you can change the password or the Memory limit.

### 2/ docker-compose.yml file: 
- Create "docker-compose.yml" file in the same folder with ".env" file.
- Content of the "docker-compose.yml" file is in "docker-compose_sample.yml"

### 3/ Increase max_map_count ( otherwise ES will crash with code 137 because of lacking memory)
```
MAC/Linux
$sysctl -w vm.max_map_count=262144

WINDOWS
$wsl -d docker-desktop
$sysctl -w vm.max_map_count=262144
```

### 4/ Run docker
- Open terminal and change directory to /elasticsearch (where docker-compose.yml is locating)
- Run
```
$docker-compose up --remove-orphans

/// This will run the setup configured in docker-compose, including fetching images and running the containers so it will take a bit of time, about 15-30min

/// It is done when these lines appear in the terminal
enterprisesearch_1  | In a few moments, you'll be able to access Enterprise Search from Kibana at the following address:
enterprisesearch_1  |
enterprisesearch_1  |   * Kibana URL: http://kibana:5601/app/enterprise_search/overview
enterprisesearch_1  |
enterprisesearch_1  | If this is your first time starting Enterprise Search, check the console output above for your user authentication credentials.
enterprisesearch_1  |
enterprisesearch_1  | Visit the documentation: https://www.elastic.co/guide/en/enterprise-search/master/index.html
enterprisesearch_1  |
enterprisesearch_1  |
enterprisesearch_1  | WARNING: A new secret session key has been generated.
enterprisesearch_1  |
enterprisesearch_1  | Set the key in your config file to persist user sessions through process restarts:
enterprisesearch_1  |
enterprisesearch_1  | secret_session_key:

```

### 5/ Check if everything is working
- Open browser at localhost:5601
- Login , username: elastic , password: ELASTIC_PASSWORD in .env file

### 6/ Stop Elasticsearch:
- Once 3 containers are created and running, you can stop them just like stopping normal containers
- Option 1, stop containers by using Docker Desktop
- Option 2, using Terminal
```
docker container stop CONTAINER_NAME_OR_ID
```

### 7/ Run again Elasticsearch
- You may need to "Increase max_map_count" in step 3 everytime your computer is started or in case Elasticsearch container is not up and running
- Open Docker Desktop and turn on Es01, Kibana and Enterprisesearch.
