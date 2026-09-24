import json, zlib, base64, urllib.parse
from pathlib import Path
import xml.etree.ElementTree as ET

path = Path(r"d:\\vision-reel\\usecase-diagram\\UC-19-Ceremonies-Event-Rehearsal.drawio")
root = ET.parse(path).getroot()
# first page's mxGraphModel
model = next(root.iter("mxGraphModel"))
xml = ET.tostring(model, encoding="unicode")

compressor = zlib.compressobj(level=9, method=zlib.DEFLATED, wbits=-15)
data = base64.b64encode(compressor.compress(xml.encode("utf-8")) + compressor.flush()).decode("ascii")

payload = json.dumps({"type": "xml", "compressed": True, "data": data}, separators=(",", ":"))
url = "https://app.diagrams.net/?grid=0&pv=0&border=10&edit=_blank#create=" + urllib.parse.quote(payload)
print(url)