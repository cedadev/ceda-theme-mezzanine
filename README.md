# ceda-theme-mezzanine

Django app providing customisation of the base templates for use with
CEDA websites deployed using the Mezzanine content management system.

The base template base.html is intended to override the default mezzanine base.html
but itself extends layout.html from the "ceda_theme" package of ceda-theme-django
(https://github.com/cedadev/ceda-theme-django)

## Installation

`ceda-theme-mezzanine` can be installed directly from Github using pip, e.g. into an existing `venv`:

```
$ virtualenv --no-site-packages ./venv
$ source ./venv/bin/activate
$ pip install mezzanine
$ pip install git+https://github.com/cedadev/ceda-theme-mezzanine.git
```
The dependencies should resolve so that the base `ceda_theme` and `django-cookie-law` packages are also installed.

Once installed, use mezzanine to create a new site "project" called e.g. `cedasite`:
```
mezzanine-project cedasite
cd cedasite
```
Then edit `cedasite/settings.py` to include the dependency apps into `INSTALLED_APPS`. The order is significant:
```
INSTALLED_APPS = (
    "ceda_theme",
    "ceda_theme_mezzanine",
    "columns",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    "mezzanine.pages",
    "mezzanine.blog",
    "mezzanine.forms",
    "mezzanine.galleries",
    "mezzanine.twitter",
    "cookielaw",
    # "mezzanine.accounts",
    # "mezzanine.mobile",
)
```
Create and run migrations for `ceda_theme_mezzanine` before creating the db:
```
python manage.py makemigrations ceda_theme_mezzanine
python manage.py createdb
```
Or if you have an existing db already, you would do the following to apply the database changes required for `ceda_theme_mezzanine`:
```
python manage.py migrate
```
After configuring any further settings (e.g. ALLOWED_HOSTS) in `cedasite/settings.py` and/or `cedasite/local_settings.py`, it should be possible to start the server.
```
python manage.py runserver
```