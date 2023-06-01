the_file=None
the_tries=5
while the_tries>0:
    try:
       print("please enter the abslute path")
       print(f"you have {the_tries}")
       print("examble d\myfiles\filename.extension")
       thefilename=input("file path is >=").strip()
       the_file=open(thefilename,'r')
       print(the_file.read())
       break
    except:
        print("the file not found")
        the_tries-=1
    finally:
        if the_file is  not None:

           the_file.close()
           print("file is closed")
else:
    print("the tries is ended")
