
## Migrate existing tables to code

```bash
sqlacodegen mysql+pymysql://root:password@db/booking > models.py
```

## Testing the endpoints

```bash
http POST http://localhost:5000/api/1.0/create/user first_name=Harry
last_name=Lee
```
