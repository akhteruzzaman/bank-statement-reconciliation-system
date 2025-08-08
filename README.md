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


## 🧾 CSV Upload Format

The file must contain the following columns:

- `company` (text)
- `description` (text)
- `amount` (float)
- `reference_number` (text)
- `invoice_no` (text)
- `date` (YYYY-MM-DD)
- `status` (Matched / Unmatched)

### Example:

| company     | description              | amount  | reference_number | invoice_no | date       | status     |
|-------------|--------------------------|---------|------------------|------------|------------|------------|
| Client A    | Payment for services      | 500.00  | REF12345         | INV1001    | 2024-12-15 | Matched    |
| Office Rent | January Rent Payment      | -250.00 | REF67890         | INV1002    | 2025-01-10 | Unmatched  |


---

## ⚙️ Tech Stack

- **Backend**: Django, Python
- **Database**: PostgreSQL
- **Machine Learning**: PyTorch
- **Containerization**: Docker + Docker Compose

---

## 🐳 How to Run (Docker)

```bash
# Build and start containers
docker-compose up --build

# Run migrations
docker exec -it bsrs-web-1 python manage.py migrate

# Open app in browser
http://localhost:8000/bank_transactions/
http://localhost:8000/upload/
