# Notice
1. never use table name as "user", which conflits to system 
<img width="280" height="120" alt="image" src="https://github.com/user-attachments/assets/8dfd6b1b-626d-44d8-a815-03ea54920cd2" />


2. when to change sqlite to postgresql, you remove "metadata.creat_all(engine ) =→ “Just make whatever tables I defined, no strict rules"   
- You should stop creating tables automatically from your code   
- and instead let a migration tool (like Alembic) manage your schema  
