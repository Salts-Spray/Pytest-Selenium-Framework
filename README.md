DemoQA Automation Testing Project
---------------------------------

This project is an automation testing suite for the DemoQA website, built using Python, Selenium WebDriver, and pytest. It includes test cases to validate various functionalities on the site.

Installation:
-------------

1. Clone the Repository:

   git clone https://github.com/your-username/DemoQA-Automation.git
   cd DemoQA-Automation

2. Create a Virtual Environment:

   python -m venv venv

3. Activate the Virtual Environment:

   - On Windows:

     venv\Scripts\activate

   - On macOS/Linux:

     source venv/bin/activate

4. Install Requirements:

   pip install -r requirements.txt

How to Use:
-----------

1. Run All Tests:

   pytest

2. Run Specific Test Module:

   pytest -m smoke

3. Generate HTML Report:

   pytest --html=report.html

Requirements:
-------------

The required Python packages are listed in the `requirements.txt` file:

- selenium
- pytest
- pytest-html
- webdriver-manager
