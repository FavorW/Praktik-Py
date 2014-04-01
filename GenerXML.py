from lxml import etree
for x in range(10):
    numfile = str(x)
    root = etree.Element("mo")
    etree.SubElement(root, "atriboot").text = "TEST"+numfile
    etree.SubElement(root, "customer").text = "content"+numfile
    app_window = etree.tostring(root)
    root = etree.Element("root")
    root.append(etree.XML(app_window))
    handle = str(etree.tostring(root, pretty_print=True, encoding='utf-8', xml_declaration=True))
    applic = open("app"+numfile+".xml", "w")
    applic.writelines(handle)
    applic.close()
    applic = open("app"+numfile+".xml", "r")
    # Удаление лишнего после генерации
    for line in applic.readlines():
       temp = list(line)
    applic.close()
    for y in range(144):
        if temp[y-1]+temp[y] == "\\n":
          temp[y] = ''
          temp[y-1] = ''
    temp[0] = ''
    temp[1] = ''
    temp[143]=''

    applic = open("app"+numfile+".xml", "w")
    applic.writelines(temp)
    applic.close()
