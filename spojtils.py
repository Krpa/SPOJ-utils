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
        print (self.prepareArguments(self, args))

    def prepareArguments(self, args):
        arguments = args.split(",")
        problems = []
        for arg in arguments:
            if arg.strip() != "":
                problems.append(arg.strip())
        return problems

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
            if prob.strip() != "":
                f.write(prob.strip()+"\n")
        f.close()


#Add to TODO list instruction
class Add(TodoInstruction):

    def __init__(self, location):
        super(Add, self).__init__(location)

    def doInstruction(self, args):
        problems = self.prepareArguments(args)
        todo = self.readTodo()
        finalList = sorted(list(set(problems + todo)))
        self.writeTodo(finalList)

#Delete problems from TODO list
class Del(TodoInstruction):

    def __init__(self, location):
        super(Del, self).__init__(location)

    def doInstruction(self, args):
        problems = self.prepareArguments(args)
        todo = self.readTodo()
        finalList = []
        for prob in todo:
            if not prob in problems:
                finalList.append(prob)
        self.writeTodo(finalList)

#Prints todo list to console
class List(TodoInstruction):

    def __init__(self, location):
        super(List, self).__init__(location)

    def doInstruction(self, args):
        todo = self.readTodo()
        print "TODO List:"
        print "================"
        for prob in todo:
            print prob
        print "================"

#Clears todo list
class Clear(TodoInstruction):

    def __init__(self, location):
        super(Clear, self).__init__(location)

    def doInstruction(self, args):
        self.writeTodo([])

#Generates Html document for todo list
class getHtml(TodoInstruction):

    def __init__(self, location):
        super(getHtml, self).__init__(location)

    def doInstruction(self, args):
        arguments = self.prepareArguments(args)
        if len(arguments) == 0:
            print "No argument given."
            return
        path = arguments[0]
        todo = self.readTodo()
        f = open(path, "w")
        f.write("<html>\n")
        f.write("<head><h2> TODO List: </h2></head>\n")
        f.write("<body>\n")
        for prob in todo:
            f.write("<a href=\"http://www.spoj.com/problems/" + prob + "/\">" + prob + "</a><br>")
        f.write("</body>\n")
        f.write("</html>\n")
        f.close()

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
    instructions["del"] = Del(init_params[todo_location])
    instructions["ls"] = List(init_params[todo_location])
    instructions["clear"] = Clear(init_params[todo_location])
    instructions["getHtml"] = getHtml(init_params[todo_location])

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
        if len(command) == 1:
            command.append("")
        try:
            instructions[command[0]].doInstruction(command[1])
        except:
            print (("Error: ", sys.exc_info()[0], sys.exc_info()[1]))
