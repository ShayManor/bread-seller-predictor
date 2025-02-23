
#!/bin/bash

# Check if pip is installed, if not install it
if ! command -v pip &> /dev/null
then
    echo "pip could not be found, installing pip..."
    apt-get update
    apt-get install python3-pip -y
fi

# Install required Python packages from requirements.txt
pip install -r requirements.txt

# Run the Flask application
python app.py
