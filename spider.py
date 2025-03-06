import requests
from bs4 import BeautifulSoup

url = 'https://github.com/trending'
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    repo_element = soup.find('h2', {'class': 'h3 lh-condensed'})
    
    if repo_element:
        repo_name = repo_element.find('a').get('href').strip('/')
        print(repo_name)
    else:
        print("ERROR: No trending repo found")
except Exception as e:
    print(f"ERROR: {str(e)}")
    exit(1)
