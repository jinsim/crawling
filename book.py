def extract_info(book_list):
    result = []
    for book in book_list:
        title = book.find("a", {"class" : "N=a:bta.title"}).string
        img_src = book.find("img")["src"]
        link = book.find("div", {"class" : "thumb_type thumb_type2"}).find("a")["href"]
        author = book.find("dd", {"class" : "txt_block"}).find("a", {"class" : "txt_name N=a:bta.author"}).string
        publisher = book.find("dd", {"class" : "txt_block"}).find("a").string

        book_info = {
            "title" : title,
            "img_src" : img_src,
            "link" : link,
            "author" : author,
            "publisher" : publisher
        }
        result.append(book_info)
    
    return result

    print(result)

    #  제목 • 이미지 주소 • 상세 페이지 링크 • 저자 • 출판사 • 가격(optional)