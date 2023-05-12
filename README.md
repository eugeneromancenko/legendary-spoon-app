## Application

The application is a Python mock REST API for emails. It uses
[poetry](https://python-poetry.org/docs/) for dependency management. In case
you're not familiar, poetry takes care of python virtualenvs to avoid dependency
conflicts, and it locks the dependency tree with `poetry.lock` to provide
repeatable builds. The app should have it's dependencies installed with `poetry
install` run from the `src/` folder.

If you'd like to try the app outside of a container first, run:

```
cd src
poetry install
poetry run python manage.py makemigrations
poetry run python manage.py migrate
poetry run python manage.py runserver
```

Then point your browser at http://localhost:8000/
