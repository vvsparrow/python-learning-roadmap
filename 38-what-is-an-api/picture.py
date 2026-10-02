from io import BytesIO

import requests
from PIL import Image

r = requests.get("")
i = Image.open(BytesIO(r.content))
i.show()
