================================================
File: README.md
================================================
# tameronline-searchyolo

## Overview
`tameronline-searchyolo` is a lightweight and automated environment setup script designed to streamline the process of creating and activating a virtual environment across different operating systems (Windows, Linux, and macOS). This project ensures that Python dependencies are properly managed and integrated with your development workflow.

## Features
- **Cross-Platform Support**: Works seamlessly on Windows (`.bat`, `.ps1`), Linux (`.sh`), and macOS (`.sh`).
- **Automated Virtual Environment Setup**: Detects Python installation, creates a virtual environment, and activates it.
- **Pip Package Management**: Ensures the latest version of pip and installs dependencies from `requirements.txt`.
- **Integrated with VS Code**: Provides a `.code-workspace` file for one-click environment activation in Visual Studio Code.

## Installation
### Prerequisites
- **Python 3.6+** must be installed.
- **VS Code (optional)** for an integrated development experience.

### Setup Instructions
#### Windows
**Using Command Prompt:**
```cmd
cd path/to/tameronline-searchyolo
activate_project.bat
```
**Using PowerShell:**
```powershell
cd path/to/tameronline-searchyolo
.\activate_project.ps1
```

#### Linux/macOS
```bash
cd path/to/tameronline-searchyolo
chmod +x activate_project.sh
./activate_project.sh
```

### **5. Install Dependencies**
After activating the virtual environment, install the required dependencies:
```bash
pip install -r requirements.txt
```

## File Structure
```
tameronline-searchyolo/
├── README.md                # Documentation
├── activate_project.bat     # Windows CMD script
├── activate_project.ps1     # Windows PowerShell script
├── activate_project.sh      # Linux/macOS Bash script
├── requirements.txt         # List of dependencies
├── .gitignore               # Git ignore file
├── tests/
│   ├── __init__.py          # Marks the tests directory as a package
│   ├── test_example.py      # Example test case
│   ├── test_search.py       # Tests for search.py
└── workspace.code-workspace # VS Code workspace file
```

================================================
File: tests/__init__.py
================================================
# This file marks the tests directory as a package.

================================================
File: tests/test_search.py
================================================
import pytest
import os
import csv
from src.search import scrape_and_save_to_csv

def test_scrape_and_save_to_csv():
    test_url = 'https://www.cdc.gov/heart-disease/about/aortic-aneurysm.html#cdc_disease_basics_types-types'
    output_file = os.path.join(os.path.dirname(__file__), '../src/aortic_aneurysm_links.csv')
    
    # Run the function
    scrape_and_save_to_csv(test_url)
    
    # Check if the file was created
    assert os.path.exists(output_file), "CSV file was not created"
    
    # Read the CSV file and check its contents
    with open(output_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        
        # Ensure the CSV has some data
        assert len(rows) > 0, "CSV file is empty"
        
        # Check the structure of the CSV file
        assert 'Link Text' in reader.fieldnames, "Missing 'Link Text' column"
        assert 'Href' in reader.fieldnames, "Missing 'Href' column"

if __name__ == "__main__":
    pytest.main()
