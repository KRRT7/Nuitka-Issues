# https://github.com/Nuitka/Nuitka/issues/3098

import requests

response = requests.get("https://www.example.com")
print(response.text)
