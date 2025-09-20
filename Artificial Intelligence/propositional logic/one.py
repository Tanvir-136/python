class Statement:
    def __init__(self, subject, predicate, singular = True):
        self.subject = subject
        self.predicate = predicate
        self.singular = singular
        
class Relation:
    def __init__(self):
        self.map = {}
        
    def add(self, statement, subject, predicate, singular = True):
        self.map[statement] = Statement(subject, predicate, singular)
               
    def print_statement(self, statement):
        if self.map[statement].singular:
            print(self.map[statement].subject, " is ", self.map[statement].predicate, end="")
        else:
            print(self.map[statement].subject, " are ", self.map[statement].predicate end="")
            
    def print_neg_statement(self, statement):
        if self.map[statement].singular:
            print(self.map[statement].subject, " is not ", self.map[statement].predicate,  end="")
        else:
            print(self.map[statement].subject, " are not ", self.map[statement].predicate, end="")
    
    def build_statement(self, logic):
        logic = logic.replace(" ", "") # no space in the statement
        logic = logic.replace(",", "") # no comma in the statement
        
        neg = False
        only_sub = False
        
        for i in range(len(logic)):
            if logic[i] == '!':
                neg = True
            elif logic[i] == '&':
                print(" and ", end="")
            elif logic[i] == '|':
                print(" or ", end="")
            elif logic[i] == '*':
                print(" if and only if, ", end="")
            elif logic[i] == '~':
                print(" implies ", end="")
            elif logic[i] == 'A':
                print(" For all ", end="")
                only_sub = True
            elif logic[i] == 'E':
                print(" For some ", end="")
                only_sub = True
            elif logic[i] in ['(', ')', ',']:
                continue
            else:
                if only_sub:
                    print(self.map[logic[i]].subject, end="")
                    only_sub = False
                elif neg:
                    self.print_neg_statement(logic[i])
                    neg = False
                else:
                    self.print_statement(logic[i])
        print('.')
    def draw_table(li, *args):
        length = len(" | ". join(args))
        print("-" * length)
        print(" | ".join(args))
        print("-", length)
        for row in li:
            print(" | ".join(str(i) for i in row))
        print("-" * length)
        
r = Relation()

r.add("s", "students", "brilliant", singular=False)
r.add("a", "Tanvir", "student")
r.add("b", "Tanvir", "lazy")

# r.build_statement("A(s) s")
# r.build_statement("a & !b ~ a")

r.add("c", "It", "raining")
r.add("d", "Road", "dry")
r.build_statement("c ~ d")
# Example usage of draw_table with sample data and column names
sample_data = [
    [1, 0],
    [0, 1],
    [1, 1]
]
r.draw_table(sample_data, "c", "d")