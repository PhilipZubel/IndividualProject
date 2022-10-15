import PyPDF2

FILE_PATH = 'book.pdf'

class BookReader:
    
    fileName = None
    fileReader = None
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.load_book()
    
    def load_book(self):
        try:
            self.fileReader = PyPDF2.PdfFileReader(self.fileName)
            print(self.fileReader)
            print(f"Successfully read {self.fileName}")
        except:
            self.fileReader = None
            print(f"Cannot read {self.fileName}")
    
    def get_number_of_pages(self):
        if self.fileReader == None: 
            return None
        return len(self.fileReader.pages)
    
    def get_page(self, pageNum):
        if self.fileReader == None: 
            return None
        print("hello")
        return self.fileReader.pages[pageNum]['/PieceInfo']



book = BookReader(FILE_PATH)
page_num = book.get_page(3)
print(page_num)