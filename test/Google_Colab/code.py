# Timeline creation in a Jupyter Notebook v25.10
# Please update your language code first, then hit the play button

language = "en"

# Step 1 - download all neccessary files
import os, urllib3, sys

%cd /content
current_path = os.getcwd()

# Create folder for database
folders = ["db", "images", "python", "python/fonts", "timeline"]
for folder in folders:
  new_path = current_path + "/" + folder
  if not os.path.exists(new_path):
    os.makedirs(new_path)

# Define function to import files to the virtual jupyter file system
def import_file(source, target):
  try:
    with urllib3.PoolManager() as http:
      with http.request('GET', source, preload_content=False, decode_content=False) as response:
        if response.status == 200:
          with open(target, 'wb') as file:
            for chunk in response.stream(8192):
              file.write(chunk)
            # print(f"Download complete. File saved as {target}")
            print(".", end="")
        else:
            print(f"Error: Unable to download file {source}. Status Code: {response.status}")
  except urllib3.exceptions.RequestError as e:
    print(f"Network Error: {e}")
  except Exception as e:
    print(f"Error: {e}")

path_required = "https://raw.githubusercontent.com/kreier/timeline/main/db/files_required.py"
import_file(path_required, "required.py")
import required
required.files.append(f"db/dictionary_{language}.csv")
required.files.append(f"images/qr-{language}.png")
print(f"Number of required files: {len(required.files)}. Downloading them now.")
current_file = 1
for file in required.files:
  source = "https://raw.githubusercontent.com/kreier/timeline/main/" + file
  target = file
  import_file(source, target)
  current_file += 1
  if current_file % 50 == 0:
    print(f" {current_file}")

# Step 2 - install dependencies
!pip install fpdf2
!pip install uharfbuzz
!pip install googletrans
!pip install qrcode

# Asyncio fix inside Google Colab
import nest_asyncio
nest_asyncio.apply()

# Start the 6000.py from the python subfolder, result will be in /timeline
%cd /content/python
sys.argv = ['fpdf2_6000.py',language, "_nwt"]
with open("fpdf2_6000.py") as file:
  exec(file.read())

# Download the generated pdf
from google.colab import files
files.download(f'/content/timeline/timeline_v{version}_{language}.pdf')
