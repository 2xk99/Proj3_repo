# 🌍 AI Travel Recommendation System

An AI-powered travel recommendation application that uses **semantic search** and **sentence embeddings** to recommend destinations based on user preferences.

The system stores destination data in **PostgreSQL**, uses **SQLAlchemy Core** for database operations, generates embeddings using **Sentence Transformers**, and finds similar destinations using **cosine similarity**.

---

# 🚀 Features

- ✅ PostgreSQL database integration
- ✅ SQLAlchemy Core database operations
- ✅ Destination data persistence
- ✅ AI text embeddings
- ✅ Semantic similarity search
- ✅ Top destination recommendations
- ✅ Fallback recommendations for unknown inputs
- ✅ Streamlit web interface (planned/implemented)
- ✅ Easy dataset expansion

---

# 🏗️ Project Structure

```
travel_recommendation/

│
├── app.py                 # Main Streamlit application
├── database.py            # PostgreSQL connection
├── models.py              # SQLAlchemy Core table definitions
├── destinations.py        # Destination dataset
├── create_tables.py       # Create database tables
├── seed_database.py       # Insert destinations and embeddings
├── search.py              # AI recommendation logic
│
├── venv/                  # Python virtual environment
│
└── README.md
```

---

# 🛠️ Technologies Used

## Backend
- Python
- PostgreSQL
- SQLAlchemy Core
- Psycopg2

## AI / Machine Learning
- Sentence Transformers
- all-MiniLM-L6-v2 embedding model
- Cosine similarity

## Frontend
- Streamlit

---

# ⚙️ Installation

## 1. Clone the project

```bash
git clone <repository-url>

cd travel_recommendation
```

---

## 2. Create virtual environment

```bash
python -m venv venv
```

Activate:

### Linux / Ubuntu

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install sqlalchemy psycopg2-binary sentence-transformers scikit-learn numpy streamlit
```

---

# 🗄️ Database Setup

## 1. Start PostgreSQL

Check:

```bash
sudo systemctl status postgresql
```

Start if needed:

```bash
sudo systemctl start postgresql
```

---

## 2. Create database

Open PostgreSQL:

```bash
sudo -u postgres psql
```

Create database:

```sql
CREATE DATABASE travel_rec_db;
```

Exit:

```sql
\q
```

---

# 🔌 Database Configuration

Open:

```
database.py
```

Update:

```python
DATABASE_URL = "postgresql://postgres:123456@localhost/travel_rec_db"
```

Change:

- username
- password
- database name

according to your PostgreSQL setup.

---

# 🏗️ Create Database Tables

Run:

```bash
python create_tables.py
```

Expected output:

```
Tables created successfully!
```

This creates:

```
destinations
```

table.

---

# 📥 Insert Destination Data

Run:

```bash
python seed_database.py
```

Expected output:

```
Destinations inserted successfully!
```

This will:

1. Load destination dataset
2. Generate AI embeddings
3. Convert embeddings into bytes
4. Store everything in PostgreSQL

---

# 🔍 Test AI Recommendation

Run:

```bash
python app.py
```

Example input:

```
I want a relaxing beach vacation
```

Example output:

```
Top Recommendations

Name: Bali
Country: Indonesia
Category: Beach
Similarity: 0.82


Name: Maldives
Country: Maldives
Category: Beach
Similarity: 0.79
```

---

# 🧠 How It Works

The application follows this pipeline:

```
User Input
     |
     v
Sentence Transformer Model
     |
     v
Text Embedding Vector
     |
     v
PostgreSQL Stored Embeddings
     |
     v
Cosine Similarity Calculation
     |
     v
Top 3 Recommended Destinations
```

---

# 🔎 Semantic Search Example

Input:

```
romantic trip with beautiful views
```

The system understands the meaning and may recommend:

```
Santorini
Paris
Maldives
```

even if the exact words are not in the descriptions.

---

# 🛟 Fallback System

If the input does not match any destination:

Example:

```
Haya
```

The system returns popular destinations instead of failing.

Example:

```
Popular destinations:

Paris
Bali
Maldives
```

---

# 🌐 Run Streamlit Website

Start the website:

```bash
streamlit run app.py
```

Open:

```
http://localhost:8501
```

---

# 🗃️ Database Preview

Using pgAdmin:

```
Servers
 |
 └── PostgreSQL
      |
      └── Databases
            |
            └── travel_rec_db
                  |
                  └── Schemas
                       |
                       └── public
                            |
                            └── Tables
                                 |
                                 └── destinations
```

---

# 📊 Destination Table

Example:

| id | name | country | category |
|-|-|-|-|
| 1 | Paris | France | Culture |
| 2 | Bali | Indonesia | Beach |
| 3 | Maldives | Maldives | Beach |
| 4 | Tokyo | Japan | City |

---

# 🔮 Future Improvements

## AI Improvements

- Explainable AI:
  - "Recommended because you like beaches and relaxation"

- Similar destination search:
  - "Places similar to Bali"

- AI travel chatbot

---

## Database Improvements

- Alembic migrations
- pgvector integration
- Search history storage
- User preferences

---

## Frontend Improvements

- Destination images
- Maps integration
- Filters
- User accounts
- Favorites

---

# 👨‍💻 Author

AI Travel Recommendation Project

Built with Python, PostgreSQL, SQLAlchemy Core, and Machine Learning.