# Shared Constants Directory

This directory contains constants and configuration values shared between frontend and backend.

## Purpose

- Define shared configuration values
- Maintain consistent constants
- Share business rules
- Define common enums
- Share API endpoints
- Define shared validation rules

## Structure

```
constants/
├── api/              # API-related constants
├── config/           # Shared configurations
├── validation/       # Validation constants
├── business/         # Business rules
└── enums/           # Shared enumerations
```

## Common Constants

### API Constants

- Endpoint URLs
- HTTP methods
- Status codes
- Error messages
- Response formats

### Configuration

- Feature flags
- Timeout values
- Pagination limits
- Cache durations
- Common settings

### Business Rules

- Status enums
- Role definitions
- Permission levels
- Process states
- Common limitations

## Best Practices

- Use proper naming conventions
- Document constant purposes
- Group related constants
- Use TypeScript enums where appropriate
- Keep values immutable
- Version constants properly
- Document any changes
- Use descriptive names
- Include units in comments
- Keep values type-safe

## Usage

```typescript
// Import shared constants in frontend
import { API_ENDPOINTS } from "@shared/constants/api";

// Import shared constants in backend
import { API_ENDPOINTS } from "../../../shared/constants/api";
```

## Adding New Constants

When adding new constants:

1. Ensure they are truly shared
2. Use proper naming conventions
3. Add appropriate documentation
4. Group related constants
5. Consider type safety
6. Test in both environments
