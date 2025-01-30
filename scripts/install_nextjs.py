#!/usr/bin/env python3

import os
import shutil
import subprocess
import sys
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def get_frontend_dir():
    """Get the absolute path to the frontend directory."""
    # Get the script's directory
    script_dir = Path(__file__).resolve().parent
    # Navigate to frontend directory (one level up and then into frontend)
    frontend_dir = script_dir.parent / 'frontend'
    return frontend_dir

def clear_directory(directory):
    """
    Clear all contents of a directory while preserving the directory itself.
    
    Args:
        directory (Path): Directory path to clear
    """
    try:
        if directory.exists():
            logger.info(f"Clearing contents of {directory}")
            for item in directory.iterdir():
                if item.is_file():
                    item.unlink()
                elif item.is_dir():
                    shutil.rmtree(item)
        else:
            directory.mkdir(parents=True)
            logger.info(f"Created directory {directory}")
    except Exception as e:
        logger.error(f"Error clearing directory {directory}: {str(e)}")
        raise

def run_command(command, cwd=None):
    """
    Run a shell command and handle its output.
    
    Args:
        command (list): Command to run as a list of strings
        cwd (Path): Working directory for the command
    """
    try:
        logger.info(f"Running command: {' '.join(command)}")
        result = subprocess.run(
            command,
            cwd=cwd,
            check=True,
            text=True,
            capture_output=True
        )
        logger.info(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed with error: {e.stderr}")
        return False

def install_nextjs():
    """Install Next.js in the frontend directory."""
    try:
        frontend_dir = get_frontend_dir()
        
        # Clear the frontend directory
        clear_directory(frontend_dir)
        
        # Check if npm is installed
        if not run_command(['npm', '--version']):
            logger.error("npm is not installed. Please install Node.js and npm first.")
            return False
        
        # Create new Next.js project with TypeScript and Tailwind CSS
        logger.info("Creating new Next.js project...")
        create_command = [
            'npx',
            'create-next-app@latest',
            '.',
            '--typescript',
            '--tailwind',
            '--eslint',
            '--app',
            '--src-dir',
            '--use-npm',
            '--no-git',
            '--import-alias', '@/*'
        ]
        
        if not run_command(create_command, frontend_dir):
            logger.error("Failed to create Next.js project")
            return False
            
        logger.info("Next.js project created successfully!")
        logger.info("\nYou can now:")
        logger.info("1. cd into the frontend directory: cd frontend")
        logger.info("2. Start the development server: npm run dev")
        return True
        
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    try:
        success = install_nextjs()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        logger.info("\nInstallation cancelled by user")
        sys.exit(1) 