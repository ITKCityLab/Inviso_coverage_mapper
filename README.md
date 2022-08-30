
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

## Data packages
The API is setup to accept data packages as JSON with the following structure (below is an example package):

{
  "adr": true, 
  "data": {
        "latitudeDeg": 00.1622157,
        "longitudeDeg": 00.2103446,
		}
  "devEUI": "70b3d5705000bf80", 
  "rxInfo": [
    {
      "name": "name-of-your-gateway",
      "rssi": -118,
      "time": "2022-02-14T19:58:05.227037Z",
      "loRaSNR": 4.2,
      "location": {
        "altitude": 49, 
        "latitude": 00.237042,
        "longitude": 00.230753 
      },
      "gatewayID": "1234567891234567"
    }
  ],
  "txInfo": {
    "dr": 5,
    "frequency": 867300000
  },
  "deviceName": "name-device-providing-the-measurement", 
}
