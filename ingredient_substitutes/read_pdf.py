from curses.ascii import isupper
import PyPDF2

FILE_PATH = 'book.pdf'

class PageReader:
    
    pageContent = None
    text = None
    redirections = {}
    ingredients = {}
    
    def __init__(self, page):
        self.page = page
        self.text = self.page.extract_text()
        self.extract_descriptions()
        
    def extract_descriptions(self):
        lines = self.text.split('\n')
        # remove ingredients which are redirected to a different ingredient
        redirections_list = [l for l in lines if "See" in l and "." and l.replace("See","").replace(".","").isupper()]
        for item in redirections_list:
            lines.remove(item)
            item_from = item[ : item.find("See")-1].rstrip().lower()
            item_to = item[item.find("See")+3 : 1].lstrip().lower()
            self.redirections[item_from] = item_to
        # get ingredient with its description
        ingredient_idxs =  [idx for idx,line in enumerate(lines) if line.isupper() and len(line)>1]
        for start_idx, end_idx in zip(ingredient_idxs,ingredient_idxs[1:]):
            ingredient_name = lines[start_idx].lower()
            unfiltered_description = "".join(lines[start_idx + 1 : end_idx])
            categories = unfiltered_description.split("SUBSTITUTE ")
            definition, substitute = categories[0], categories[1]
            substitutes = substitute.replace("\xa0g","g").replace("\xa0lb", "lb").replace("\xa0oz", "oz").lstrip()
            split_substitute_what_from_idx = substitutes.find("with")
            substitute_what = substitutes[:split_substitute_what_from_idx]
            substitute_from = substitutes[split_substitute_what_from_idx + 4:].split("• ")
            # print(substitute_from)
            substitute_what = substitutes[0]
            substitute_with = substitutes[1:]
            self.ingredients[ingredient_name] = {
                "definition": definition, 
                "substitute_what": substitute_what, 
                "substitute_with": substitute_with
            } 
            
        

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
        return self.fileReader.pages[pageNum]

class PageIterator:
    pass

book = BookReader(FILE_PATH)
page_6 = book.get_page(6)
p = PageReader(page_6)
print(p.ingredients)