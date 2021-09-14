import glob, os, shutil

source_dir = 'C:/Users/xande/Documents' #Path where your files are at the moment
dst = 'C:/Users/xande/Documents/New folder' #Path you want to move your files to
files = glob.iglob(os.path.join(source_dir, "*.exe"))
print('path located')
for i in files:
    if os.path.isfile(i):
        print(i)
        shutil.copy2(i, dst)
        shutil.rmtree(i)
        os.remove(i)





