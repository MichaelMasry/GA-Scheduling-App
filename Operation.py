class Operation:

    def __init__(self, name, machine, duration, job_id):
        self.name = name
        self.machine = machine
        self.duration = duration
        self.dependencies = []
        self.start_time = 0
        self.job_id = job_id

    def __str__(self):

        return ("  Stage: " + str(self.machine) + "\t Start time: " + str(
                    format(round(self.start_time, 2))) + "\t  Duration: " + str(format(round(self.duration, 2))))

    def print_dependencies(self):
        if len(self.dependencies) > 0:
            print(str(self) + " depends on ")
            for operation in self.dependencies:
                print(str(operation))
