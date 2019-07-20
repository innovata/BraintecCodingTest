
import xml.etree.ElementTree as ET


def handle_uploaded_xml(file):
    try:
        binary = file.read()
    except Exception as e:
        print(f"{'#'*50} {__name__}\nException : {e}")
    else:
        decstr = binary.decode(encoding="utf-8", errors="strict")
        root = ET.fromstring(decstr)
        for contact in root.findall('.'):
            print(f"contact : {contact}")
            data = {
                'firstname':contact.find('firstname').text,
                'lastname':contact.find('lastname').text,
                'email':contact.find('email').text,
                'address':contact.find('address').text,
                'phone':contact.find('phone').text,
            }
        return data
