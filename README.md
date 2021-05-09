# DD2424-Project - Dog Detection
**By Alice Palm, Emma Lind, and Johanna Peterson**

This **repository** contains the code and data for the project in the course DD2424 - Deep Learning in Data Science, at KTH Royal Institue of Technology, Spring 2021. The network developed was based on InceptionV3 as pre-trained model, and further trained on the *Tsinghua Dogs Dataset* which can be found at https://cg.cs.tsinghua.edu.cn/ThuDogs/.

**Files:**
./Dataset: contains files with low-annotations and train-and-val-list used for organizing the data into appropriate directories.
organize_data: contains code for splitting data into train-val-test sets. 
./data: 16 classes split into train-val-test sets used for developing model (the rest of the dataset was stored on Google Drive).
main.ipynb: main source code for the model. Developed using Google Colab. 
