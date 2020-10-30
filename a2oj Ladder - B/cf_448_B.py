t = input()
s = input()

automaton = False

if len(t) != len(s) and s in t:
    automaton = True
else:
