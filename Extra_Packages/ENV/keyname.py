from dotenv import load_dotenv
import os

load_dotenv()

keyname = os.getenv('keyname')
print(keyname)
