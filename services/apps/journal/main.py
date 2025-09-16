# Journal Service (Main)
import uvicorn
from .src.routes import app

# Run the application
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
