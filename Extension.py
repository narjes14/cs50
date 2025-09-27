user_file =  input("File name :").strip().lower()

if user_file.endswith(".gif"):
    print("image/gif")

elif user_file.endswith(".jpeg")or user_file.endswith(".jpg"):
   print("image/jpen")

elif user_file.endswith(".txt"):
  print("text/plain")

elif user_file.endswith("zip"):
    print("application/pdf")

elif user_file.endswith("pdf"):
  print("application/ pdf")

elif user_file.endswith(".png"):
   print("image/png")

else:
   print("application/octed-stream")