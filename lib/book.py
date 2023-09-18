class Book:
    def __init__(self, title):
        self.title = title

    def get_page_count(self):
        try:
            return self._page_count
        except:
            return
    
    def set_page_count(self, page_count):
        if (type(page_count) == int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
    page_count = property(get_page_count, set_page_count)