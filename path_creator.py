import os

f = open("wav.scp", "w")

initial_path="./data_dir/VoxCeleb1_test_wav/wav"

for folder in os.listdir(initial_path):
    for folder2 in os.listdir(initial_path+"/"+folder):
        
        for file in os.listdir(initial_path+"/"+folder+"/"+folder2):
            if file.endswith(".wav"):
                f.write( folder+"-"+folder2+"-"+file[0:4]+" "+initial_path+"/"+folder+"/"+folder2+"/"+file+"\n")