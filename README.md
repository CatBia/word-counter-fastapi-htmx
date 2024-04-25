# Word Counter example project:
This project is a flask-htmx project to exemplify the capabilities os a simple template and API

## Architecture

This project has a layered architeture, with Presentation and business rules layer.

Each layer is organized by folders and files:

### Presentation Layer
I the laywer hwere the web application will send/receive requests.
#### Routers
The routers file is, in this case, the outbound file with two exposed endpoint:

## Tests:
This project has some tests to verify the 
##### `/` the Root 
Returns the main template

METHOD: GET
Response: HTML content with the html

##### `/word-counter`
Return the word count sent via Form data

METHOD: POST
BODY: `{"text": str}`
HEADERS: `{"content-type": "application/x-www-form-urlencoded"}`
Response: An integer or str

##### `/docs`
Auto generated docs via FastAPI framework. Please access [FastAPI documentation](https://fastapi.tiangolo.com/) fro more information

## How to build a development environment
### Install Docker at your machine
Access [Docker's installation page](https://docs.docker.com/engine/install/) and follow the instructions to install Docker in your machine
_Tip: Pay special attention to the "Docker User" step. This configuration is important if you're not your own machine administrator/root and file created inside the machine_
### Install GNU's Make tool
Make is a well-known, older than 70% of the SWE community on this blue rock, amazing tool (i'm biased, i knnow!)._Is a build automation tool that builds executable programs and libraries from source code by reading files called makefiles which specify how to derive the target program._[Wikipedia Make's page](https://en.wikipedia.org/wiki/Make_(software)). 
#### `Make` for Windows
Access [GNUWin32 Make's page](https://gnuwin32.sourceforge.net/packages/make.htm) and follow the instructions
OR
Access [Chocolatey - The Windows Package Manager](https://chocolatey.org/) and follow the instructions to install this tool and [this instrutions](https://community.chocolatey.org/packages/make) to install `Make`. (Developer's First Choice!🥇)
### Execute the build instuctions
At the project's folder. exeecure the following instruction:
```
make build
```
### To open the developer's environment have a bash playground:
At the project's folder. exeecure the following instruction:
```
make dev
```
### To execute the unit tests:
At the project's folder. execute the following instruction:
```
make test
```
### To execute the Django server:
At the project's folder. exeecure the following instruction:
```
make up
```
The web platform will be served at the following address:
```
0.0.0.0:8000
```
Please read the API Doc section to see all available endpoints