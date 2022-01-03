import os
import itertools
from utils import *
from config import *


def main():
    ##Generating
    dirs = os.listdir('.')

    all_files = set(dirs)

    work_dirs = all_files - exclude_files 

    layer_image = dict()

    all_list = []
    for dir in work_dirs:
        l = []
        files = os.listdir(dir)
        layer_image[dir] = files
        for file in files:
            l.append({dir:file})
        all_list.append(l)

    # iter_all = None
    results = list(itertools.product(*all_list))

    toprocess = []
    for result in results:
        d = {}
        s = ''
        single_process = []
        for e in result:
            d.update(e)

        for layer in layers_order:
            single_process.append(f"{layer}/{d[layer]}")
        toprocess.append(single_process)



    ##Processing
    ps = []
    j = 0
    k = 0
    iter = len(toprocess)
    print(f"To process {iter}\n\n")
    for img in toprocess:
        #print(img)
        img_2_save = []
        for l in img:
            img_2_save.append(cv2.imread(l, cv2.IMREAD_UNCHANGED))

        ps.append(Process(target=generate_image, args=(img_2_save,k,iter)))
        j = j + 1

        if j == batch:
            for p in ps:
                p.start()
            for p in ps:
                p.join()
            j = 0
            ps = []   
        
        k = k + 1

    if len(ps) != 0:
        for p in ps:
            p.start()
        for p in ps:
            p.join()

if __name__ == "__main__":
    main()