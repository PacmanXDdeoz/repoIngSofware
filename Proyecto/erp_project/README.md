# Analisis de proyecto

## Requerimientos

Proyecto que pretende simular la gestión de recursos de una app de audiolibros

## Vistas

```
Login
    |-- Correo y Password
        |-- Dashboard
            |-- Biblioteca
            |-- 

```

## Base de datos

> Database: audiolearn
> Tables:
    |-- Books
        |-- id
        |-- title
        |-- autor
        |-- public_date
        |-- genere
        |-- status
    |-- Users
        |-- id
        |-- name
        |-- lastname
        |-- username
        |-- password ( insert into users (name, lastname, email, password) values ('admin', 'example', 'admin@example.com', crypt('123456', gen_salt('bf'))); )
        |-- correo
        |-- status
    |-- Lists
        |-- id
        |-- name
        |-- user_id
    |-- books_inlist
        |-- id
        |-- book_id
        |-- list_id
    |-- Reader
        |-- id
        |-- book_id
        |-- user_id
