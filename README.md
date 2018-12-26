
## Migrate existing tables to code

```bash
sqlacodegen mysql+pymysql://root:password@db/booking > models.py
```

## Creating a new database using migration

Create a new database `booking`.

```bash
flask db upgrade
```

## Testing the endpoints

```bash
http POST http://localhost:5000/api/1.0/create/user first_name=Harry
last_name=Lee
```
