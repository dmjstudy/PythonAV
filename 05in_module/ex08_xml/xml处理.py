__author__ = "Alex Li"

import xml.etree.ElementTree as ET

# tree = ET.parse("xmltest.xml")
tree = ET.parse("http://www.nnmap.net/mapapps/PoiSearchService?&orderfield=qhpx&ordertype=asc&citycode=&hightlight=false&pageindex=1&pagesize=10&request=keyword&returntype=xml&searchname=上林")
root = tree.getroot()
print(root.tag)


# 遍历 xml 文档
for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print("--",i.tag, i.text,i.attrib)

# 只遍历year 节点 学习
# for node in root.iter('year'):
#     print(node.tag, node.text)