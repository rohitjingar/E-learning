import requests
from PIL import Image
from io import BytesIO

PEXELS_API_KEY = 'AoT9H8x2uZgTu8MQNeK8KiZ3aL30KJLQc6vqHEFiA5iBX2NIDNqa9crV'
def generate_course_image(course_name):
    url = f'https://api.pexels.com/v1/search?query={course_name}&per_page=1&page=1'
    headers = {'Authorization': PEXELS_API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data['total_results'] > 0:
            photo_url = data['photos'][0]['src']['medium']
            image_response = requests.get(photo_url)
            image = Image.open(BytesIO(image_response.content))
            return image
    return None