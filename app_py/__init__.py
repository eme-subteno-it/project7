from flask import Flask
from .     import models

@app.cli.command()
def index():
    index()