"""
Very basic python app to get sum of 2 numbers
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/sum/{left}/{right}")
def root(left, right):
    """Some doc goes here"""
    try:
        return {"sum": float(left) + float(right)}
    except ValueError:
        return {"error": "valid numbers are required"}
