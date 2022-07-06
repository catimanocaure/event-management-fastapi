# event_mgmt_app/main.py

from fastapi import FastAPI

app = FastAPI()

# endpoints

@app.get('/')
def read_root():
    return 'Welcome to Event Management App built with FastAPI.'
