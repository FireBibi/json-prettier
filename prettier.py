import json
import sys, argparse
import os.path

parser = argparse.ArgumentParser()
parser.add_argument('file', help='Choose an input file')
parser.add_argument("-o", "--ouput_file", dest="filename", required=False, help="Set an output file")
args = parser.parse_args()


def open_base_file(file):
    with open(file) as f:
        data = json.load(f)
        return json.dumps(data, indent=4, sort_keys=True)

def write_file(json_to_write, ouput_file):
    with open(ouput_file, "w") as f:
        data = json.loads(json_to_write)
        f.write(json.dumps(data, indent=4, sort_keys=True))
        print("JSON was successfully writen to file !")
        sys.exit()

def is_valid_file(file):
    if not os.path.exists(file):
        print("The file %s doesn't exist please provide a valid file !" % file)
        return False
    else:
        return True
                    


file = args.file

if not is_valid_file(file):
    sys.exit()

json_opened = open_base_file(file)

if args.filename is not None:
    to_write = args.filename
    write_file(json_opened, to_write)
else:
    print(json_opened)

