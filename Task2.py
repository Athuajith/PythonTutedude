def edit_file(filename):
   try:
      msg = input("Enter text to write to the file:")

      file=open(filename,'w')
      file.write(msg)
      print(f"Data successfully written to {filename}")
      file.close()

      addmsg=input("Enter additional text to append:")
      file=open(filename,'a')
      file.write("\n")
      file.write(addmsg)
      file.close()

      print(f"File content of output text file is")
      file=open(filename,'r')
      fileMsg=file.read()
      print(fileMsg)
      file.close()

   except FileNotFoundError:
       print(f"Error: Could not find or open the file '{filename}'.")

   except Exception as e:
       print(f"An unexpected error occurred: {e}")

edit_file("sample.txt")
