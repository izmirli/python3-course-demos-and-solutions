import sys


def get_hosts():
    """
    Parsing a file by the name 'hosts' for servers name and IP address.
    :return: A dict with servers names as keys and their IP addresses as values.
    """
    hosts = {}
    try:
        with open('hosts', 'r', encoding='UTF-8') as f:
            for line in f:
                (server_name, server_address) = line.split('=', 1)
                hosts[server_name] = server_address.rstrip()
    except FileNotFoundError as e:
        print(f'Failed to read hosts file - {e}\nAborting.')
        exit(1)
    return hosts


hosts_dict = get_hosts()
# print(hosts_dict)
for i in range(1, len(sys.argv)):
    server = sys.argv[i]
    print(f'{server + " IP address:":20}', end=' ')
    try:
        print(hosts_dict[server])
    except KeyError:
        print('not in hosts list.')
