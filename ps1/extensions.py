fileextension =input("File name: ")
if fileextension.endswith(".gif"):
    print("Image/.gif")
elif fileextension.endswith(".jpg"):
    print("Image/.jpg")
elif fileextension.endswith(".jpeg"):
    print("Image/.jpeg")
elif fileextension.endswith(".png"):
    print("Image/.png")
elif fileextension.endswith(".pdf"):
    print("Image/.pdf")
elif fileextension.endswith(".txt"):
    print("Image/.txt")
elif fileextension.endswith(".zip"):
    print("Image/.zip")
else:
    print("application/octet-stream")


