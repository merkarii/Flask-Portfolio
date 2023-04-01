# JobScrapping-BeautifulScoup
Job Scraper
This job scraper is a simple Python script that scrapes job listings from Remote OK based on a given search query.

Features
Scrapes job listings from Remote OK
Supports multiple pages of job listings
Extracts job title, company, and URL for each job listing
Displays job listings in the terminal
Prerequisites
You need to have Python 3 installed on your system. You can download it from the official website.

Dependencies
Requests
Beautiful Soup 4
You can install the dependencies by running the following command:

bash
Copy code
pip install -r requirements.txt
Usage
Clone this repository or download the job_scraper.py file.
Open the terminal or command prompt and navigate to the folder containing the script.
Set your desired search query in the search_query variable within the script.
Set the number of pages you want to scrape in the num_pages parameter when calling the scrape_remoteok_job_listings function.
Run the script using the following command:
bash
Copy code
python job_scraper.py
The script will then scrape the job listings and display them in the terminal.

Customization
You can customize the script to scrape job listings for different queries or to fetch more job listings by modifying the search_query variable and the num_pages parameter.

For example:

python
Copy code
search_query = "data scientist"
job_listings = scrape_remoteok_job_listings(search_query, num_pages=3)
This will scrape job listings for "data scientist" from the first three pages of the search results.
