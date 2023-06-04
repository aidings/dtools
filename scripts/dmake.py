import os
import shutil
import argparse
import yaml
from .dtools import find, data_root

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--conf', help='conf file', default='./conf.yaml', required=True)
    parser.add_argument('-t', '--target', help='target name', default='demo')
    parser.add_argument('-m', '--mode', choices=['main', 'lib', 'so', 'clean'], default='main')
    parser.add_argument('-n', '--nthread', default=-1, help='input compile number thread')
    args = parser.parse_args()
    if not os.path.exists(args.conf):
        shutil.copyfile(os.path.join(data_root, 'conf.yaml'), args.conf)
        print("1. you can edit the conf.yaml and run dmake xxx")
        print("2. you can run dmake -c path/to/conf.yaml xxx ")
    else:
        with open(args.conf, 'r') as f:
            conf = yaml.load(f, yaml.FullLoader)

        # get cpp's file paths
        cpp_files = find(conf['srcs_root'])

        # preprocess head paths
        head_paths = ['-I'+h for h in conf['incs_root']]

        # preprocess lib paths
        libs_paths = ['-L'+l for l in conf['libs_root']]

        # preprocess lib files
        libs = ['-l'+l for l in conf['libs']]

        mkfile = os.path.join(data_root, 'makefile')
        cmd = r'make -f {mkfile} SRCS_ROOT={srcs_root} INCS_ROOT={head_paths} LIBS_ROOT={libs_paths} LIBS={libs} TARGET={target} {args.mode} -j{args.nthread}'
        os.system(cmd)




    