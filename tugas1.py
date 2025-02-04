def main ():
    try: 
        bookList =[]
        infile = open("theBookList", "r")
        line = infile.readline()
        while line:
            bookList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()
    except FileNotFoundError:
        print("the <booklist.txt> is not found")
        print ("starting a new book in list!")
        bookList=[]
    
    choice = 0
    while choice != 4: 
        print("=============Book Manager++++++++++++")
        print("1.) add a book")
        print("2.) lookup a book")
        print("3.) display a book")
        print("4.) Quit")
        choice = int(input())
        
        if choice == 1:
            print("=====Add A Book====")
            nBook = input("Enter the name of Book ==>")
            nAuthor =  input("Enter the name of author ==> ")
            nPages = input("Enter the year of book ==> ")
            
            bookList.append([nBook, nAuthor, nPages]) 
        elif choice == 2:
            print("Lookup the book ...")
            keyword = input("Enter search term : ")
            for book in bookList:
                if keyword in book:
                    print(book) 
                    
        elif choice == 3:
            print("Display a book ... ")
            for i in range(len(bookList)):
                print(bookList[i])
                
        elif choice == 4:
            print("Quit Program!")
            
        print ("program terminated!") 
        
        # saving to external file/.txt 
        outfile = open('theBookList.txt', 'w') 
        for book in bookList: 
            outfile.write(",".join(book)+ "\n")
        outfile.close()  
            
if __name__ == "__main__":
    main()