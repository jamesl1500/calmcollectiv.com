# Journal Service (Main)
import uvicorn
from backend.services.journal.src.routes import app


def main():
    """Start the Journal Service."""
    uvicorn.run(
        app=app,
        host="localhost",
        port=8000,
        reload=True
    )


if __name__ == "__main__":
    main()
