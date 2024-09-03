# https://github.com/Nuitka/Nuitka/issues/3098
# report: requests module does not work with Nuitka

import requests

response = requests.get("https://www.example.com")
print(response.text)
