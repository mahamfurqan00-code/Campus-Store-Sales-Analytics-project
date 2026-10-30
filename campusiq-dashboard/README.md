# CampusIQ — Sales Analytics Dashboard

A responsive portfolio dashboard built with Flask, Pandas, NumPy, HTML, CSS, JavaScript and Chart.js.

## Features
- Revenue, profit, order count and units sold KPIs
- Monthly revenue and profit trends
- Category and regional breakdowns
- Top products table
- Date, category and region filters
- Filtered CSV export
- Flask JSON API and health endpoint
- Analytics unit tests
- 360 synthetic demo sales records

## Run locally
Python 3.10+ recommended.

```bash
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000.

## Tests
```bash
pytest -q
```

## API
- `GET /api/dashboard`
- `GET /api/dashboard?category=Electronics&region=North`
- `GET /api/export`
- `GET /health`

Optional query filters: `start`, `end`, `category`, `region`.

Dataset is synthetic demo data, not real customer information.
