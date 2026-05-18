# Django To-Do CRUD Project — Run + File Explanations

This document explains **how to run the entire project** and what **each important file** does. It also explains what typically happens if a file (or key line) is missing.

---

## 1) Run the full project

### Step A — Go to the Django project folder

```bat
cd "c:/Users/mark0/OneDrive/Desktop/Code College/Python/Python_Tutorials/Django Project"
```

### Step B — Create and activate a virtual environment

```bat
python -m venv ll_env
ll_env\Scripts\activate
```

### Step C — Install Django

```bat
pip install Django
```

### Step D — Apply migrations

```bat
python manage.py makemigrations
python manage.py migrate
```

### Step E — Start the server

```bat
python manage.py runserver
```

### Step F — Open URLs in your browser

- App list: http://127.0.0.1:8000/
- App create: http://127.0.0.1:8000/new/
- Admin (optional): http://127.0.0.1:8000/admin/

---

## 2) App behavior (CRUD endpoints)

All CRUD routes are provided by the `tasks` app and mounted at the site root.

Relative URLs:

- `GET /` → list tasks
- `GET /new/` → show create form
- `POST /new/` → create a task and redirect
- `GET /<id>/` → show a task detail page
- `GET /<id>/edit/` → show update form
- `POST /<id>/edit/` → update task and redirect
- `GET /<id>/delete/` → show delete confirmation
- `POST /<id>/delete/` → delete task and redirect

---

## 3) File-by-file: what each element does

### A) Top-level project folder: `todoproject/`

#### `todoproject/settings.py`

- Django settings (debug, installed apps, templates, database, etc.)
- Most important for this project: `INSTALLED_APPS` must include `tasks`.

If `tasks` is missing:

- Model/tables won’t be registered
- Migrations won’t be created for `Task`
- Admin and templates won’t work for the app

#### `todoproject/urls.py`

- Site-wide URL routing.
- Must include the tasks URLs so `/`, `/new/`, and the CRUD paths reach the correct views.

Expected key line:

- `path('', include('tasks.urls'))`

If this line is missing/incorrect:

- You’ll see **404 Not Found** for `/new/`, `/1/`, etc.

#### `todoproject/wsgi.py` / `todoproject/asgi.py`

- Standard Django entrypoints for running.

If missing:

- Running/deploying may fail (less likely for your local dev workflow).

---

### B) App folder: `tasks/`

#### `tasks/models.py`

- Defines the `Task` model stored in SQLite.

If missing/incorrect:

- Database table won’t exist
- Views that query/save tasks fail

#### `tasks/admin.py`

- Registers `Task` with Django admin.

If missing:

- Admin won’t show the Task model (but the site CRUD pages can still work)

#### `tasks/forms.py`

- Defines `TaskForm` used by create/update views.

If missing/incorrect:

- `/new/` and `/edit/` will error or won’t validate input

#### `tasks/views.py`

- Implements the CRUD logic:
  - `task_list`
  - `task_create`
  - `task_detail`
  - `task_update`
  - `task_delete`

If missing:

- Routes may exist but will error when accessed

#### `tasks/urls.py`

- URL patterns for the app.

If missing/incorrect:

- `/`, `/new/`, `/<id>/edit/`, etc. won’t map to the right views

#### `tasks/templates/tasks/*.html`

- Templates rendered by the views.

If any template is missing:

- The page that renders it will raise a template error (500)

Required templates:

- `task_list.html`
- `task_form.html`
- `task_detail.html`
- `task_confirm_delete.html`

---

## 4) Database files

- SQLite database is stored at: `todoproject/db.sqlite3`

If migrations haven’t been applied:

- Views that use the database may fail

---

## 5) Quick troubleshooting

### 404 for `/new/`

- Usually means `todoproject/urls.py` is not including `tasks.urls`.

### Template errors

- Usually means missing or misnamed files in `tasks/templates/tasks/`.

### “No such column …” after model changes

- You need to re-run migrations:

```bat
python manage.py makemigrations tasks
python manage.py migrate
```

---

## Notes

- If you add new fields to `Task`, you must migrate.
- If you rename templates, you must update the view render() calls accordingly.
