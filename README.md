# Dream
Attack!

# Start the notebook server
```
docker kill nb; docker rm nb; docker run -p 8888:8888 --name nb -v "$(pwd)"/notebooks:/home/jovyan nb
```