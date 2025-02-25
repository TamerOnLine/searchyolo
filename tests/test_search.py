import pytest
import os
import csv
from src.search import scrape_and_save_to_csv

def test_scrape_and_save_to_csv():
    test_url = 'https://www.cdc.gov/heart-disease/about/aortic-aneurysm.html#cdc_disease_basics_types-types'
    output_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'aortic_aneurysm_links.csv'))
    
    # Run the function
    scrape_and_save_to_csv(test_url, output_file)
    
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