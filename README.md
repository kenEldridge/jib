# coding_challenge
Various programming exercises

# Start the notebook server
```
docker kill nb; docker rm nb; docker run -p 8888:8888 --name nb -v "$(pwd)"/notebooks:/home/jovyan nb
```
Should probably use docker-compose
