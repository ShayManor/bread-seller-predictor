
#!/bin/bash

# Ensure virtual environment is active or create it if not
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt

# Run the Flask application
python app.py
