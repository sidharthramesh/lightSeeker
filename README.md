# Light Seeker
Simulates an environment with agent and light

## Installation
Have python3 installed with virtualenv, clone the repository.
```
cd lightSeeker
virtualenv venv
```
Activate Virtual Environment
```
venv\Scripts\activate.bat
```
Install dependencies
```
pip install -r requirements.txt
```
Run migration, initialization scripts
```
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```
Run server 
```
python serve.py
```
## API Usage

### POST /simulations/
Creates a new instance of a simulation with random position for light and agent. The app can support multiple simulation instances limited only by the database throughput. Use postgres or MySQL for more than training more than 500 simulations simultaneously. 

`brightness` (optional): Float64 : The brightness of the light

`torque` (optional): Float64 : The turning speed

`speed` (optional)

Response will contain pk (Primary key) that is required for other requests

### GET /simulations/pk/
Gets the state of the simulation environment. The visualization tool does this for you.

### PUT /simulations/pk/
A request takes a step on the simulation environment

`right` (required): Bool : Right wheel on/of

`left` (required): Bool : Left wheel on/of

### DELETE /simulations/pk/
Deletes the instance of simulation

## Visualization Tool
After creating a simulation with a POST request, visit localhost:8000/pk/