def create_html(data):
    html = "<body><p style='text-align:center;'>"
    #data = ["http://mythicspoiler.com/mid/cards/wrennandseven2.jpg","http://mythicspoiler.com/mid/cards/wrennandseven2.jpg","http://mythicspoiler.com/mid/cards/wrennandseven2.jpg"]
    img_tag =""
    for i in data:
        img_tag += "<img src=" + i + "></img>"
    #print(img_tag)
    html += img_tag + "</p></body>"
    

    file = open("email.html","w")
    file.write(html)
    file.close()