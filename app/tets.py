from app.schemas import Currency,OperationType,validate_category_pair,ALL_CATEGORIES


def categories():
    return {"status":"ok","categories":ALL_CATEGORIES.keys()}