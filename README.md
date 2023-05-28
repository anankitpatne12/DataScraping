# Selenium Web Scraping Project

This is a web scraping project developed using Selenium, a powerful browser automation tool, to extract author names, book lengths, and titles from Amazon Audible's best sellers. The extracted data is stored in a CSV file for further analysis and processing.

## Project Overview

The main objective of this project is to gather information about the best-selling books on Amazon Audible. By automating the web scraping process with Selenium, we are able to extract the following details:

- Author Names: The names of the authors of the best-selling books.
- Book Lengths: The duration or length of the audio books.
- Titles: The titles or names of the books.

## Technologies Used

- Selenium: A browser automation framework that allows us to interact with web pages, perform actions, and extract data.
- Python: The programming language used for developing the web scraping project.
- CSV: The extracted data is stored in a CSV (Comma-Separated Values) file for easy storage and analysis.

## Setup and Installation

1. Clone the repository: `git clone https://github.com/your-username/project.git`
2. Navigate to the project directory: `cd project`
3. Create a virtual environment: `python -m venv env`
4. Activate the virtual environment:
   - For Windows: `env\Scripts\activate`
   - For macOS/Linux: `source env/bin/activate`
5. Install the project dependencies: `pip install -r requirements.txt`
6. Download and install the appropriate web driver for Selenium (e.g., ChromeDriver for Google Chrome).
7. Update the web driver path in the project code to match your system configuration.
8. Run the project: `python main.py`

## Usage

1. Make sure the project dependencies are installed and the web driver is properly configured.
2. Run the project using the command mentioned above.
3. The program will launch a web browser and automatically navigate to the Amazon Audible best sellers page.
4. It will then scrape the required information such as author names, book lengths, and titles from the web page.
5. The extracted data will be stored in a CSV file named `output.csv` in the project directory.
6. You can analyze and process the data further using your preferred tools or programming languages.

## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## Acknowledgements

- [Selenium Documentation](https://www.selenium.dev/documentation/): Official documentation for the Selenium framework.
- [Amazon Audible](https://www.audible.com/): Source of the best sellers data used in the project.

---
