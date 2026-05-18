# Django To-Do CRUD Project — Run Guide & File Map

This project is a small Django app that implements CRUD (Create, Read, Update, Delete) for a **Task** model.

---

## 1) How to run the entire project

### A. Create/activate a virtual environment (recommended)
From:
`c:/Users/mark0/OneDrive/Desktop/Code College/Python/Python_Tutorials/Django Project`

```bat
python -m venv ll_env
ll_env\Scripts\activate
```

### B. Install dependencies
```bat
pip install Django
```

### C. Run migrations
```bat
python manage.py makemigrations
python manage.py migrate
```

### D. Start the dev server
```bat
python manage.py runserver
```

Open in browser:
- App: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

---

## 2) What this project does (CRUD)

The app `tasks` provides these routes (relative to site root):
- `GET /` → list all tasks (`task_list`)
- `GET /new/` → show create form (`task_create`)
- `POST /new/` → create task (then redirects to list)
- `GET /<id>/` → view one task (`task_detail`)
- `GET /<id>/edit/` → show edit form (`task_update`)
- `POST /<id>/edit/` → save task changes (redirect to detail)
- `GET /<id>/delete/` → show delete confirmation (`task_delete`)
- `POST /<id>/delete/` → delete and redirect to list

---

## 3) File-by-file: what each element is responsible for

### Project root
#### `todoproject/settings.py`
- Django configuration.
- Key part for this project:
  - `INSTALLED_APPS` must include `tasks`.

**If missing/incorrect:**
- Django won’t register your models/templates/admin.
- You may get errors like “App not installed” or missing migrations.

#### `todoproject/urls.py`
- The URL router for the whole site.
- This project must route root paths to the app:
  - `path('', include('tasks.urls'))`

**If missing/incorrect:**
- `/new/` and the CRUD pages will return **404** even if the app code exists.

#### `todoproject/wsgi.py` / `todoproject/asgi.py`
- Entry points for deploying/running under WSGI/ASGI.

**If missing:**
- Dev server might fail (less common in this setup).

---

### App: `tasks/`

#### `tasks/models.py`
- Defines the database model:
  - `Task` with fields: `title`, `completed`, `created_at`, `updated_at`.

**If missing/incorrect:**
- No database tables for tasks.
- CRUD views will fail when querying/saving.

#### `tasks/admin.py`
- Registers `Task` in Django admin.

**If missing:**
- Admin UI won’t show your Task model, but the app still works.

#### `tasks/apps.py`
- App configuration (mainly the app name).

**If incorrect:**
- Django may fail to load the app.

#### `tasks/forms.py`
- Defines `TaskForm` (used for create/update screens).

**If missing:**
- `/new/` and `/edit/` pages won’t be able to validate/save input.

#### `tasks/views.py`
- Implements the handlers for all CRUD operations.
- Uses:
  - `render()` to show templates
  - `redirect()` after POST
  - `get_object_or_404()` for safe detail/edit/delete

**If missing:**
- Routes will exist but return errors when accessed.

#### `tasks/urls.py`
- The app’s URL patterns.

**If missing/incorrect:**
- `/`, `/new/`, `/<id>/edit/`, etc. won’t map to the correct view.

#### `tasks/templates/tasks/*.html`
These templates are rendered by the views.
- `task_list.html` — list of tasks
- `task_form.html` — create/update form
- `task_detail.html` — single task display
- `task_confirm_delete.html` — delete confirmation

**If templates are missing:**
- You’ll get template errors (often 500 errors) when browsing those pages.

---

### `TODO.md` (in this project folder)
- A checklist describing the steps for building the project.

---

## 4) Common issues

### 404 on `/new/`
Cause: `todoproject/urls.py` not including `tasks.urls`.
Fix: ensure:
- `path('', include('tasks.urls'))`

### Migrations not applied
Cause: forgot `makemigrations` / `migrate`.
Fix:
```bat
python manage.py makemigrations
python manage.py migrate
```

### Template errors
Cause: missing or misnamed templates.
Fix: check `tasks/templates/tasks/` file names match what views render.

---

## 5) How to extend the project (ideas)
- Add validation rules (e.g., required title, length limit UX)
- Add pagination for task list
- Add user ownership (requires auth + model changes)
- Add Bootstrap styling (UI enhancement)


