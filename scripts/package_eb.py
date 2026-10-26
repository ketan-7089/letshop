import zipfile
import os
import shutil

src_dir = r"c:\Users\ketan\Desktop\letshop\eb-flask-app"
cc_dir = r"C:\Users\ketan\Desktop\CC lab 8"

# Read base files
with open(os.path.join(src_dir, "application.py"), "r", encoding="utf-8") as f:
    app_code_v1 = f.read()

with open(os.path.join(src_dir, "requirements.txt"), "r", encoding="utf-8") as f:
    req_code = f.read()

app_code_v2 = app_code_v1.replace("version='1.0'", "version='2.0'")

# Function to write zip
def make_zip(zip_path, app_content):
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("application.py", app_content)
        zf.writestr("requirements.txt", req_code)
    print(f"Created: {zip_path}")

# Create in CC lab 8
make_zip(os.path.join(cc_dir, "app-v1.zip"), app_code_v1)
make_zip(os.path.join(cc_dir, "app-v2.zip"), app_code_v2)

# Also create in letshop/eb-flask-app
make_zip(os.path.join(src_dir, "app-v1.zip"), app_code_v1)
make_zip(os.path.join(src_dir, "app-v2.zip"), app_code_v2)

print("Done packaging v1 and v2!")
