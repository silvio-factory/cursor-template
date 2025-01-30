# webapp-template

## Tech Stack

- Frontend: Next.js (React)
- Backend: FastAPI (Python) OR Node.js (Express/NestJS)
- Database: PostgreSQL (Supabase)
- AI API Handling: OpenAI API + Hugging Face + Custom ML models
- Queue/Async: Celery (Python) OR BullMQ (Node.js)
- Hosting: Vercel (frontend) + Railway/Fly.io (backend)
- Observability: Sentry + Prometheus

## Folder Structure

📁 frontend/
├── 📁 src/
│ ├── 📁 app/ Next.js app directory
│ ├── 📁 components/ Reusable React components
│ ├── 📁 lib/ Utility functions
│ ├── 📁 styles/ CSS and styling
│ └── 📁 types/ TypeScript types/interfaces
├── 📁 public/ Static assets
📁 backend/
├── 📁 src/
│ ├── 📁 api/ API routes and handlers
│ ├── 📁 models/ Database models
│ ├── 📁 services/ Business logic
│ ├── 📁 utils/ Helper functions
│ └── 📁 ai/ AI/ML related code
└── 📁 tests/ Test files
📁 shared/ Shared between front/backend
├── 📁 types/ Common type definitions
└── 📁 constants/ Shared constants
📁 infrastructure/
├── 📁 terraform/ Infrastructure as code
└── 📁 docker/ Docker configuration
📁 scripts/ Utility scripts
📁 docs/ Documentation
📁 .github/workflows/ CI/CD pipelines
📁 .vscode/ Editor configuration
📁 instructions/ Project instructions
