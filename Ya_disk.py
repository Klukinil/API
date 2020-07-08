import requests


class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path


    def upload(self):
        file_path_splitted = self.file_path.split('\\')
        file_name = file_path_splitted[-1]

        response = requests.get(f'https://cloud-api.yandex.net:443/v1/disk/resources/upload?path=%2F{file_name}',
                            headers={'Authorization': 'OAuth '}, )
        info = response.json()
        href = info['href']

        with open(self.file_path, 'rb') as f:
            _file = f.read()

        r = requests.put(href, data=_file)
        print('Вcе ок')


if __name__ == '__main__':
    uploader = YaUploader('C:\\Users\\FX\\Desktop\\Note.jpg')
    result = uploader.upload()