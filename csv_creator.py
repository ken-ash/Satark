import xml.etree.ElementTree as ET

tree = ET.parse('data.kml')
root = tree.getroot()

with open("data.csv","w") as file:
    file.write("latitude,longitude,crimeActivity\n")
    for i in root.findall("./Document/Folder/Placemark/Point/coordinates"):
        file.write(f"{i.text.strip()[:-2]}\n")
    print("done")
    
