This project helps you to learn the basics of FastAPI in Python.

Pre-requisites:
Install:
Python
VS Code

Clone this project in your local system and open in VS Code.

Clone Command:
Execute the below command in a folder where you want this project to be cloned.

git clone -b feature/develop https://github.com/Ajithkumar-Explores/AI-ML.git

Then, open the project in VS Code.
Then, open a Terminal in VS Code and execute the below command to install the packages.

Install Command:

pip install fastapi uvicorn pydantic

To run the app:

In the Terminal, execute the below command.

Run Command:

uvicorn main:app --reload

Once the app is running, open the below mentioned URL to see and call the APIs.

Swagger URL:
http://localhost:8000/docs

To run the APIs in the URL, click on "Try it out" button under each API and then click "Execute".
If any parameter is required, Eg. user_id, enter a number in that field and then click "Execute".
Eg. user_id: 1
