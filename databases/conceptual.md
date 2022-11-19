### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  Postgres is one of the most popular, powerful and open source relational database that follows SQL standards

- What is the difference between SQL and PostgreSQL?
  SQL is a sttuctured query language. PostgreSQL is RDBMS that uses SQL standards. 

- In `psql`, how do you connect to a database?
  \c db_name

- What is the difference between `HAVING` and `WHERE`?
  "HAVING is used for groups(with "GROUP BY" clause), "WHERE" os used for individual rows.

- What is the difference between an `INNER` and `OUTER` join?
  INNER join can only contain data if it's in both of joining tables. OUTER joinfs can have data that are onluy in one of joining tables.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
  "Left join will combine all raw of the "main" table and corresponding data from "joining" table and vice versa.

- What is an ORM? What do they do?
  ORM is object-relational mapper. Used for data interaction between relational databases and OO languages.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  Requests made with ajax are going from client side straight to API server and response is sent back to the browser.
  Requests made with 'requests' library are made from server side and response is also sent to the server and then to the browser.

- What is CSRF? What is the purpose of the CSRF token?
  CSRF is a token that is automatically created when showin a form and sent with form data for security purposes to make sure the data is coming from the right site.

- What is the purpose of `form.hidden_tag()`?
  form.hidden_tag() - generates a hidden field that contains the csrf token to protect the form.
