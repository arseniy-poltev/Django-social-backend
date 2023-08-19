## Introduction

## 1. Requirements

Python 3.7 or higher.

## 2. How to run the project

1. `cd` into the project and then run `virtualenv venv`

#### If you are using MacOS, Linux or Ubuntu

2. Run `source venv/bin/activate`
3. Run `pip install -r requirements.txt`
4. Install Ganache and download BSC testnet network into your local computer by running `python setup_ganache.py`

#### If you are using Windows

2. If Windows, run `venv\Scripts\activate`
3. Run `pip install -r requirements_windows.txt`
4. Install Ganache and download BSC testnet network into your local computer by running `python setup_ganache_windows.py`

5. Run `python manage.py migrate`
6. (optional) Run `python manage.py createsuperuser`
7. Run `python manage.py runserver`
