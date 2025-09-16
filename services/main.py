# MH Website Backend
import multiprocessing
import uvicorn
from typing import Dict, List

# Service configurations
SERVICES = [
    {
        "name": "journal",
        "module": "services.journal.main:app",
        "host": "localhost",
        "port": 8000
    }
    # Add more services here as needed
]

def start_service(service_config: Dict) -> None:
    """Start a FastAPI service with given configuration."""
    uvicorn.run(
        app=service_config["module"],
        host=service_config["host"],
        port=service_config["port"],
        reload=True
    )

def main():
    """Start all FastAPI services in parallel using multiprocessing."""
    processes: List[multiprocessing.Process] = []

    # Create and start process for each service
    for service in SERVICES:
        process = multiprocessing.Process(
            target=start_service,
            args=(service,),
            name=f"Service-{service['name']}"
        )
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

if __name__ == "__main__":
    main()
