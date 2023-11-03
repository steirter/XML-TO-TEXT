from bs4 import BeautifulSoup as bs

with open('source/source.xml', 'r', encoding="utf-8") as f:
    data = f.read()

bs_data = bs(data, "xml")
b_item = bs_data.find_all('content:encoded')
i = 0

for item in b_item:
    f = open("output/pagina_%s.txt" % str(i), "w+", encoding="utf-8")
    for img_tag in item.find_all("img width="):
        img_tag.extract()
    cleaned_text = item.getText()
    f.write(cleaned_text)
    f.close()
    i += 1


