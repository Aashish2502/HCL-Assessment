# **HCL Assessment**
 This is an assignment for HCL-Software recruitment.

 ## Installation and requirements
 To install all the dependencies and run the programs, do the following:
 - Clone the repository to your local machine
   ```
   git clone https://github.com/Aashish2502/HCL-Assessment .
   ```
 - Create a Python virtual environment
   ```
   python -m venv env
   ```
- Activate the virtual environment
  ```
  \env\Scripts\activate
  ```
- Install all the dependencies using requirements.txt
  ```
  pip install -m requirements.txt
  ```
## Files
- ### **_Email-Extraction_** :
  This folder includes the script to extract valid emails from a text file and output it into an Excel file. The folder contains a test.txt file, which consists of text for the test and also includes
an Excel file, containing the valid email addresses, is generated after the execution of the script.
- ### **_HTML-Parser_**:
  This folder includes the Python script to parse an HTML page containing product name, price, and quantity. BeautifulSoup is used to scrape the data from the page. The scripts output the product name and the price of the corresponding product.
- ### **_File_Validator_** :
  This folder contains the Python script to validate an uploaded file by checking their file signatures (magic numbers). In this script:
  - Initially, the file signature is read and then, it is verified if the file uploaded is of the allowed type or not.
  - Then, the file is checked for the allowed size.
  - The file is also checked for the corresponding extension.
  ### **_NOTE:_**
    The methods implemented in the script are too basic. There are several ways to implement a robust set of checks and safeguards to have a secure file upload, such as the following:
    - Scan the uploaded file for potentially harmful content, especially for embedded scripts in documents or malicious payloads in image files
    - Upload the file with a particular naming standard, to normalize paths and ensure files stay within the intended directory.
    - We can also implement role-based access control (RBAC) to restrict file upload permissions.
- ### **_string_calculation.py_**:
  This script calculates the sum of all integers within the string, containing digits and other characters. Continuous integers are to be considered as one number.
- ### **_main.ipynb_** :
  This notebook contains code for all the scripts discussed above and the output for the corresponding cell.

