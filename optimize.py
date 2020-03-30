import os
import shutil
import pathlib
from PIL import Image

# file extension inventory
staticDirs = [x[0] for x in os.walk("./static")]

types = dict()

for dir in staticDirs:
    files = os.listdir(dir)
    for filePath in files:
        # print(filePath)
        # lowercase all media file paths
        # targetPath = filePath.lower()
        # if not os.path.isdir(dir + "/" + filePath) and filePath != targetPath:
            # shutil.copyfile(dir + "/" + filePath, dir + "/" + targetPath)
            # os.remove(dir + "/" + filePath)           


        filetype = (pathlib.Path(filePath).suffix)
        if filetype in types:
            types[filetype] +=1
        else:
            types[filetype] = 1

print("staticFiles")
print(types)

imagesToDelete = []
# look at all images in markdown files

ConvertThumbnails = False
ConvertInline = True

articles = os.listdir("content/portfolio")
for a in articles :
    print(a)
    
for article in articles:
    print(article)
    originalFile = "content/portfolio/" + article
    newFileName = originalFile + "new"
    with open(originalFile, 'r',  encoding='utf-8') as content_file:
        with open(newFileName , 'w',  encoding='utf-8') as new_file:
            for line in content_file:

                if(ConvertThumbnails):
                    if "image:" in line:
                        imagePath = line.replace("\n","").split(": ")[-1]
                        absPath =  imagePath
                        if "static" not in absPath:
                            absPath = "static/" + absPath

                        absPath = absPath.replace("//","/")
                        size = os.path.getsize(absPath) / (1024 * 1024)
                        print("\t", size, absPath)

                        if "png" in absPath:
                            im1 = Image.open(absPath)
                            imagesToDelete.append(absPath)
                            absPath = absPath.replace( "png", "jpg")

                            background = Image.new("RGB", im1.size, (255, 255, 255))
                            background.paste(im1) # 3 is the alpha channel

                            background.save(absPath, 'JPEG', quality=80)

                        toReplace = absPath.replace("static/","").lower()
                        new_file.write(line.replace(imagePath, toReplace))
                    else:
                        new_file.write(line)

                if(ConvertInline):
                    if "png" in line :
                        if "![" in line or "{{<" in line:
                            line= line.replace("jpg", "png")

                new_file.write(line)

    os.replace( newFileName, originalFile)

for delete in imagesToDelete:
    print("deleting", delete)
    os.remove(delete)
                # if "![" in line:
                #     print("\t"+line)
                # if "<img" in line:
                #     print("\t"+line)