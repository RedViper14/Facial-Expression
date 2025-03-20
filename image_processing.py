import cv2
import os

os.chdir("facial_expressions")

#Anger Emotions

dataset_path=os.path.join("data_set","anger") #create a path for dataset

with open("anger.txt",'r') as f:
    img=[line.strip() for line in f]

for image in img:
    image_path=os.path.join("images",image)
    loaded_image=cv2.imread(image_path) #Read the data

    if loaded_image is not None:
        output_path=os.path.join(dataset_path,image) #create the path to store the extracted image
        cv2.imwrite(output_path,loaded_image) #Write the data
    else:
        print(f"coudn't read the file: {image}") 

print("Anger emotions Extracted Successfully")


#Happy Emotions

dataset_path=os.path.join("data_set","happy")

with open("happy.txt",'r') as f:
    img=[line.strip() for line in f]

for image in img:
    image_path=os.path.join("images",image)
    loaded_image=cv2.imread(image_path)

    if loaded_image is not None:
        output_path=os.path.join(dataset_path,image)
        cv2.imwrite(output_path,loaded_image)

print("Happy emotions Extracted Successfully")