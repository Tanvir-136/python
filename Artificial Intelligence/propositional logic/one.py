import itertools

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

    # Draw truth table
    def draw_table(self, li, *args):
        header = " | ".join(args)
        length = len(header)
        print("-" * length)
        print(header)
        print("-" * length)
        for row in li:
            print(" | ".join(str(i) for i in row))
        print("-" * length)

    # Generate truth table for expression
    def truth_table(self, expr, vars):
        print(f"Truth Table for: {expr}")
        header = vars + [expr]
        rows = []
        for values in itertools.product([0,1], repeat=len(vars)):
            env = dict(zip(vars, values))
            result = eval(expr, {}, env)
            rows.append([*values, int(result)])
        self.draw_table(rows, *header)

    # Check tautology/contradiction/satisfiability
    def check_formula(self, expr, vars):
        results = []
        for values in itertools.product([0,1], repeat=len(vars)):
            env = dict(zip(vars, values))
            results.append(eval(expr, {}, env))
        if all(results):
            print("Formula is a Tautology ✅")
        elif not any(results):
            print("Formula is a Contradiction ❌")
        else:
            print("Formula is Satisfiable ☑️")

# -----------------------------
# Example usage
# -----------------------------

r = Relation()
r.add("s", "students", "brilliant", singular=False)
r.add("a", "Tanvir", "student")
r.add("b", "Tanvir", "lazy")
r.add("c", "It", "raining")
r.add("d", "Road", "dry")

# Natural language from logic
r.build_statement("c ~ d")   # "It is raining implies Road is dry."
r.build_statement("a & !b")  # "Tanvir is student and Tanvir is not lazy."

# Truth table example
r.truth_table("p and (not q)", ["p","q"])

# Formula check
r.check_formula("p or (not p)", ["p"])   # Tautology
r.check_formula("p and (not p)", ["p"])  # Contradiction
