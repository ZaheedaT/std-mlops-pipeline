#!/bin/bash

# Setup script for the MLOps app

set -e

echo "========================================="
echo "       MLOps Project Setup"
echo "========================================="

if [ -z "$1" ]; then
    echo "Error: Project name is required."
    echo
    echo "Usage:"
    echo "  ./setup/setup.sh <project-name>"
    echo
    echo "Example:"
    echo "  ./setup/setup.sh house-price-model"
    exit 1
fi

PROJECT_NAME="$1"

echo "Project name: $PROJECT_NAME"

echo
echo "Installing Python dependencies..."

sudo apt-get update
sudo apt-get install -y python3-pip python3-venv

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

source venv/bin/activate

echo "Virtual environment activated."

echo
echo "Installing Python packages..."

python -m pip install --upgrade pip
python -m pip install -r setup/requirements.txt

echo
echo "Saving project configuration..."

cat > .env <<EOF
PROJECT_NAME=$PROJECT_NAME
EOF

echo
echo "========================================="
echo "       Setup completed successfully"
echo "========================================="
echo
echo "Project: $PROJECT_NAME"
echo "Virtual environment: ./venv"
echo "Environment file: ./.env"
echo
echo "To activate the environment later:"
echo "  source venv/bin/activate"
echo