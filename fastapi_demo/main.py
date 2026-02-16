from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# This is a simple FastAPI application that demonstrates various features such as path parameters, query parameters, request bodies, and response models. You can run this code using Uvicorn to see how it works.

# Create an instance of the FastAPI class, which will be our main application object.
app = FastAPI()

# API 1
# This endpoint is the default route that returns a simple JSON response with a message. You can access it by going to http://localhost:8000/ in your browser or using a tool like curl or Postman.
@app.get("/")
def get_default():
    return {"message": "Hello, World!"}

# API 2
#  This endpoint uses a path parameter to get the user ID and returns a simple JSON response with the user ID and a name.
# Eg: http://localhost:8000/user/123
@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": f"User {user_id}"}

# API 3
# This endpoint demonstrates how to raise an HTTP exception if a certain condition is met (in this case, if the user ID is 3). If the user ID is 3, it will return a 404 Not Found error with a custom message. Otherwise, it will return the user information as before.
@app.get("/users/{user_id}")
def get_user_with_exception(user_id: int):
    if user_id == 3:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"user_id": user_id, "name": f"User {user_id}"}

# API 4
# This endpoint uses a query parameter to search for a user by name and returns a JSON response with the name and a message.
# Eg: http://localhost:8000/searchuser?name=AK
@app.get("/searchuser")
def search_user(name: str):
    return {"name": name, "message": f"Searching for user with name: {name}"}

# API 5
# This endpoint demonstrates how to use a Pydantic model to define the structure of the request body. The User model has two fields: name (a string) and age (an integer). 
# When a POST request is made to this endpoint with a JSON body that matches the User model, it will return a JSON response confirming the creation of the user.
# Request Body with Pydantic model

class User(BaseModel):
    name: str
    age: int

# This endpoint accepts a POST request with a JSON body that matches the User model. It returns a JSON response confirming the creation of the user.
@app.post("/createuser", status_code=201)
def create_user(user: User):
    return {"message": f"User {user.name} created with age {user.age}"}

# API 6
# This endpoint demonstrates how to use a Pydantic model to define the structure of the response. The UserResponse model has three fields: user_id (an integer), name (a string), and age (an integer). 
# When a GET request is made to this endpoint with a user ID, it will return a JSON response

# Response Model with Pydantic
class UserResponse(BaseModel):
    user_id: int
    name: str
    age: int

@app.get("/getuser/{user_id}", response_model=UserResponse)
def get_user_response(user_id: int):
    # In a real application, you would fetch user data from a database
    return UserResponse(user_id=user_id, name=f"User {user_id}", age=20)
