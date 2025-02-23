fastapi-project
├── alembic/
├── config  # db connection
│   │   ├── database.py
│   │   ├── config.py
│   │   └── utils.py
├── src
│   ├── auth
│   │   ├── route.py          # auth main router with all the endpoints
│   │   ├── schemas.py        # pydantic models
│   │   ├── models.py         # database models
│   │   ├── dependencies.py   # router dependencies
│   │   ├── config.py         # local configs
│   │   ├── constants.py      # module-specific constants
│   │   ├── exceptions.py     # module-specific errors
│   │   ├── service.py        # module-specific business logic
│   │   └── utils.py          # any other non-business logic functions
│   └── feature-1
│   │   ├── route.py
│   │   ├── schemas.py
│   │   ├── models.py
│   │   ├── dependencies.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── service.py
│   │   └── utils.py
│   └── feature-2
│   │   ├── route.py
│   │   ├── schemas.py
│   │   ├── models.py
│   │   ├── dependencies.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── service.py
│   │   └── utils.py
|   |    __init__.py
│   ├── config.py  # global configs
│   ├── models.py  # global models
│   ├── exceptions.py  # global exceptions
│   └── main.py
├── tests/
│   ├── auth
│   ├── azure
│   └── feature-1
│   └── feature-2
├── templates/
│   └── index.html or jinja
├── .env
├── .gitignore
├── logging.ini
└── alembic.ini
└── pyproject.toml
└── uv.lock







fastapi-project
├── alembic/
├── config  # db connection
│   │   ├── database.py    # db connection related stuff
│   │   ├── config.py      # global configs
│   │   └── utils.py
├── src
│   ├── auth
│   │   ├── main.py           # auth main router with all the endpoints
│   │   ├── schemas.py        # pydantic models
│   │   ├── models.py         # database models
│   │   ├── dependencies.py   # router dependencies
│   │   ├── config.py         # local configs
│   │   ├── constants.py      # module-specific constants
│   │   ├── exceptions.py     # module-specific errors
│   │   ├── service.py        # module-specific business logic
│   │   └── utils.py          # any other non-business logic functions
│   ├── aws
│   │   ├── client.py  # client model for external service communication
│   │   ├── schemas.py
│   │   ├── config.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   └── utils.py
│   └── feature_1
│   │   ├── main.py
│   │   ├── schemas.py
│   │   ├── models.py
│   │   ├── dependencies.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── service.py
│   │   └── utils.py
│   ├── models.py      # global database models
│   ├── exceptions.py  # global exceptions
│   ├── pagination.py  # global module e.g. pagination
│   └── main.py
├── tests/
│   ├── auth
│   ├── aws
│   └── posts
├── templates/
│   └── index.html
├── .env
├── .gitignore
├── logging.ini
└── alembic.ini
└── pyproject.toml
└── poetry.lock