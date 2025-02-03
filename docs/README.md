# Project Documentation Directory

This directory contains configuration files and setup instructions for various components of the SaaS project.

## Project Overview

This project is a simple collection of requirements, folders and file structure for a SaaS project with the following tech stack:

- Frontend: Next.js (React)
- Backend: FastAPI (Python) OR Node.js (Express/NestJS)
- Database: PostgreSQL (Supabase)
- AI API Handling: OpenAI API + Hugging Face + Custom ML models
- Queue/Async: Celery (Python) OR BullMQ (Node.js)
- Hosting: Vercel (frontend) + Railway/Fly.io (backend)
- Observability: Sentry + Prometheus

## Directory Contents

- `cursor_prompt.json`: Best practices and prompts for working with Cursor AI
- `roadmap.json`: Project roadmap and technical configurations
- `supabase.json`: Database schema and configuration details
- `README.md`: This file - contains development guidelines

## Development Guidelines

### Fundamental Principles

- Write clean, simple, readable code.
- Implement features in the simplest possible way.
- Keep files small and focused (<200 lines).
- Test after every meaningful change.
- Focus on core functionality before optimization.
- Use clear, consistent naming.
- Think thoroughly before coding. Write 2-3 reasoning paragraphs.
- ALWAYS write simple, clean, and modular code.
- Use clear and easy-to-understand language. Write in short sentences.
- AVOID huge refactoring and PREFERABLY break down the change in multiple steps.
- ALWAYS include the location and a little explanation of ALL new files you create as a comment.

### Error Fixing

- DO NOT JUMP TO CONCLUSIONS! Consider multiple possible causes before deciding.
- Explain the problem in plain English.
- Make minimal necessary changes, changing as few lines of code as possible.
- In case of strange errors, ask the user to perform a Perplexity web search to find the latest up-to-date information.

### Building Process

- Verify each new feature works by telling the user how to test it.
- DO NOT write complicated and confusing code. Opt for the simple & modular approach.
- When you are not sure what to do, tell the user to perform a web search or to check the documentation.

### Comments

- ALWAYS try to add more helpful and explanatory comments into our code.
- NEVER delete old comments - unless they are obviously wrong/obsolete.
- Include LOTS of explanatory comments in the code. ALWAYS write well documented code.
- Document all changes and their reasoning IN THE COMMENTS YOU WRITE.
- When writing comments, use clear and easy-to-understand language. Write sentences.

## Additional Resources

### Useful Commands for Proxy Configuration

```bash
# Check Proxy Settings
git config --global --get http.proxy
git config --global --get https.proxy

# Windows: netsh winhttp show proxy
# Linux/Mac: env | grep -i proxy

# Set Proxy
git config --global http.proxy http://127.0.0.1:PORT
git config --global https.proxy http://127.0.0.1:PORT

# Remove Proxy
git config --global --unset http.proxy
git config --global --unset https.proxy
```

### Troubleshooting Tips

1. Run test_connection.py to verify proxy settings
2. Watch for timeout errors (usually indicate slow proxy connection)
3. Check for authentication errors (may require proxy credentials)
4. Monitor SSL errors (might need certificate configuration)
5. Consider bypassing proxy for GitHub if not required
