# Book project
class book:

    def __init__(self,book_id,book_name,book_price,book_publisher,book_author): # these all are local variables
        self.book_id=book_id
        self.book_name=book_name
        self.book_price=book_price
        self.book_publisher=book_publisher
        self.book_author=book_author
    
    def __str__(self): #overridding
    
        return f"Book_id:{self.book_id} \nBook_name:{self.book_name} \nBook_price:{self.book_price} \nBook_publisher:{self.book_publisher} \nBook_author:{self.book_author}"
    
    def set_book_id(self,book_id):
        self.book_id=book_id
    def set_book_name(self,book_name):
        self.book_name=book_name
    def set_book_price(self,book_price):
        self.book_price=book_price
    def set_book_author(self,book_author):
        self.book_author=book_author
    def set_book_publisher(self,book_publisher):
        self.book_publisher=book_publisher
    
    def get_book_id(self):
        return self.book_id
    def get_book_name(self):
        return self.book_name
    def get_book_price(self):
        return self.book_price
    def get_book_publisher(self):
        return self.book_publisher
    def get_book_author(self):
        return self.book_author


