from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory account storage: keys are account IDs and values are account balances.
accounts = {}


class Account(BaseModel):
    id: str
    balance: float


class Transaction(BaseModel):
    amount: float


class TransferRequest(BaseModel):
    source_acc_id: str
    target_acc_id: str
    amount: float


@app.get("/accounts")
def list_accounts():
    """
    List all accounts.
    Returns:
        A JSON object containing all account IDs and their balances.
    """
    # Returns the entire in-memory accounts dictionary.
    return {"accounts": accounts}


@app.post("/account")
def create_account(account: Account):
    accounts[account.id] = account.balance
    return {"message": f"Account {account.id} created with balance {account.balance}"}


@app.post("/account/{account_id}/withdraw")
def withdraw(account_id: str, transaction: Transaction):
    accounts[account_id] -= transaction.amount
    return {
        "message": f"Withdrew {transaction.amount} from account {account_id}",
        "balance": accounts[account_id],
    }


@app.post("/account/transfer")
def transfer(transfer_request: TransferRequest):
    # TODO: Implement the transfer functionality.
    raise HTTPException(status_code=501, detail="Not implemented yet")


if __name__ == "__main__":
    import uvicorn

    # Note: Running in debug mode is acceptable for this exercise.
    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True)
