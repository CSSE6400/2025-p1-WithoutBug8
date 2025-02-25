[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18328249)
# CSSE6400 Week 1 Practical

[English](README.md) | [简体中文Chinese](README_ZH.md)

**Get the detail practice course notes please refer Chinese version.**

### Project brief introduction 

Construction of a simple HTTP server in Python. **Practical-1** is a simple practice project designed to help understand the **HTTP protocol** while using the **Flask framework** and **REST API** to build a basic **Todo application**.

### Specific content

- This project covers the four common HTTP request methods: **GET, POST, PUT, DELETE**.

    | HTTP Method | Purpose                   | Requires Request Body?                  | Requires Specific ID             | Use Case          | Security🔒                  |
  | ----------- | ------------------------- | --------------------------------------- | -------------------------------- | ----------------- | -------------------------- |
  | GET         | Retrieve resources        | Generally no, parameters are in the URL | Not necessarily                  | Querying data     | ❌Not secure                |
  | POST        | Create new resources      | Required                                | User-defined or Server-generated | Creating new data | ⚠️Reletively secure         |
  | PUT         | Update existing resources | Required                                | Must specify ID                  | Modifying data    | ❓Depends on implementation |
  | DELETE      | Remove resource           | Only URL                                | Must specify ID                  | Deleting data     | ❓Depends on implementation |

### More information

- The next update will refine this file. There are still many shortcomings due to my limited programming skills, but I will continue improving my progarm ability.
