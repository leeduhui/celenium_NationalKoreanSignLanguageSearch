National Korean Sign Language Search Automation

This repository contains a Python script that automates the process of searching for Korean sign language terminology using Selenium and saves the results to an Excel file.
The script reads a list of terms from an Excel file, performs searches on the National Institute of Korean Language sign language dictionary, and outputs the results back to the Excel file.

Repository Structure

bash
├── 128/  

    │   └── chromedriver-win64/  

    │       └── chromedriver-win64/  

    │           └── chromedriver.exe   # ChromeDriver for Selenium  

    ├── chrome.py                      # Main script for automating search and saving results  

    ├── 전문용어선정_후보_from_Erin.xlsx  # Input Excel file with terms to search  

    ├── 전문용어선정_후보_with_results.xlsx # Output Excel file with search results  


Requirements

    Python 3.x
    Selenium (pip install selenium)
    Pandas (pip install pandas)
    openpyxl (pip install openpyxl)
    Google Chrome installed

Setup

    Install necessary Python libraries:

    bash

    pip install selenium pandas openpyxl

    Download the ChromeDriver corresponding to your version of Chrome from here and place it in the 128/chromedriver-win64/chromedriver-win64/ directory.

    Make sure the input Excel file (전문용어선정_후보_from_Erin.xlsx) is in the repository.

How to Run

    Open the chrome.py script and ensure that the path to the ChromeDriver is correct for your local setup:

    python

service = Service('C:/Users/scott/chrome/128/chromedriver-win64/chromedriver-win64/chromedriver.exe')

Run the script:

bash

    python chrome.py

    The script will:
        Open the National Institute of Korean Language's Korean Sign Language Dictionary.
        Read the list of search terms from the Excel file (전문용어선정_후보_from_Erin.xlsx).
        Perform a search for each term.
        Write the results (if found) back into a new column of the Excel file (전문용어선정_후보_with_results.xlsx).

Output

The results of the search will be saved in a new Excel file (전문용어선정_후보_with_results.xlsx). The script will add a new column, "검색 결과" (Search Results), which contains the title of the search result and the number of matches.
Notes

    The script pauses for 2 seconds after each search to allow the webpage to load. Adjust the time.sleep() duration if necessary.
    If no results are found for a search term, the output will state "결과 없음" (No results).

License

This project is licensed under the MIT License - see the LICENSE file for details.
