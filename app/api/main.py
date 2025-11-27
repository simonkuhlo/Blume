import uvicorn

host: str = "localhost"
port: int = 8081
debug: bool = True

if __name__ == "__main__":
    uvicorn.run("app:app", host=host, port=port, reload=debug)

