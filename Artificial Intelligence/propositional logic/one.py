from itertools import product 

class Statement:
    def __init__(self, subject, predicate, singular=True):
        self.subject = subject
        self.predicate = predicate
        self.singular = singular

class Relation:
    def __init__(self):
        self.map = {}

    # Add a statement
    def add(self, key, subject, predicate, singular=True):
        self.map[key] = Statement(subject, predicate, singular)

    # Print normal statement
    def print_statement(self, key):
        st = self.map[key]
        if st.singular:
            print(st.subject, "is", st.predicate, end="")
        else:
            print(st.subject, "are", st.predicate, end="")

    # Print negated statement
    def print_neg_statement(self, key):
        st = self.map[key]
        if st.singular:
            print(st.subject, "is not", st.predicate, end="")
        else:
            print(st.subject, "are not", st.predicate, end="")

    # Build natural language from logic formula
    def build_statement(self, logic):
        logic = logic.replace(" ", "").replace(",", "")
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
                print(" if and only if ", end="")
            elif logic[i] == '~':
                print(" implies ", end="")
            elif logic[i] == 'A':
                print("For all ", end=""); only_sub = True
            elif logic[i] == 'E':
                print("For some ", end=""); only_sub = True
            elif logic[i] in ['(', ')']:
                continue
            else:
                if only_sub:
                    print(self.map[logic[i]].subject, end=""); only_sub = False
                elif neg:
                    self.print_neg_statement(logic[i]); neg = False
                else:
                    self.print_statement(logic[i])
        print('.')

# Truth table function (kept structure similar)
def truth_table(expr):
    print("c d | output")
    for c, d in product([0,1], repeat=2):
        print(c, d, "|", int(expr(c, d)))

# -----------------------------
# Example usage
# -----------------------------

r = Relation()
r.add("s", "students", "brilliant", singular=False)
r.add("a", "Tanvir", "student")
r.add("b", "Tanvir", "lazy")
r.add("c", "It", "raining")
r.add("d", "Road", "wet")

# Natural language from logic
r.build_statement("c ~ d")   # "It is raining implies Road is dry."
r.build_statement("a & !b")  # "Tanvir is student and Tanvir is not lazy."

# Truth table example using lambda
expr = lambda c, d: (not c) or d     
truth_table(expr)


# # AND
# AND = lambda P, Q: P and Q

# # OR
# OR = lambda P, Q: P or Q

# # NOT
# NOT = lambda P: not P

# # IMPLIES (P → Q)
# IMPLIES = lambda P, Q: (not P) or Q

# # BICONDITIONAL (P ↔ Q)
# IFF = lambda P, Q: P == Q