import os
SRC='/home/irae/plash/standalone-build/dist/starter/src/'
import pdb; pdb.set_trace()
filepath=sys.argv[0]
global_namespace = {
    "__file__": filepath,
    "__name__": "__main__",
}
assert not '/' in filepath
with open(os.path.join(SRC, 'bin', filepath), 'rb') as file:
    exec(compile(file.read(), filepath, 'exec'), globals())
