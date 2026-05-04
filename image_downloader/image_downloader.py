import os 
import requests

def get_extension(url: str) -> str | None:
    extensions: list[str] = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp', 'svg']
    for ext in extensions:
        if ext in url:
            return ext
        
def download_image(url: str, name: str, folder: str = None):
    if ext := get_extension(url):
        if folder:
            image_name: str = f'{folder}/{name}.{ext}'
        else:
            image_name: str = f'{name}.{ext}'

    else:
        raise Exception('Image extension not found in URL')
    
    if os.path.exists(image_name):
        raise Exception('File name already exists')
    
    # Download image
    try:
        image_content: bytes = requests.get(url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Image downloaded successfully: {image_name}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    input_url:str = input('Enter URL: ')
    input_name:str = input('Enter name: ')

    print('Downloading...')
    download_image(input_url, name=input_name, folder='image_downloader/images')
