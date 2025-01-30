# Shared Types Directory

This directory contains TypeScript type definitions and interfaces shared between frontend and backend.

## Purpose

- Define common data structures
- Share API interfaces
- Define shared enums
- Maintain type consistency
- Document data models
- Share validation types

## Structure

```
types/
├── api/              # API request/response types
├── models/           # Shared data models
├── enums/            # Shared enumerations
├── validation/       # Validation schemas
└── utils/           # Utility types
```

## Common Types

### API Types

- Request/Response interfaces
- API error types
- Pagination types
- Filter types

### Data Models

- User interfaces
- Authentication types
- Shared entity types
- Common data structures

### Validation

- Input validation schemas
- Form validation types
- Shared validators

## Best Practices

- Keep types simple and focused
- Use proper TypeScript features
- Document complex types
- Maintain backward compatibility
- Use proper type exports
- Follow naming conventions
- Keep types DRY
- Version types appropriately
- Include JSDoc comments
- Test type compatibility

## Usage

```typescript
// Import shared types in frontend
import { UserType } from "@shared/types/models/user";

// Import shared types in backend
import { UserType } from "../../../shared/types/models/user";
```

## Adding New Types

When adding new types:

1. Ensure they are truly shared
2. Document the type purpose
3. Add proper JSDoc comments
4. Update relevant documentation
5. Test in both frontend and backend
6. Follow existing conventions
