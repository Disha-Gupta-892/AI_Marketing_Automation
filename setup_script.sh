#!/bin/bash

# AI-First Marketing Automation - Setup Script
# This script automates the setup process for both backend and frontend

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Print functions
print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_info() {
    echo -e "${YELLOW}ℹ $1${NC}"
}

print_header() {
    echo ""
    echo "======================================"
    echo "$1"
    echo "======================================"
    echo ""
}

# Check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Main setup function
main() {
    print_header "AI-First Marketing Automation - Setup"
    
    # Check prerequisites
    print_info "Checking prerequisites..."
    
    if ! command_exists python3; then
        print_error "Python 3 is not installed. Please install Python 3.9 or higher."
        exit 1
    fi
    print_success "Python 3 found: $(python3 --version)"
    
    if ! command_exists node; then
        print_error "Node.js is not installed. Please install Node.js 16 or higher."
        exit 1
    fi
    print_success "Node.js found: $(node --version)"
    
    if ! command_exists npm; then
        print_error "npm is not installed. Please install npm."
        exit 1
    fi
    print_success "npm found: $(npm --version)"
    
    # Ask for installation type
    echo ""
    echo "Select installation type:"
    echo "1) Full installation (Backend + Frontend)"
    echo "2) Backend only"
    echo "3) Frontend only"
    read -p "Enter choice [1-3]: " choice
    
    case $choice in
        1)
            setup_backend
            setup_frontend
            print_completion_message
            ;;
        2)
            setup_backend
            print_backend_only_message
            ;;
        3)
            setup_frontend
            print_frontend_only_message
            ;;
        *)
            print_error "Invalid choice. Exiting."
            exit 1
            ;;
    esac
}

# Backend setup
setup_backend() {
    print_header "Setting up Backend"
    
    # Create directories
    print_info "Creating required directories..."
    mkdir -p backend/agents
    mkdir -p backend/utils
    mkdir -p uploads
    mkdir -p outputs
    mkdir -p logs
    mkdir -p campaign_data
    
    # Create __init__.py files
    touch backend/agents/__init__.py
    touch backend/utils/__init__.py
    
    print_success "Directories created"
    
    # Create virtual environment
    print_info "Creating Python virtual environment..."
    cd backend
    python3 -m venv venv
    print_success "Virtual environment created"
    
    # Activate virtual environment
    print_info "Activating virtual environment..."
    source venv/bin/activate
    
    # Install dependencies
    print_info "Installing Python dependencies (this may take a few minutes)..."
    pip install --upgrade pip
    pip install -r requirements.txt
    print_success "Dependencies installed"
    
    # Setup environment file
    if [ ! -f .env ]; then
        print_info "Creating .env file from template..."
        cp .env.example .env
        print_success ".env file created"
        print_info "Please edit backend/.env and add your OpenAI API key"
    else
        print_info ".env file already exists, skipping..."
    fi
    
    cd ..
}

# Frontend setup
setup_frontend() {
    print_header "Setting up Frontend"
    
    cd frontend
    
    # Install dependencies
    print_info "Installing Node.js dependencies (this may take a few minutes)..."
    npm install
    print_success "Dependencies installed"
    
    # Create .env file if needed
    if [ ! -f .env ]; then
        print_info "Creating frontend .env file..."
        echo "REACT_APP_API_URL=http://localhost:8000" > .env
        print_success "Frontend .env created"
    fi
    
    cd ..
}

# Completion messages
print_completion_message() {
    print_header "Setup Complete!"
    
    echo "To start the application:"
    echo ""
    echo "1. Backend:"
    echo "   cd backend"
    echo "   source venv/bin/activate"
    echo "   python main.py"
    echo "   → Server will run on http://localhost:8000"
    echo ""
    echo "2. Frontend (in a new terminal):"
    echo "   cd frontend"
    echo "   npm start"
    echo "   → App will run on http://localhost:3000"
    echo ""
    print_info "Don't forget to add your OpenAI API key in backend/.env"
    echo ""
}

print_backend_only_message() {
    print_header "Backend Setup Complete!"
    
    echo "To start the backend:"
    echo "   cd backend"
    echo "   source venv/bin/activate"
    echo "   python main.py"
    echo "   → Server will run on http://localhost:8000"
    echo "   → API docs: http://localhost:8000/docs"
    echo ""
    print_info "Don't forget to add your OpenAI API key in backend/.env"
    echo ""
}

print_frontend_only_message() {
    print_header "Frontend Setup Complete!"
    
    echo "To start the frontend:"
    echo "   cd frontend"
    echo "   npm start"
    echo "   → App will run on http://localhost:3000"
    echo ""
    print_info "Make sure the backend is running on http://localhost:8000"
    echo ""
}

# Run main function
main