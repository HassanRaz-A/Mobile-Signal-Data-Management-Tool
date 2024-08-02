Mobile Signal Data Management Tool
This application allows users to manage mobile signal data using an Excel file only in USA Region and for the these Carries AT&T, T-Mobile, Verizon. It provides functionalities to look up existing data and add new entries via a graphical user interface (GUI) built with Tkinter. The tool utilizes Pandas for data handling and manipulation.

Features
Lookup Tool: Search for mobile signal data by column and value.
Add New Data: Submit new entries to the Excel file.
Data Handling: Load and save data from/to an Excel file.
User-Friendly GUI: Intuitive interface for searching and adding data.
Requirements
Python 3.x
pandas
openpyxl (for Excel file handling)
tkinter (standard library)
Installation
Clone the Repository:
sh
Copy code
git clone https://github.com/yourusername/your-repository.git
Navigate to the Project Directory:
sh
Copy code
cd your-repository
Install Dependencies:
sh
Copy code
pip install pandas openpyxl
Usage
Prepare Your Excel File:
Ensure the Excel file is located at the specified path in the script:

python
Copy code
file_path = r"C:\Users\user\DTS Dropbox\Ehsan Nawaz\Old Dropbox files\Post Processing\Hassan_Raza\personal\HAssan BAlti\Frequency Bands\Channel list.xlsx"
The file should contain columns: Band Name, Bands, UP-LINK, DOWN-LINK, ERFCN, and Carrier.

Run the Application:
Execute the script:

sh
Copy code
python your_script.py
A GUI window will open with two tabs:

Lookup Tool: Search for data by selecting a column and entering a value.
Add New Data: Add new data entries by filling out the form and submitting.
Interacting with the GUI:

In the Lookup Tool tab, select a column, enter a value, and click "Search" to view results.
In the Add New Data tab, fill out the form and click "Submit" to add new data to the Excel file.
Error Handling
If the specified Excel file is not found, a new DataFrame will be created.
Any errors during data loading or saving will be displayed in a message box.
