from fastapi import FastAPI
from app.schemas import Currency

app = FastAPI(title="Money Tracker")

transactions_storage = []
current_id = 1

@app.get("/")
def root():
    return {"status": "ok","message": "Ласкаво просимо до Money Tracker!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/transactions")
def transactions(amount_cents :int,currency: Currency,description:str,category:str,date:str,subcategory:str):
    return {"status": "ok",
            "message": "Транзакція додана!",
            "amount":round(amount_cents / 100, 2) ,
            "description" : description,
            "category":category,
            "subcategory":subcategory,
            "currency": currency,
            "date" : date}

@app.get("/transactions")
def get_transactions():
    #  для тестування
    fake_transactions = [
        {
            "id": 1,
            "amount": 10.50,
            "currency": "USD",
            "description": "кава",
            "category": "Особистий розвиток",
            "subcategory": "Курси",
            "date": "2025-01-15"
        }
    ]
    return {"status": "ok", "transactions": fake_transactions}