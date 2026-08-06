# Day 2 Notes

## 1. Why shouldn't business logic be inside route handlers?

Route handlers should stay focused on receiving a request, validating it, and sending a response. If business logic is placed directly inside them, the code becomes harder to read, harder to test, and harder to reuse. Keeping logic in separate services makes the app cleaner and easier to maintain.

## 2. What problem does APIRouter solve?

APIRouter helps organize routes into smaller groups instead of putting everything into one large file. It makes the code modular, easier to manage, and cleaner to scale as the application grows.

## 3. What is a Pydantic model?

A Pydantic model is a Python class used to define the structure of input or output data. It validates data automatically, so you can be confident that the values coming into your API match the expected format.

## 4. Why do we use .env files?

.env files store configuration values such as environment variables, secrets, and app settings outside the source code. This keeps sensitive information safe and makes it easier to change configuration between development, testing, and production.

## 5. What's the difference between a route, a service, and a schema?

- A route handles the HTTP request and response.
- A service contains the business logic.
- A schema defines the shape of the data, usually for validation and serialization.

In short: routes receive requests, services process them, and schemas describe the data.
