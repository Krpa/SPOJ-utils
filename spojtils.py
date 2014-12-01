import os
import sys

#Base class for instructions revolving aroung TODO list.
class TodoInstruction(object):

    #location parameter = location of todo list file
    def __init__(self, location):
        self.location = location

    #execute instruction
    def doInstruction(self, args):
        print ("Doing instruction! Parameters:")
        print (args)

    #read todo list
    def readTodo(self):
        if not os.path.isfile(self.location):
            return []
        f = open(self.location, "r")
        result = []
        a = f.readline().strip()
        while a != "":
            result.append(a)
            a = f.readline().strip()
        f.close()
        return result

    #write todo list
    def writeTodo(self, lst):
        f = open(self.location, "w")
        for prob in lst:
            f.write(prob+"\n")
        f.close()


#Add to TODO list instruction
class Add(TodoInstruction):

    def __init__(self, location):
        super(Add, self).__init__(location)

    def doInstruction(self, args):
        problems = args.split(",")
        todo = self.readTodo()
        finalList = sorted(list(set(problems + todo)))
        self.writeTodo(finalList)

#init function, reads init file, initializes instructions
def init_function():
    todo_location = "TODO_LOCATION"
    init_file = "init.txt"
    init_params = {}
    location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    init = open(os.path.join(location, init_file), "r")
    s = init.readline().strip()
    while s != "":
        params = s.split("=")
        init_params[params[0]] = params[1]
        s = init.readline().strip()
    init.close()

    global instructions
    instructions = {}
    instructions["add"] = Add(init_params[todo_location])


if __name__ == "__main__":
    instructions = {}
    print(("Initializing..."))
    try:
        init_function()
    except:
        print (("Error initializing: ", sys.exc_info()[0], sys.exc_info()[1]))
        print ("Closing.")
        sys.exit(0)
    print(("Completed"))

    while(True):
        s = raw_input(">")
        command = s.split(" ")
        if not command[0] in instructions:
            print("Unknown instruction.")
            continue
        try:
            instructions[command[0]].doInstruction(command[1])
        except:
            print (("Error: ", sys.exc_info()[0], sys.exc_info()[1]))
