from fastapi import FastAPI

app = FastAPI()


@app.get("/HelloWorld")
def helloworld():
    return "Hello World"


@app.post("/new_user")
def new_user(info: dict):
    name = info.get("name")
    pwd = info.get("password")
    
    with open(name + ".txt", "w") as file:
        file.write(f"name {name}\npassword {pwd}")

    return {"message": "user created"}

@app.post("/whoami")
def whoami(info: dict):
    name = info.get("name")

    userprofile = localdb.get(name)

    if userprofile:
        return userprofile

    return {"error": "user not found"}
