import os
import os.path
print(os.getcwd())
with open("data.txt","w") as res:
    for cur_dir, dirs, files in os.walk("./main"):
        for j in files:
            if (".py" in j):
                txt = str(cur_dir)
                txt += "\n"
                txt = txt[2:]
                res.write(txt)
                break
        print(cur_dir,dirs, files)