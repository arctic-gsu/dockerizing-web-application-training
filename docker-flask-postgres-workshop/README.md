## Clone the repo

## Change the following files in the app folder

- docker-compose.yml: Edit services stimsina-web, stimsina-db and environment variable DATABASE_URL
- config.py: Edit SQLALCHEMY_DATABASE_URI with yourusername-db in place of stimsina-db


## Build the docker image
```
docker compose up -d
```

## Check the docker images built

```
docker images
```

## Check the running container
```
docker ps
```

## Stop the running container
```
docker stop CONTAINERID
```

## Delete the docker images
```
docker rmi -f IMAGEID
```

## Tag docker images
Change stimsina-web to yourusername-web 
```
docker tag docker-flask-postgres-workshop-stimsina-web:latest harbor.rs.gsu.edu/training/stimsina-web:0.0.1
```

## Login to docker registry

```
docker login harbor.rs.gsu.edu -u 'username' -p 'password' 
```

## Push images to docker registry
Change stimsina-web to yourusername-web 

```
docker push harbor.rs.gsu.edu/training/stimsina-web:0.0.1 
```