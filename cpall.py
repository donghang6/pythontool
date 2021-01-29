import os, sys

maxfileload = 1000000
blksize = 1024 * 500


def copyfile(pathfrom, pathto, maxfileload=maxfileload):
    if os.path.getsize(pathfrom) < maxfileload:
        with open(pathfrom, 'rb') as ffrom, open(pathto, 'wb') as fto:
            fto.write(ffrom.read())
    else:
        with open(pathfrom, 'rb') as ffrom, open(pathto, 'wb') as fto:
            while True:
                chunk = ffrom.read(blksize)
                if not chunk:
                    break
                fto.write(chunk)


def copytree(dirfrom, dirto):
    if not os.path.exists(dirto):
        os.mkdir(dirto)
    for filename in os.listdir(dirfrom):
        pathfrom = os.path.join(dirfrom, filename)
        pathto = os.path.join(dirto, filename)
        if os.path.isdir(pathfrom):
            os.mkdir(pathto)
            copytree(pathfrom, pathto)
        else:
            copyfile(pathfrom, pathto)


def getargs():
    pass


if __name__ == '__main__':
    copytree(r'C:\Users\hangdong\Desktop\ares', r'C:\Users\hangdong\Desktop\test-1')
