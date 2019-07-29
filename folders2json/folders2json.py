from .functions import GetFullPathFiles, GetDevices, GenerateJson, prep


__version__ = "1.0.6"


def main():
    args = prep()  # get rootpath
    fullnamefiles = GetFullPathFiles(args.rootpath)  # get relative path files
    devices = GetDevices(fullnamefiles, args.rootpath)  # get devices for json
    GenerateJson(devices, args.windows, fullnamefiles)  # generate json file for each


if __name__ == "__main__":
    main()
