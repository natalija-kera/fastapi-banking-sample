# FastAPI Banking Sample App

This repository contains a sample FastAPI application that simulates a basic banking API using an in-memory store for account data.

## Setup

1. **Clone the Repository:**

    ```bash
    git clone <repo-url>
    cd fastapi-banking-sample
    ```

2. **Install Dependencies:**

    Use pip to install the required packages:
    ```bash
    pip install fastapi uvicorn pydantic
    ```

3. **Run the Application:**

    Start the FastAPI app with:
    ```bash
    uvicorn app:app --reload
    ```

4. **Interact with the API:**

    Open your browser and navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the Swagger UI.

## Your Challenge

### Step 1: Identify and Fix Bugs

Run the app, call these endpoints via Swagger UI or curl/Postman, and note the issues.

### Step 2: Implement the Transfer Endpoint

- **Transfer Endpoint (`POST /account/transfer`):**  
  *Task:* Implement this endpoint so that it transfers funds from a source account to a target account.

### Step 3: Discuss Concurrency

Once the basic functionality is working, we’ll discuss potential issues related to concurrency and race conditions in an in-memory storage scenario, and how these might be mitigated in a real-world application.

Happy coding!
