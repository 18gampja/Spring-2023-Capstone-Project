def divider():
    print("-------------------------")

class turtleBot:
    '''
    Task Syntax: SYNTAX SENSITIVE 
    (
        Priority (Lowest First)
        ID (Allows for correct removal of duplicate tasks)
        Task Name (One word only, case sensitive)
    )
    '''
    def __init__(self):
        self.objectives = [(10, 10, "Finish_Scan")]
        self.id = 0
        self.partners = []

    def Execute_Next(self, task=None):
        nextTask = self.objectives[0]
        runTask = getattr(self, nextTask[2])
        print(f"Attempting to execute the task: '{nextTask}'.")
        divider()
        taskStatus = runTask(nextTask)
        if taskStatus != 1:
            print(f"There was an error completing the task: {nextTask}.")
            divider()
        else:
            for task in self.objectives:
                if task[1] == nextTask[1]:
                    self.objectives.remove(task)
                    print(f"The task '{nextTask}' has been executed and removed from Turtlebot's Task Queue.")
                    divider()
                    self.Print_Queue()

        if len(self.objectives) > 0:
            self.Execute_Next()

    def Add_Task(self, priority, id, taskName):
        newTask = (priority, id, taskName)
        try:
            getattr(self, taskName)
            self.objectives.append(newTask)
            print(f"The task '{newTask}' has been added to the Task Queue for Turtlebot.")
            self.Print_Queue()
        except:
            print(f"Error: No Task Name titled: {taskName}")            

    def Sort_Queue(self, task=None):
        self.objectives.sort()

    def Print_Queue(self, task=None):
        self.Sort_Queue()
        print(f"Remaining Tasks: {len(self.objectives)}")
        divider()
        for task in self.objectives:
            print(task)

    def Finish_Scan(self, task=None):
        if len(self.objectives) == 1:
            print(f"All Turtlebot tasks completed, Turtlebot is now awaiting further instruction.")
            divider()
            return 1
        else:
            print(f"Error: Task Queue not empty. Turtlebot cannot finish the scan.")
            divider()
            return 2
    
    def Placeholder_Task(self, task=None):
        print(f"Placeholder task 'ID: {task[2]}' completed.")
        divider()
        return 1

    # UNDONE
    # This function will take the map from the LIDAR scan of the room and slice it up into even sections.
    def sliceMap(self, task=None):
        return 0

    # UNDONE
    # This function will take the sliced map from the sliceMap() function and distribute them amongst the TurtleBot and M5s.
    def distributeSlices(self, task=None):
        return 0

    # UNDONE
    # This function will traverse the TurtleBot to a given location based on its (X,Y) coordinates.
    def gotoCell(self, task=None):
        return 0

    # UNDONE
    # This function will rotate the TurtleBot a given number of degrees.
    def rotateTB(self, task=None):
        return 0

    # UNDONE
    # This function will utilize the TurtleBot's camera to analyze the current onject to determine if it is a softball.
    def analyzeObject(self, task=None):
        return 0

    # UNDONE
    # This function will detect objects within a certain radius of the M5.
    def detectObjects(self, task=None):
        return 0

class sightedM5:
    '''
    Task Syntax: SYNTAX SENSITIVE 
    (
        Priority (Lowest First)
        ID (Allows for correct removal of duplicate tasks)
        Task Name (One word only, case sensitive)
    )
    '''
    def __init__(self):
        self.objectives = [(10, 10, "Finish_Scan")]
        self.id = 0
        self.partners = []

    def Execute_Next(self, task=None):
        nextTask = self.objectives[0]
        runTask = getattr(self, nextTask[2])
        print(f"Attempting to execute the task: '{nextTask}'.")
        divider()
        taskStatus = runTask(nextTask)
        if taskStatus != 1:
            print(f"There was an error completing the task: {nextTask}.")
            divider()
        else:
            for task in self.objectives:
                if task[1] == nextTask[1]:
                    self.objectives.remove(task)
                    print(f"The task '{nextTask}' has been executed and removed from M5: {self.id}'s Task Queue.")
                    divider()
                    self.Print_Queue()

        if len(self.objectives) > 0:
            self.Execute_Next()

    def Add_Task(self, priority, id, taskName):
        newTask = (priority, id, taskName)
        try:
            getattr(self, taskName)
            self.objectives.append(newTask)
            print(f"The task '{newTask}' has been added to the Task Queue for M5: {self.id}.")
            self.Print_Queue()
        except:
            print(f"Error: No Task Name titled: {taskName}")            

    def Sort_Queue(self, task=None):
        self.objectives.sort()

    def Print_Queue(self, task=None):
        self.Sort_Queue()
        print(f"Remaining Tasks: {len(self.objectives)}")
        divider()
        for task in self.objectives:
            print(task)

    def Finish_Scan(self, task=None):
        if len(self.objectives) == 1:
            print(f"All of M5: {self.id} tasks completed, M5: {self.id} is now awaiting further instruction.")
            divider()
            return 1
        else:
            print(f"Error: Task Queue not empty. M5: {self.id} cannot finish the scan.")
            divider()
            return 2
    
    def Placeholder_Task(self, task=None):
        print(f"Placeholder task 'ID: {task[2]}' completed.")
        divider()
        return 1

    # UNDONE
    # This function will traverse the M5 to a given location based on its (X,Y) coordinates.
    def gotoCell(self, task=None):
        return 0

    # UNDONE
    # This function will rotate the M5 a given number of degrees.
    def rotateM5(self, task=None):
        return 0

    # UNDONE
    # This function will utilize the M5's camera to analyze the current onject to determine if it is a softball.
    def analyzeObject(self, task=None):
        return 0
    
    # UNDONE
    # This function will detect objects within a certain radius of the M5.
    def detectObjects(self, task=None):
        return 0

