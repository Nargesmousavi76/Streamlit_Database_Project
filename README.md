# 🎬 Movie Database Management System

### 🗄️ Manage your movie collection using Python, SQLite, and Streamlit!

## 📌 About The Project

This project is a simple **Movie Database Management System** developed with Python, SQLite, and Streamlit.

It provides a user-friendly web interface that allows users to manage movie records directly through a Streamlit application.

Users can easily add, search, view, update, and delete movie information using different options in the sidebar.

## ✨ Features

- 📋 View all movie records.
- 🔍 Search movies by ID.
- 🎥 Search movies by title.
- ⭐ Find movies by IMDb rating.
- ➕ Add new movie records.
- 🗑️ Delete movies by ID or title.
- ✏️ Update movie information by ID.
- 🔄 Update movie information by title.
- 🗄️ Store movie data in an SQLite database.
- 🖥️ Interactive web interface using Streamlit.

## 🛠️ Technologies Used

| Technology | Description |
|---|---|
| 🐍 Python | Main programming language |
| 🗄️ SQLite3 | Database management |
| 🎨 Streamlit | Web-based user interface |

## 📂 Project Structure

```text
Movie_Database/
│
├── app.py
├── app_db.py
├── MoviesData.db
└── README.md
```

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Install the required library**

```bash
pip install streamlit
```

**3. Run the application**

```bash
streamlit run app.py
```

## 🗃️ Database Structure

The project uses SQLite to store movie information in a database named `MoviesData.db`.

The `movies` table contains the following fields:

| Column | Data Type | Description |
|---|---|---|
| `id` | INTEGER | Unique movie ID |
| `title` | TEXT | Movie title |
| `year` | TEXT | Release year |
| `country` | TEXT | Movie country |
| `imdb_rate` | REAL | IMDb rating |

## 🖥️ Application Interface

The application provides different options through the sidebar:

- **SELECT ALL RECORDS:** Display all movies.
- **SELECT RECORD BY ID:** Find a movie using its ID.
- **SELECT RECORD BY TITLE:** Search by movie title.
- **SELECT RECORD BY IMDB_RATE:** Find movies with a specific IMDb rating.
- **INSERT RECORD:** Add a new movie.
- **DELETE RECORD BY ID:** Remove a movie using its ID.
- **DELETE RECORD BY TITLE:** Remove a movie using its title.
- **UPDATE RECORD BY ID:** Update a movie's year and IMDb rating.
- **UPDATE RECORD BY TITLE:** Update a movie's year, country, and IMDb rating.

## 🎯 Project Goals

Through this project, I practiced:

- Creating and managing SQLite databases.
- Writing SQL queries.
- Implementing CRUD operations.
- Connecting Python applications to databases.
- Building interactive web applications with Streamlit.
- Working with user inputs and buttons in Streamlit.

---

### 💻 Developed with Python ❤️

⭐ Thanks for visiting this project!
