with open("file.txt", 'w') as f:
    f.write("Lakshmi Abhilash")
with open("file.txt", 'r+') as f:
    data=f.read()
    print("Previous:",data)
    new_data=data.replace("Lakshmi Abhilash","Gadde Lakshmi Abhilash")
    f.seek(0)
    f.write(new_data)
    f.truncate()
with open("file.txt", 'r') as f:
    print("Latest:",f.read())





