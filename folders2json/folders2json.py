from .functions import GetFullPathFiles, GetDevices, GenerateJson, prep

__version__ = "1.1.2"


def main():
    args = prep(__version__)  # get rootpath
    fullnamefiles = GetFullPathFiles(args.rootpath)  # get relative path files
    devices = GetDevices(fullnamefiles, args.rootpath)  # get devices for json
    GenerateJson(devices, args.windows, fullnamefiles)  # generate json file


if __name__ == "__main__":
    main()