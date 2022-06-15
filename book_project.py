from book_mini_project import *
class book_project:
    book_list=[]
    def execute(self,choice):
        if choice==1:
            print("************Add Books***********")
            book_id=int(input("Enter book_id:"))
            book_name=(input("Enter book_name:"))
            book_price=float(input("Enter book_price:"))
            book_publisher=(input("Enter book_publisher:"))
            book_author=(input("Enter book_author:"))
            book_obj=book(book_id,book_name,book_price,book_author,book_publisher)
            self.book_list.append(book_obj)


        elif choice==2:
            print("**********Search Book************")
            book_id=int(input("Enter the book id:"))
            for i in self.book_list:
                if i.book_id==book_id:
                    print(i)
                    break
            else:
                print("Invalid book")
                
        elif choice==3:
            print("*********Update Book***********")
            book_id=int(input("Enter book id:"))
            for i in self.book_list:
                if i.book_id==book_id:
                    i.set_book_name(input("Enter book name:"))
                    i.set_book_price(float(input("Enter book price:")))
                    i.set_book_author(input("Enter book author:"))
                    i.set_book_publisher(input("Enter book publisher:"))

        elif choice==4:
            print("**********Delete Book*************")
            found=False
            book_id=int(input("Enter the book id:"))
            for i in self.book_list:
                if i.book_id==book_id:
                    self.book_list.remove(i)
                    found=True
                    break
            if found==False:
                print("Invalid book")
                

        elif choice==5:
            print("*********Display Book***************")
            for i in range(len(self.book_list)):
                print(self.book_list[i])
            
        else:
            print("Invalid input")

while(True):
    print("Enter \n1.Add book \n2.Search book \n3.Update book \n4.Delete book \n5.Display book")
    choice=int(input("Enter your choice:"))
    book_project_obj=book_project()
    book_project_obj.execute(choice)


