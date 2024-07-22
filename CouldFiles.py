import requests


class CouldFile:
    def __init__(self, could_folder, token):
        self.could_folder = could_folder
        self.token = token
        self.base_url = ""

    def load(self, path):
        with open(path, 'rb') as file:
            response = requests.post(f"{self.base_url}/upload",
                                     files={"file": file},
                                     data={"folder": self.could_folder})
        return response.status_code == 200

    def reload(self, path):
        return self.load(path)

    def delete(self, filename):
        response = requests.post(f"{self.base_url}/delete/{self.could_folder}/{filename}")
        return response.status_code == 200

    def get_info(self):
        response = requests.get(f"{self.base_url}/list/{self.could_folder}")
        return response.json()
