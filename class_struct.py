# coding: utf-8
import xml.etree.ElementTree

with open("./class.xml", "r", encoding="utf-8") as f:
    # tree = xml.etree.ElementTree.fromstring(f.read())
    tree = xml.etree.ElementTree.parse(f)
student_ip_map = {}
user_data = tree.getroot().find("students").findall("student")
for i in user_data:
    name = i.find("name").text
    ip = i.find("address").attrib['IP']
    student_ip_map[ip] = name
student_ip_map["127.0.0.1"] = "教师"
