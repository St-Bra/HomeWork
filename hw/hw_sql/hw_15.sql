CREATE TABLE authors(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR
);

CREATE TABLE books(
    id SERIAL PRIMARY KEY,
    title VARCHAR,
    autor_id INT REFERENCES authors(id),
    publication_year INT
);

CREATE TABLE Sales
(
    id SERIAL PRIMARY KEY,
    quantity INT,
    book_id INT REFERENCES books(id)
);

DROP TABLE authors, sales, books;

INSERT INTO authors(first_name, last_name) VALUES
('Лев', 'Толстой'),
('Федор', 'Достоевский'),
('Михаил', 'Булгаков'),
('Николай', 'Гоголь'),
('Александр', 'Пушкин');

INSERT INTO books(title, autor_id, publication_year) VALUES
('Война и мир', 1, 1873),
('Престуаление и наказание', 2, 1866),
('Мастер и Маргарита', 3, 1940),
('Мёртвые души', 4, 1835);

INSERT INTO sales(quantity, book_id) VALUES
(15, 3),
(12, 1);


SELECT books.title, authors.first_name, authors.last_name FROM authors
JOIN books ON authors.id = books.autor_id;


SELECT books.title, authors.first_name, authors.last_name FROM authors
LEFT JOIN books ON authors.id = books.autor_id;

SELECT books.title, authors.first_name, authors.last_name FROM authors
RIGHT JOIN books ON authors.id = books.autor_id;

SELECT B.title, A.first_name, A.last_name, S.quantity FROM authors A
INNER JOIN books B ON A.id = B.autor_id
INNER JOIN sales S ON B.id = S.book_id;

SELECT B.title, A.first_name, A.last_name, S.quantity FROM authors A
LEFT JOIN books B ON A.id = B.autor_id
LEFT JOIN sales S ON B.id = S.book_id;