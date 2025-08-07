# 🏦 Bank Statement Reconciliation System (BSRS)

This is a Django-based system for automating and managing the reconciliation of bank statements. The system uses a trained machine learning model to classify uploaded transactions as **Matched** or **Unmatched**.

---

## 🚀 Features

- ✅ Upload `.csv` or `.xlsx` bank transaction files
- ✅ Auto-validate headers and data schema
- ✅ Predict transaction status (`Matched` / `Unmatched`) using pre-trained ML model
- ✅ Store processed data into PostgreSQL database
- ✅ View all uploaded transactions with their predicted status
- ✅ Simple web UI to manage uploads

---

## 🧾 CSV Upload Format

The file must contain the following columns:

- `amount` (float)
- `transaction_date` (YYYY-MM-DD)
- `description` (text)

### Example:

| amount  | transaction_date | description              |
|---------|------------------|--------------------------|
| 500.00  | 2024-12-15       | Payment from Client A    |
| -250.00 | 2025-01-10       | Office Rent January      |

---

## ⚙️ Tech Stack

- **Backend**: Django, Python
- **Database**: PostgreSQL
- **Machine Learning**: Scikit-learn (pre-trained model)
- **Containerization**: Docker + Docker Compose

---

## 🐳 How to Run (Docker)

```bash
# Build and start containers
docker-compose up --build

# Run migrations
docker exec -it bsrs-web-1 python manage.py migrate

# Open app in browser
[http://localhost:8000/](http://localhost:8000/bank_transactions/)
http://localhost:8000/upload/
