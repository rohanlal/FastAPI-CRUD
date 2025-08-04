from fastapi import FastAPI, Depends

app = FastAPI()

class Database:
    def get_dbConnection(self):
        # Simulate a database connection
        return "Database connection established"
    
    def close_dbConnection(self):
        # Simulate closing the database connection
        return "Database connection closed"

def get_database():
    db = Database()
    try:
        yield db.get_dbConnection()
    finally:
        db.close_dbConnection()

        
@app.get("/test-db")
def test_db(db= Depends(get_database)):
    return {"message": "Database connection successful", "db": db}