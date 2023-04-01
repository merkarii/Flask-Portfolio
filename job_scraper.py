import requests
from bs4 import BeautifulSoup

def scrape_remoteok_job_listings(search_query, num_pages=1):
    base_url = "https://remoteok.io/remote"
    job_listings = []

    for page in range(1, num_pages + 1):
        url = f"{base_url}-{search_query}-jobs"
        if page > 1:
            url += f"/{page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        job_rows = soup.find_all('tr', class_='job')

        print(f"Scraping page {page}...")

        for job_row in job_rows:
            job_id = job_row['data-id']
            job_url = f"https://remoteok.io/l/{job_id}"
            job_title = job_row.find('td', class_='company_and_position').find('h2').text
            company = job_row.find('td', class_='company').find('h3').text

            job_listings.append({
                'title': job_title,
                'company': company,
                'url': job_url
            })

    return job_listings

search_query = "software"
print(f"Scraping job listings for '{search_query}'...\n")
job_listings = scrape_remoteok_job_listings(search_query, num_pages=2)

print("Scraped job listings:\n")
for job in job_listings:
    print(f"{job['title']} - {job['company']}\n{job['url']}\n")