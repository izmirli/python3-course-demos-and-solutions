import glob
import os.path
from collections import Counter, defaultdict

all_files_with_extensions = glob.glob('*.*')
print(f'{"all_files:":15}', all_files_with_extensions)

files_by_ext = {}
for cur_file in all_files_with_extensions:
    base, ext = os.path.splitext(cur_file)
    if ext not in files_by_ext:
        files_by_ext[ext] = []
    files_by_ext[ext].append(base)
print(f'{"files_by_ext:":15}', files_by_ext)

ext_length = {
    key: len(val) for key, val in files_by_ext.items()  # if key != ''
}
print(f'{"my ext_length:":15}', ext_length)

py_counter = Counter()
py_counter.update([os.path.splitext(file_name)[1] for file_name in all_files_with_extensions])

yanon_counter = {}
py_defaultdict = defaultdict(int)
for filename in all_files_with_extensions:
    _, ext = os.path.splitext(filename)
    py_defaultdict[ext] += 1
    try:
        yanon_counter[ext] += 1
    except KeyError:
        yanon_counter[ext] = 1

print(f'{"yanon_counter:":15}', yanon_counter)
print(f'{"py_counter:":15}', dict(py_counter))
print(f'{"py_defaultdict:":15}', dict(py_defaultdict))
