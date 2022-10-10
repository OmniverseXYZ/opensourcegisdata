from pandas import *

def files(filename):
    f = open(filename + ".html", "w+")
    s = filename
    f.write(s)
    f.close()

data = read_csv("states.csv")
state_list = data["states"].to_list()
print(state_list)

for state in state_list:
    files(state)