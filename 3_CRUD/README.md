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

