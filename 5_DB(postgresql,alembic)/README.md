# Summary
PostgreSQL → stores data  
SQLAlchemy → defines data (Python → DB)  
Alembic → manages changes over time  
# PostgreSQL
A database management system (DBMS).

- Stores your data (tables, rows, relations)
- Handles queries, transactions, concurrency
- Production-ready (unlike SQLite for small apps)

why???  
- Because you need a reliable, scalable place to store data
# Alembic

A database migration tool for SQLAlchemy.

- Tracks schema changes (tables, columns, indexes)
- Generates migration scripts
- Applies changes safely over time

why????          
Because your database structure will change, and you need:
- version control for DB
- reproducible updates (team / deploy)

* migration
a controlled change to your database structure over time, or a file that records this change.

## Why SQLAlchemy alone is NOT enough?
- No version control
- No history of changes
- Can’t handle:     
  column rename     
  data migration   
  rollback    
- Dangerous in production
# Result
<img width="1348" height="530" alt="Screenshot from 2026-03-25 09-17-26" src="https://github.com/user-attachments/assets/447fde1f-9ab7-4506-b221-eeb3980cde84" />


# Process
1. alembic init 
```
# Bash
alembic init alembic(folder name)
```
2. edit url in alembic.ini( you can also manage it in envrionment parameter)
```
sqlalchemy.url = postgresql://username:passowrd@localhost:port_number/db_name
ex : sqlalchemy.url = postgresql://gidong:1234@localhost:5432/testdb
```
3. make sure to have user name and password
```
sudo -u postgres psql

CREATE USER name WITH PASSWORD 'password';
ALTER USER name WITH SUPERUSER
CREATE DATABASE db_name; #
CREATE DATABASE db_name OWNER user_name ( designe owner)
```
4. find model location
```
from my_model import Base

target_metadata = Base.metadata
``` 
4. create Migration
```
alembic revision --autogenerate -m "init"
```
5. upgrade head
```
alembic upgrade
```

6. connect to psql
```
psql -U gidong -h localhost -d testdb -W
```

# Notice
1. never use table name as "user", which conflits to system 
<img width="280" height="120" alt="image" src="https://github.com/user-attachments/assets/8dfd6b1b-626d-44d8-a815-03ea54920cd2" />


2. when to change sqlite to postgresql, you remove "metadata.creat_all(engine ) =→ “Just make whatever tables I defined, no strict rules"   
- You should stop creating tables automatically from your code   
- and instead let a migration tool (like Alembic) manage your schema   

| Feature         | create_all() | Alembic |
| --------------- | ------------ | ------- |
| Creates tables  | ✅            | ✅       |
| Updates schema  | ❌            | ✅       |
| Version control | ❌            | ✅       |
| Production safe | ❌            | ✅       |
