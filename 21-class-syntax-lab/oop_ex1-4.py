# Ex1
print('\n ----- Ex1 -----')

class Summer:
    def __init__(self):
        self._total = 0

    def add(self, *numbers: int) -> None:
        self._total += sum(numbers)

    def print_total(self):
        print(self._total)

s = Summer()
t = Summer()
s.add(10, 20)
t.add(50)
s.add(30)
s.print_total()  # should print 60
t.print_total()  # should print 50


# Ex2
print('\n ----- Ex2 -----')

class MyCounter:
    count = 0

    def __init__(self):
        MyCounter.count += 1

for _ in range(10):
    c1 = MyCounter()

print(MyCounter.count)  # should print 10


# Ex3
print('\n ----- Ex3 -----')

class Widget:
    def __init__(self, name):
        self.name = name
        self._dependencies = []
        self.built = False

    def add_dependency(self, *dependencies):
        self._dependencies.extend(dependencies)

    def build(self):
        self.built = True
        for d in self._dependencies:
            if not d.built:
                d.build()
                print(d.name)


luke = Widget("Luke")
hansolo = Widget("Han Solo")
leia = Widget("Leia")
yoda = Widget("Yoda")
padme = Widget("Padme Amidala")
anakin = Widget("Anakin Skywalker")
obi = Widget("Obi-Wan")
darth = Widget("Darth Vader")
_all = Widget("All")

luke.add_dependency(hansolo, leia, yoda)
leia.add_dependency(padme, anakin)
obi.add_dependency(yoda)
darth.add_dependency(anakin)

_all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)
_all.build()
# code should print: Han Solo, Padme Amidala, Anakin Skywalker, Leia, Yoda, Luke, Obi-Wan, Darth Vader
# (can print with newlines in between modules)


# Ex4
print('\n ----- Ex4 -----')
from collections import deque

debug = False

class Queue:
    def __init__(self, clerk):
        self.id = clerk
        self.queue = deque()
        if debug: print(f'__init__ Queue for {clerk}')

    def queue_len(self):
        return len(self.queue)

    def add_to_queue(self, customer):
        self.queue.append(customer)

    def serve_next(self):
        return self.queue.popleft()


class QueueSystem:
    no_valid_command_msg = """No valid command was given.
Please use one of these formats:
wait <clerk-name> <customer-name>
next <clerk-name>
"""

    def __init__(self):
        self.clerks = {}
        if debug: print('__init__ QueueSystem')

    def accept_commands(self):
        while True:
            command = input(': ')
            try:
                (action, clerk_customer) = command.split(' ', 1)
            except ValueError:
                if 'exit' == command:
                    print('bye')
                    return None
                print(QueueSystem.no_valid_command_msg)
                continue
            if 'wait' == action:
                try:
                    (clerk, customer) = clerk_customer.split(' ', 1)
                except ValueError:
                    print(QueueSystem.no_valid_command_msg)
                    continue
                self.wait(clerk, customer)
            elif 'next' == action:
                self.next(clerk_customer)
            else:
                print(QueueSystem.no_valid_command_msg)

            if debug: self.show_queues()

    def wait(self, clerk, customer):
        if debug: print(f'customer: {customer} will wait in clerk {clerk} queue.')
        if clerk in self.clerks:
            self.clerks[clerk].add_to_queue(customer)
        else:
            new_clerk = Queue(clerk)
            new_clerk.add_to_queue(customer)
            self.clerks[clerk] = new_clerk

    def next(self, clerk):
        if clerk not in self.clerks:
            new_clerk = Queue(clerk)
            self.clerks[clerk] = new_clerk
        try:
            customer = self.clerks[clerk].serve_next()
        except IndexError:  # No customers in given clerk's queue
            clerks_queues_by_len = {self.clerks[c].queue_len(): c for c in self.clerks}  # OK to squash same size queues.
            busiest_queue_len = max(clerks_queues_by_len.keys())
            if 0 < busiest_queue_len:
                customer = self.clerks[clerks_queues_by_len[busiest_queue_len]].serve_next()
        try:
            print(customer)
        except UnboundLocalError:
            print('There are no more customers to serve.')

    def show_queues(self):
        for cur_clerk in self.clerks:
            print(cur_clerk, self.clerks[cur_clerk].queue)

qs = QueueSystem()
qs.accept_commands()
