import xml.etree.ElementTree as ET

tree = ET.parse('USD_BS4.xml')
root = tree.getroot()

data = []
data.append(root.text.strip())
for child in root.iter('span'):
    data.append(child.text.strip())
del data[1]

# # convert list data to dict with tag
# key = [data[1],data[2]]
# value = [data[3],data[4]]
# my_dict = dict(zip(key,value))

# print(data[0]+str(my_dict))

print(data)
