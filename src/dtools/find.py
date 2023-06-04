import os
import glob
 
def find(src, ext='.cpp'):
    def __find(src, ext):
        files = []
        if os.path.isdir(src):
            root = os.path.join(src, '/**/*'+ext)
            files = list(glob.glob(root, recursive=True))
        return files

    files = []
    if isinstance(src, str):
        files = __find(src, ext)
    elif isinstance(src, (list, tuple)):
        for s in src:
            if os.path.exists(s):
                files += __find(s, ext)
    return files