class blindM5:
    '''
    Task Syntax: SYNTAX SENSITIVE 
    (
        Priority (Lowest First)
        ID (Allows for correct removal of duplicate tasks)
        Task Name (One word only, case sensitive)
    )
    '''
    def __init__(self):
        self.objectives = [(10, 10, "Finish_Scan")]
        self.id = 0
        self.partners = []

    def Execute_Next(self, task=None):
        nextTask = self.objectives[0]
        runTask = getattr(self, nextTask[2])
        print(f"Attempting to execute the task: '{nextTask}'.")
        divider()
        taskStatus = runTask(nextTask)
        if taskStatus != 1:
            print(f"There was an error completing the task: {nextTask}.")
            divider()
        else:
            for task in self.objectives:
                if task[1] == nextTask[1]:
                    self.objectives.remove(task)
                    print(f"The task '{nextTask}' has been executed and removed from M5: {self.id}'s Task Queue.")
                    divider()
                    self.Print_Queue()

        if len(self.objectives) > 0:
            self.Execute_Next()

    def Add_Task(self, priority, id, taskName):
        newTask = (priority, id, taskName)
        try:
            getattr(self, taskName)
            self.objectives.append(newTask)
            print(f"The task '{newTask}' has been added to the Task Queue for M5: {self.id}.")
            self.Print_Queue()
        except:
            print(f"Error: No Task Name titled: {taskName}")            

    def Sort_Queue(self, task=None):
        self.objectives.sort()

    def Print_Queue(self, task=None):
        self.Sort_Queue()
        print(f"Remaining Tasks: {len(self.objectives)}")
        divider()
        for task in self.objectives:
            print(task)

    def Finish_Scan(self, task=None):
        if len(self.objectives) == 1:
            print(f"All of M5: {self.id} tasks completed, M5: {self.id} is now awaiting further instruction.")
            divider()
            return 1
        else:
            print(f"Error: Task Queue not empty. M5: {self.id} cannot finish the scan.")
            divider()
            return 2
    
    def Placeholder_Task(self, task=None):
        print(f"Placeholder task 'ID: {task[2]}' completed.")
        divider()
        return 1

    # UNDONE
    # This function will traverse the M5 to a given location based on its (X,Y) coordinates.
    def gotoCell(self, task=None):
        return 0

    # UNDONE
    # This function will rotate the M5 a given number of degrees.
    def rotateM5(self, task=None):
        return 0

    # UNDONE
    # This function will detect objects within a certain radius of the M5.
    def detectObjects(self, task=None):
        return 0

    # UNDONE
    # This function will call the closest 'sighted' partner to the location of the M5 for assistance.
    def callForHelp(self, task=None):
        return 0

divider()

tb = turtleBot()

m5_1 = sightedM5()
m5_2 = blindM5()
m5_3 = blindM5()
m5_4 = blindM5()
m5_5 = blindM5()

bots = []
m5s = []

bots.append(tb)

m5s.append(m5_1)
bots.append(m5_1)
m5s.append(m5_2)
bots.append(m5_2)
m5s.append(m5_3)
bots.append(m5_3)
m5s.append(m5_4)
bots.append(m5_4)
m5s.append(m5_5)
bots.append(m5_5)

m5Count = len(m5s)
botCount = len(bots)

for i in range(m5Count):
    m5s[i].id = i+1

for bot in bots:
    for otherBot in bots:
        if otherBot is not bot:
            bot.partners.append(otherBot)

print(f"There are {botCount} bots on the field, with {m5Count} of them being M5s.")