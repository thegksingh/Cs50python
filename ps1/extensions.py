fileextension =input("File name: ").strip().lower()
if fileextension.endswith(".gif"):
    print("image/gif")
elif fileextension.endswith(".jpg"):
    print("image/jpg")
elif fileextension.endswith(".jpeg"):
    print("image/jpeg")
elif fileextension.endswith(".png"):
    print("image/png")
elif fileextension.endswith(".pdf"):
    print("image/pdf")
elif fileextension.endswith(".txt"):
    print("image/txt")
elif fileextension.endswith(".zip"):
    print("image/zip")
else:
    print("application/octet-stream")


