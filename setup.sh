#!/bin/bash
envname="dut-psas"

# Create a virtual environment
echo "Creating $envname virtual environment..."
python3 -m venv $envname
# Activate the virtual environment
echo "Activating virtual environment..."
source $envname/bin/activate

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Setup completed successfully."
