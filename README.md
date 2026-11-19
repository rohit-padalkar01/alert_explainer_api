# Alert Explainer API

A FastAPI service for storing alerts and generating rule-based explanations of their metrics and recommended next steps.

## Project Structure

```text
database.py       SQLite engine, session, and database base
main.py           FastAPI application and root endpoint
models.py         Alert database model
schemas.py        Request and response schemas
routers/alerts.py Alert and explanation endpoints
services/explainer.py  Rule-based explanation generator
test_alerts.py    API tests
requirements.txt  Application dependencies
docs/adr/         Architecture decision records
```

## Alert Fields

| Field | Type | Description |
| --- | --- | --- |
| `id` | integer | Database-generated alert ID. |
| `title` | string | Alert title. |
| `severity` | string | One of `critical`, `warning`, or `info`. |
| `source` | string | Alert source. |
| `metric_name` | string | Name of the metric. |
| `metric_value` | number | Current metric value. |
| `threshold` | number | Metric threshold. |
| `created_at` | datetime | Alert creation timestamp. |

Supply all fields except `id` and `created_at` when creating an alert.

## Endpoints

| Method | Path | Description | Status codes |
| --- | --- | --- | --- |
| GET | `/` | Return the service status. | 200 |
| POST | `/alerts/` | Create an alert. | 201 created, 422 invalid request |
| GET | `/alerts/` | List alerts ordered by ID. | 200 |
| GET | `/alerts/{alert_id}` | Retrieve an alert. | 200, 404 not found, 422 invalid ID |
| GET | `/alerts/{alert_id}/explain` | Generate an explanation. | 200, 404 not found, 422 invalid ID |
| POST | `/alerts/{alert_id}/explain` | Generate an explanation. | 200, 404 not found, 422 invalid ID |

Both explanation methods return `alert_id`, `explanation`, and `generated_at`.
Unexpected server errors can return 500.

FastAPI also provides `GET /docs`, `GET /redoc`, `GET /openapi.json`, and `GET /docs/oauth2-redirect`, each returning 200 on success.

## Install and Run on Windows

From the project directory in PowerShell, with Python installed:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` and retry activation. The API is available at `http://127.0.0.1:8000`, with interactive documentation at `http://127.0.0.1:8000/docs`. The application creates `alerts.db` in the working directory if needed.

## Tests

With the virtual environment activated, install the test dependencies and run:

```powershell
python -m pip install pytest httpx
python -m pytest test_alerts.py -v
```

## Architecture Decisions

- [Rule-Based Explanations](docs/adr/0001-rule-based-explanations.md)
- [Human Approval for Alert Summaries](docs/adr/0002-human-approval-for-alert-summaries.md)