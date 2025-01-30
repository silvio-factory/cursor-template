# Instructions Directory

This directory contains configuration files and setup instructions for various components of the project.

## Configuration Files

### `cursor_prompt.json`

- Configuration for Cursor IDE settings
- Custom prompts and templates
- Editor behavior settings
- Project-specific IDE configurations

### `supabase.json`

- Supabase database configuration
- Authentication settings
- Database schema definitions
- API configurations
- Security rules and policies

### `proxy_settings.json`

- Proxy configuration settings
- Network routing rules
- API gateway configurations
- Service mesh settings

## Usage

### Cursor IDE Setup

1. Ensure `cursor_prompt.json` is properly configured
2. Restart Cursor IDE to apply changes
3. Verify settings are applied correctly

### Supabase Configuration

1. Copy `supabase.json` to your Supabase project
2. Update necessary credentials and settings
3. Apply database migrations
4. Verify database connections

### Proxy Settings

1. Review `proxy_settings.json` for your environment
2. Apply proxy configurations to your services
3. Test network connectivity
4. Verify routing rules

## Best Practices

- Keep sensitive information in environment variables
- Document all configuration changes
- Version control configuration templates
- Use separate configurations for different environments
- Validate JSON files before deployment
- Keep configurations DRY
- Document required environment variables
- Include setup instructions for new developers
- Maintain change history
- Regular configuration reviews

## File Structure

```
instructions/
├── cursor_prompt.json    # Cursor IDE configuration
├── supabase.json        # Database and auth settings
├── proxy_settings.json  # Network and proxy configs
└── README.md           # This documentation file
```

## Adding New Configurations

When adding new configuration files:

1. Follow the existing naming convention
2. Document all settings thoroughly
3. Include usage examples
4. Update this README
5. Provide default/template values
6. Include validation steps
