import requests

# URL of the Google Fonts Latin glyph set (plist format)
GF_Latin_All = "https://github.com/googlefonts/glyphsets/raw/main/GF_glyphsets/Latin/glyphs/CustomFilter_GF_Latin.plist"

# Destination path where the file will be saved locally
dest = "sources/CustomFilter_GF_Latin_All.plist"

# Send a GET request to download the glyph set file
r = requests.get(GF_Latin_All)

# Write the downloaded content into the destination file in binary mode
with open(dest, "wb") as f:
    f.write(r.content)
