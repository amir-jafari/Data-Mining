# -----------------------------------------
from dotenv import load_dotenv
import os
# -----------------------------------------
# create a .env file in the directory and add the following line
# keyname = 'Secret Key'
load_dotenv()
# -----------------------------------------

keyname = os.getenv('keyname')
print(keyname)
