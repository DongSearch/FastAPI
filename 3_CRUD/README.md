# CRUD
fundamental function for managing posts

| Method | Endpoint          | Description             | Request Body                  | Query Params                                          | Response         |
| ------ | ----------------- | ----------------------- | ----------------------------- | ----------------------------------------------------- | ---------------- |
| POST   | `/post`           | Create a new post       | `title, content, author, age` | ❌ None                                                | Created post     |
| GET    | `/post`           | Get all posts           | ❌ None                        | `author` (optional), `limit`, `skip`, `sort`, `order` | List of posts    |
| GET    | `/post/{id}`      | Get a single post       | ❌ None                        | ❌ None                                                | Single post      |
| POST   | `/post/{id}/like` | Like a post             | ❌ None                        | ❌ None                                                | Like count       |
| PUT    | `/post/{id}`      | Update entire post      | `title, content, author, age` | ❌ None                                                | Updated post     |
| PATCH  | `/post/{id}`      | Partially update a post | Partial fields (optional)     | ❌ None                                                | Updated post     |
| DELETE | `/post/{id}`      | Delete a post           | ❌ None                        | ❌ None                                                | Deletion message |


# Result
- we can see that the poses are sorted in order "desc" with "like", and using patch data of id 2 was partially updated
<img width="1165" height="943" alt="result" src="https://github.com/user-attachments/assets/2680fccc-781d-435e-83f3-6c2ee4c54b48" />


# Trouble shooting and Main point to know
1. currently list is used for simplicity, but after restart, all of datas will disappear  
-> need to chagned it to SQL DB  
2. Patch update post partially, which means it needs new database model including optional variable by using "Optional"
```
update_data = post.model_dump(exclude_unset= True)
```
-> exclude_unset is essential that ignore the data that users doesn't give

3. for handling exception, I need to know standard error codes
| Code | Name                  | When to Use                                           |
| ---- | --------------------- | ----------------------------------------------------- |
| 200  | OK                    | Request succeeded (GET, PUT, DELETE)                  |
| 201  | Created               | Resource successfully created (POST)                  |
| 400  | Bad Request           | Invalid request (wrong data format, validation error) |
| 401  | Unauthorized          | Authentication required or failed                     |
| 403  | Forbidden             | No permission to access resource                      |
| 404  | Not Found             | Resource does not exist                               |
| 422  | Unprocessable Entity  | Validation error (FastAPI + Pydantic)                 |
| 500  | Internal Server Error | Server error                                          |


4. currently user can put value to "like" and " view_count" as they want, it should be changed to avoid form manupulating form users
->  Request and Response model should be seperated!!!!!
