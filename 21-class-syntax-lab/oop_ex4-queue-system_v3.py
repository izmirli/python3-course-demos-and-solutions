from collections import deque

debug = True


class Clerk:
    def __init__(self, clerk_name):
        self.name = clerk_name
        self._queue = deque()
        if debug: print(f'__init__ Clerk for {clerk_name}')

    def handle(self, cmd_atr):
        if 'wait' == cmd_atr['action']:
            self.wait(cmd_atr['customer'])
        elif 'next' == cmd_atr['action']:
            self.next()

    def wait(self, customer):
        self._queue.append(customer)

    def next(self):
        try:
            print(self._queue.popleft())
        except IndexError:
            print('There are no more customers to serve.')

    def has_customers_in_queue(self):
        return True if 1 <= len(self._queue) else False


class CommandTools:
    valid_actions = ('wait', 'next')
    customer_actions = ('wait')
    no_valid_command_msg = """
Please use one of these formats:
wait <clerk-name> <customer-name>
next <clerk-name>
"""

    @staticmethod
    def read_command():
        while True:
            cmd_input = input(': ')
            try:
                return CommandTools.parse_command(cmd_input)
            except UserWarning as e:
                print(f'No valid command was given: {e}', CommandTools.no_valid_command_msg)
                continue

    @staticmethod
    def parse_command(command):
        command_words = command.split(' ')
        if 2 > len(command_words) or 4 <= len(command_words):
            raise UserWarning(f'Wrong number of words ({len(command_words)}).')

        command_attribs = {}
        if command_words[0] not in CommandTools.valid_actions:
            raise UserWarning(f'Invalid command action ({command_words[0]}).')

        command_attribs['action'] = command_words[0]
        command_attribs['clerk'] = command_words[1]
        if command_attribs['action'] in CommandTools.customer_actions:
            if 3 > len(command_words):
                raise UserWarning(f"Missing mandatory customer on a {command_attribs['action']} action.")

            command_attribs['customer'] = command_words[2]

        return command_attribs


class Dispatcher:
    def __init__(self):
        self._clerks = {}

    def get_clerk(self, cmd_atr):
        clerk_on_call = cmd_atr['clerk']
        self.add_clerk_if_not_exist(clerk_on_call)

        if 'next' == cmd_atr['action']:
            clerk_on_call = self.get_clerk_with_customers(clerk_on_call)

        return self._clerks[clerk_on_call]

    def add_clerk_if_not_exist(self, name):
        if name not in self._clerks:
            clerk_obj = Clerk(name)
            self._clerks[name] = clerk_obj

    def get_clerk_with_customers(self, requested_clerk):
        if self._clerks[requested_clerk].has_customers_in_queue():
            return requested_clerk

        for c in self._clerks:
            if c != requested_clerk and self._clerks[c].has_customers_in_queue():
                return c

        return requested_clerk

    def print_queues(self):
        for c in self._clerks:
            print(f'{c}\t{self._clerks[c]._queue}')


dispatcher = Dispatcher()
while True:
    cmd = CommandTools.read_command()
    if debug: print(cmd)
    clerk = dispatcher.get_clerk(cmd)
    clerk.handle(cmd)

    if debug: dispatcher.print_queues()
