import requests
import json

repose = requests.get('https://rest.coincap.io/v3/assets/?apiKey=e90b70ff5e0c28a0900167f6d7b2e9faea7758cc1edb5ae07a7b0ffdddf6ccb0',
                    )
contxt = repose.json()
data = json.dumps(contxt, ensure_ascii=False, indent=2)


