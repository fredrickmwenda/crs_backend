# 🧾 Cashier Record System (CRS)

A web-based Cashier Record System built with **Django + Django REST Framework**, designed to manage attendants, cash drop records, card assignments, and user authentication via sessions and tokens. Ideal for businesses tracking cash deposits by staff using card-linked sessions and shift-based reporting.

---

## 🚀 Features

- 🔐 **Authentication & Sessions**
  - JWT + session-based login
  - Auto logout after 5 mins of inactivity

- 👥 **User Management**
  - Admin-created users via dashboard
  - Role-based access (admin, supervisor, auditor)
  - Email invite with profile update on first login

- 🧑‍💼 **Attendant Module**
  - Standalone (not linked to `User`)
  - Tracks full name, contact info
  - Assign/revoke access cards
  - View assignment history with timestamps

- 🪪 **Card Management**
  - Track card status (assigned/unassigned)
  - Assign to only one attendant at a time
  - Full audit trail via pivot table

- 💸 **Drop File Module**
  - Upload CSVs of cash drops
  - Auto-match entries to attendants via cards
  - View unmatched entries for manual assignment

- 📜 **Drop Entries & Reporting**
  - View all drop records
  - Filter by attendant, card, date, matched
  - Export options (CSV/PDF) *(optional feature)*

---

## 📁 Folder Structure

crs_backend/
├── apps/
│ ├── users/ # Auth, registration, roles
│ ├── attendants/ # Attendant logic, card history
│ ├── cards/ # Card model and assignment
│ ├── drops/ # CSV file upload + DropEntry
│ └── core/ # Common utilities (e.g. session timeout)


---

## ⚙️ Installation

```bash
# 1. Clone the repo
git clone https://github.com/your-org/cashier-record-system.git
cd cashier-record-system

# 2. Create a virtual environment
python -m venv env
source env/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create database
python manage.py makemigrations
python manage.py migrate

# 5. Create superuser
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver


🛡️ Security & Session Timeout
User is auto-logged out after 5 minutes of inactivity using custom middleware:
middleware.SessionTimeoutMiddleware

📦 API Overview (REST)
| Endpoint                            | Method   | Description                                 |
| ----------------------------------- | -------- | ------------------------------------------- |
| `/api/auth/login/`                  | POST     | Login                                       |
| `/api/auth/logout/`                 | POST     | Logout                                      |
| `/api/users/`                       | GET/POST | Admin manage users                          |
| `/api/attendants/`                  | CRUD     | Manage attendants                           |
| `/api/attendants/<id>/assign-card/` | POST     | Assign card                                 |
| `/api/attendants/<id>/revoke-card/` | POST     | Revoke card                                 |
| `/api/cards/`                       | GET      | Card list                                   |
| `/api/drops/upload/`                | POST     | Upload CSV drop file                        |
| `/api/drops/entries/`               | GET      | Drop list, filter by attendant/card         |
| `/api/drops/<id>/manual-assign/`    | PATCH    | Manually assign unmatched drop *(optional)* |

