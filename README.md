# FastAPI Code Snippet & Execution Platform

A secure GitHub-like platform to store, version, and execute Python code inside an isolated Docker sandbox.

## Features

* Versioned code snippets
* Async execution queue (Redis)
* Isolated Docker sandbox
* Execution logs
* Swagger / OpenAPI
* MariaDB persistence
* Type-safe FastAPI + Pydantic

## Stack

FastAPI • MariaDB • Redis • Docker • Async Python • SQLAlchemy 2.0

---

## Run

### 1. Install (modern)

```bash
uv sync
```

### 2. Start system

```bash
docker compose up --build
```

API → [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Flow

1. Create snippet → `/snippets`
2. Execute snippet → `/execute`
3. Worker runs code in Docker sandbox
4. Output saved in DB

---

## Security

* Code runs in isolated container
* No host access
* Output limited
* Timeout enforced
* Builtins restricted

---

## License

MIT License

Copyright 2026

Seyyed Ali Mohammadiyeh (Max Base)
