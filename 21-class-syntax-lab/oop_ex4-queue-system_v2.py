from collections import deque

debug = False


class Clerk:
    def __init__(self, clerk_name):
        self.name = clerk_name
        self.queue = deque()
        if debug: print(f'__init__ Clerk for {clerk_name}')

    def wait(self, customer):
        self.queue.append(customer)

    def next(self):
        return self.queue.popleft()

    def has_customers_in_queue(self):
        return True if 1 <= len(self.queue) else False


class CommandTools:
    valid_actions = ('wait', 'next')
    customer_actions = ('wait')
    no_valid_command_msg = """
Please use one of these formats:
wait <clerk-name> <customer-name>
next <clerk-name>
"""

    @staticmethod
    def process_command(command):
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


clarks = {}

while True:
    this_command = input(': ')
    try:
        this_command_attributes = CommandTools.process_command(this_command)
    except UserWarning as e:
        print(f'No valid command was given: {e}', CommandTools.no_valid_command_msg)
        continue

    if this_command_attributes['clerk'] not in clarks:
        new_clerk = Clerk(this_command_attributes['clerk'])
        clarks[this_command_attributes['clerk']] = new_clerk

    if 'wait' == this_command_attributes['action']:
        clarks[this_command_attributes['clerk']].wait(this_command_attributes['customer'])
    elif 'next' == this_command_attributes['action']:
        next_customer = None
        if clarks[this_command_attributes['clerk']].has_customers_in_queue():
            next_customer = clarks[this_command_attributes['clerk']].next()
        else:
            for clark in clarks:
                if clark == this_command_attributes['clerk']:
                    continue
                if clarks[clark].has_customers_in_queue():
                    next_customer = clarks[clark].next()
        if next_customer is not None:
            print(next_customer)
        else:
            print('There are no more customers to serve.')

    if debug:
        for c in clarks:
            print(f'{c}\t{clarks[c].queue}')
