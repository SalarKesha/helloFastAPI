import uvicorn

# models.Base.metadata.create_all(bind=engine)
if __name__ == "__main__":
    uvicorn.run(app='config:app', host='127.0.0.1', port=8000, reload=True)
