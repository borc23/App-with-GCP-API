from flask import Flask, request, render_template
from googleapiclient.discovery import build
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find_similar_images', methods=['POST'])
def find_similar_images():
    image_url = request.form['image_url']
    api_key = 'AIzaSyBRDpX8O4QYgGSaobXB-TqLDr-jyaxtkiY'
    service = build("vision", "v1", developerKey=api_key)
    vision_request = service.images().annotate(body={
        'requests': [{
            'image': {
                'source': {
                    'imageUri': image_url
                }
            },
            'features': [{
                'type': 'WEB_DETECTION'
            }]
        }]
    })
    response = vision_request.execute()
    web_detection = response['responses'][0]['webDetection']
    result = []
    if 'visuallySimilarImages' in web_detection:
        for image in web_detection['visuallySimilarImages']:
            result.append(image['url'])

    return render_template('result.html', urls=result)

if __name__ == '__main__':
    app.run()

