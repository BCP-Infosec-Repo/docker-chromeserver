# Docker-Chromeserver
Downloadscript and Dockerfile to build a Docker container to run the ChromeDriver as a server.

## Getting Started
Clone the repo and make docker-chromeserver the current active directory. Run the getdriver.py script to download the latest version of the ChromeDriver. Build the docker container afterwards.

### Downloading the latest Chromedriver binary
```
python3 getdriver.py [--platform]
{'version': '2.42', 'platform': 'linux', 'status': 'success'}
```

### Build docker container
Build the docker container and add your own tags. 
```
docker build -t chromedriver -t chromedriver:v2.42
```
