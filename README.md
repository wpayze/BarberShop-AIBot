# BarberShop-AIBot (Windows Setup)

## Requirements
- Python 3.11+ installed and on PATH
- PowerShell with script execution allowed for virtualenv activation

## Create and activate a virtual environment
```powershell
python -m venv .venv
# PowerShell
.\.venv\Scripts\Activate.ps1
# Command Prompt
.\.venv\Scripts\activate.bat
```

## Install dependencies
```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

## Run the FastAPI app (dev)
```powershell
uvicorn app.main:app --reload
```

The hello endpoint will be at http://127.0.0.1:8000/ and /docs will expose the interactive API docs.

## Migrations (when you add a migration tool)
We are not generating migrations in this scaffold. Once you choose a migration tool (e.g., Alembic), set it up and then:
- Initialize your migration config (e.g., `alembic init migrations`).
- Create a migration after updating models: `alembic revision --autogenerate -m "describe change"`.
- Apply migrations: `alembic upgrade head`.

Keep migration commands in the project root so paths resolve correctly.
