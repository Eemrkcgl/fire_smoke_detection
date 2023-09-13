"""
This code used for adjust diffrent labels into same shape
"""
import os

path_of_dir = ["data3/test/labels","data3/train/labels","data3/valid/labels"]

counter = 1
for paths in path_of_dir:
    labels = os.listdir(paths)
    for each in labels:
        final = "1"

        file = open(paths + "/" + each,"r+")
        text = file.read()
        file.close()
        
        

        conv_list=text.split()
        conv_list[0]="1"
        final=" ".join(conv_list)
        print(final)
        
        with open(paths + "/" + each,"w") as file:
            file.write(final)
        
        print(f"Counter :{counter}")
        counter += 1
