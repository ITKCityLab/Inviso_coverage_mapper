
# Inviso coverage mapper
Inviso stores and visualize loraWAN signal quality.  
This code is delivered as a Docker container for easy deployment.

Your devices send antenna data to the API as HTTP POST. SCORE stores the data in a SQL database and visualizes it in your browser.

API build with [FastAPI](https://fastapi.tiangolo.com/)  
IoT Sensor data persisted on PostgreSQL. The Database files are accessible in the docker volume.


## Requirements
Docker Engine, Docker-compose

## How to set up
Get your favourite server with Docker on it.
Depending on your network setup, reverse proxy to the following containers:
 - port 6660: API
 - port 8080: Adminer SQL interface. (Optional)
 - port 5432: PostgreSQL
 - port 6661: Grafana

## Build & Run
Start project with  `docker-compose -f docker-compose.yml up -d --build`

Connect to sql admin interface at localhost:8080

Explore API at localhost:6660/docs

Stop and delete all data: `docker-compose -f docker-compose.yml down -v`

## Development & testing
Some components require environment variables before running:
 - FastAPI: `INVISO_DB_CONN` (for the SQL connection).

