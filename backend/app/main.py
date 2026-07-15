from fastapi import FastAPI

app = FastAPI(
    title="PPE Safety Platform API",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to PPE Safety Platform API",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health():
    return {"status": "ok"}
