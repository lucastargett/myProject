from fastapi import FastAPI

app = FastAPI(
    title="Strength Training API",
    description="Backend API for the intelligent strength-training platform.",
    version="0.1.0"
)

@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Strength Training API is running"}

@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"status": "healthy"}