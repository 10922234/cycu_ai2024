from lxml import etree
import csv

# Load and parse the XML file
tree = etree.parse("ETagPair.xml")
root = tree.getroot()

# Open a CSV file in write mode
with open("ETagPair.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    # Write the header dynamically
    headers = [ETagPairID.tag for ETagPairID in root.find(".//ETagPair")]
    writer.writerow(headers)

    # Extract data from XML and write to CSV dynamically
    for ETagPair in root.findall("student"):
        row_data = [element.text for element in student]
        writer.writerow(row_data)