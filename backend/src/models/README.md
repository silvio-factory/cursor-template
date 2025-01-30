# Models Directory

This directory contains database models, schemas, and data transfer objects (DTOs) for the application.

## Purpose

- Define SQLAlchemy ORM models for database tables
- Implement Pydantic models for request/response validation
- Define data transfer objects for API interactions
- Manage database migrations and schema changes
- Handle model relationships and constraints

## Structure

- Each model typically has its own file
- Base models and shared functionality in `base.py`
- Separate files for complex types and enums
- Migration scripts are version controlled
- Model relationships are clearly defined

## Best Practices

- Keep models simple and focused on data structure
- Use type hints and validation rules
- Implement proper indexing for performance
- Follow database normalization principles
- Document model fields and relationships
- Use appropriate data types for columns
- Implement proper cascade behaviors for relationships
