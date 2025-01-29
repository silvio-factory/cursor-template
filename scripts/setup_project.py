import os
import subprocess
import sys
import platform
import shutil
from pathlib import Path

def create_venv():
    """Create and activate virtual environment"""
    print("Setting up Python virtual environment...")
    
    # Check if venv already exists
    if os.path.exists('backend/venv'):
        print("Virtual environment already exists.")
        return
    
    try:
        # Create venv
        subprocess.run([sys.executable, '-m', 'venv', 'backend/venv'], check=True)
        print("Virtual environment created successfully.")
        
        # Determine the pip path based on the operating system
        if platform.system() == "Windows":
            pip_path = 'backend/venv/Scripts/pip'
        else:
            pip_path = 'backend/venv/bin/pip'
        
        # Upgrade pip
        subprocess.run([pip_path, 'install', '--upgrade', 'pip'], check=True)
        
        # Install requirements if requirements.txt exists
        if os.path.exists('backend/requirements.txt'):
            print("Installing requirements...")
            subprocess.run([pip_path, 'install', '-r', 'backend/requirements.txt'], check=True)
            print("Requirements installed successfully.")
    
    except subprocess.CalledProcessError as e:
        print(f"Error setting up virtual environment: {e}")
        sys.exit(1)

def create_directory_structure():
    """Create the project directory structure"""
    print("Creating project directory structure...")
    
    # Root level directories with their purposes
    directories = {
        'frontend/src/app': 'Next.js app directory',
        'frontend/src/components': 'Reusable React components',
        'frontend/src/lib': 'Utility functions',
        'frontend/src/styles': 'Global styles and CSS modules',
        'frontend/src/types': 'TypeScript type definitions',
        'frontend/public': 'Static assets',
        'backend/src/api': 'API routes and endpoints',
        'backend/src/models': 'Database models',
        'backend/src/services': 'Business logic services',
        'backend/src/utils': 'Helper functions',
        'backend/src/ai': 'AI/ML integration code',
        'backend/tests': 'Backend tests',
        'shared/types': 'Shared TypeScript types',
        'shared/constants': 'Shared constants',
        'infrastructure/terraform': 'Infrastructure as code',
        'infrastructure/docker': 'Docker configurations',
        'scripts': 'Development and deployment scripts',
        'docs': 'Project documentation',
        '.github/workflows': 'GitHub Actions CI/CD',
        '.vscode': 'VS Code settings',
        'instructions': 'Project instructions and documentation'
    }

    # Create directories and .gitkeep files
    for directory, purpose in directories.items():
        dir_path = Path(directory)
        if not dir_path.exists():
            print(f"Creating {directory} - {purpose}")
            dir_path.mkdir(parents=True, exist_ok=True)
            # Add .gitkeep to empty directories
            (dir_path / '.gitkeep').touch()

def create_config_files():
    """Create basic configuration files if they don't exist"""
    print("Setting up configuration files...")
    
    config_files = {
        'frontend/package.json': '''{
  "name": "frontend",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  }
}''',
        'backend/requirements.txt': '''fastapi==0.104.1
uvicorn==0.24.0
python-dotenv==1.0.0
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
celery==5.3.4
openai==1.3.5
transformers==4.35.2
python-jose==3.3.0
passlib==1.7.4
pytest==7.4.3
''',
        '.vscode/settings.json': '''{
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.fixAll": true
    },
    "python.defaultInterpreterPath": "${workspaceFolder}/backend/venv/bin/python",
    "python.analysis.extraPaths": ["${workspaceFolder}/backend/src"]
}'''
    }

    for file_path, content in config_files.items():
        path = Path(file_path)
        if not path.exists():
            print(f"Creating {file_path}")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)

def main():
    """Main setup function"""
    try:
        print("Starting project setup...")
        
        # Create directory structure
        create_directory_structure()
        
        # Create configuration files
        create_config_files()
        
        # Setup virtual environment
        create_venv()
        
        print("\nProject setup completed successfully! 🚀")
        print("\nNext steps:")
        print("1. Activate the virtual environment:")
        if platform.system() == "Windows":
            print("   backend\\venv\\Scripts\\activate")
        else:
            print("   source backend/venv/bin/activate")
        print("2. Install frontend dependencies:")
        print("   cd frontend && npm install")
        print("3. Start developing!")
        
    except Exception as e:
        print(f"Error during setup: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main() 