def read_file(name_file):
    import xml.etree.ElementTree as ET
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(name_file, parser)
    root = tree.getroot()
    news_xml = root.findall("channel/item")
    return news_xml

def create_list(data):
    read_file("newsafr.xml")
    for news in data:
        a = news.find("title").text
        list_of_words = a.split(" ")
    return list_of_words

def sort_dict(dict):
    list_lider_word = list(dict.items())
    list_lider_word.sort(key=lambda i: i[1])
    list_lider_word.reverse()
    return list_lider_word[0:3]

def create_list_lider_word(file):
    #print(read_file(file))
    data = read_file(file)
    list_of_words = create_list(data)
    list_of_words_1 = [ ]
    counter_dict = { }
    for element in list_of_words:
        lenght_word = len(element)
        if lenght_word > 6:
            list_of_words_1.append(element)
            enter_count = list_of_words_1.count(element)
            counter_dict[element] = enter_count
    return counter_dict



print(create_list_lider_word("newsafr.xml"))


