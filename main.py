import requests
import csv

def scrape_unsplash(page):
    url = f"https://unsplash.com/napi/search/photos?query=nature&xp=&per_page=20&page={page}"
    response = requests.get(url).json()
    return response

csvfile = open('UnsplashPhotos.csv', 'w', encoding='utf-8')
writer = csv.writer(csvfile)
writer.writerow(['Photo ID', 'Photo URL', 'Photographer', 'Photographer URL'])

for i in range(1, 6):
    data = scrape_unsplash(i)
    for photo in data['results']:
        photo_id = photo['id']
        photo_url = photo['urls']['full']
        photographer = photo['user']['name']
        photographer_url = photo['user']['links']['html']
        writer.writerow([photo_id, photo_url, photographer, photographer_url])

csvfile.close()
