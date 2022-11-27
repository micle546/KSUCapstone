# KSUCapstone

Kent State Capstone Repo
https://dev.kentcapstone.ai-home.co/

# Setting up Local Database
1. download this: https://www.mongodb.com/try/download/community
2. install (clickthrough, no setting changes) (complete, and as a service)
3. type: services.msc into your start menu, seach for mongoDB and verify it is running (you can stop and disable it when you're not local debugging, just make sure to start it back up when coding)

![image](https://user-images.githubusercontent.com/1088521/203186558-0c67160b-86ec-4621-b794-ddafd4c867a4.png)


# Setting up Visual Studio
- Open Visual Studio
- Select clone a repo
- Enter repo URL
- Change path if desired
![image](https://user-images.githubusercontent.com/1088521/190232582-a427b950-1a56-4c8d-b050-ba4aa2a1c6b7.png)
- Close visual studio
- Open the location you copied the github repo to, should look something like this
![image](https://user-images.githubusercontent.com/1088521/190249704-c41c2cec-136b-41ed-8231-d341af981683.png)
- Double click on the .sln file to open it
- If it mentions something about the project being unloaded, right click and reload the solution.
- In the bottom right, click on 'main' and change it to 'origin/dev' (all uploads to github should be under dev)
![image](https://user-images.githubusercontent.com/1088521/190249557-cc4dd7fd-fd83-4f02-a08f-ccba1a36fe6a.png)
- Right click on the Python Environments in the Solution explorer, click add environment
![image](https://user-images.githubusercontent.com/1088521/190248653-670955aa-1ff8-4fdc-a701-ed72c26d38a1.png)
set to python 3.10, and click OK
![image](https://user-images.githubusercontent.com/1088521/190248950-8f626583-852f-49a4-9715-ed323228db95.png)
Now, if you click the start button, it should launch a live local version of the website that will change as you edit it. 

