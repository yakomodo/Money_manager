from fastapi import FastAPI
from app.schemas import Currency,OperationType,validate_category_pair,INCOME_CATEGORIES,EXPENSE_CATEGORIES

app = FastAPI(title="Money Tracker")

transactions_storage = []
current_id = 1

def add_transaction(amount_cents, currency, description, category, date, subcategory, user_id):
    global current_id

    transaction = {
        "amount_cents":amount_cents,
        "currency":currency,
        "description":description,
        "category":category,
        "date":date,
        "subcategory":subcategory,
        "user_id":user_id,
        "id" : current_id
    }
    transactions_storage.append(transaction)
    current_id += 1

    return transaction

@app.get("/")
def root():
    return {"status": "ok","message": "Ласкаво просимо до Money Tracker!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/transactions")
def transactions(amount_cents: int, currency: Currency, description: str, category: str, date: str, subcategory: str,
                 operation_type: OperationType, user_id: int):
    if not validate_category_pair(category, subcategory):
        return {"status": "error", "message": "Неправильна комбінація категорії та підкатегорії"}

    # Викликай свою функцію!
    created_transaction = add_transaction(amount_cents, currency, description, category, date, subcategory, user_id)
    return {"status": "ok", "message": "Транзакція додана!", "transaction": created_transaction}

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

@app.get("/categories/{operation_type}")
def get_categories(operation_type: OperationType):
    if operation_type == OperationType.INCOME:
        categories_list = list(INCOME_CATEGORIES.keys())
    else:  # EXPENSE
        categories_list = list(EXPENSE_CATEGORIES.keys())

    return {"status": "ok", "operation_type": operation_type, "categories": categories_list}