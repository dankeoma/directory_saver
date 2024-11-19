# Directory File Saver
This package lists and saves the files in the computer directory. The directory path is provided as a string in the request body bearing the name filePath: using Postman for example, the request body should have; "filePath":"documentpart"

e.g {

    "filePath":"D:/Desktop/Pictures"
} 

After running the package as a post request, the list of files consisting of the File id, filename, filesize, file type and date created, are displayed according to the number of files contained in the provided directory path. Secondly, an sqlite database named document.db is created in the package directory. The database can be acessed from the command window following the sqlite principles.
## Prerequisite for making use of the package
### Here are the list of the required files as provided
1. app.py
2. error.log
3. __init__.py
4. readme.md
5. requirements.txt
6. d_saver.py
1. .gitignore
### Setting up the system
1. Install Python - Make sure that latest version of python is installed in your system. You can click [Here](https://www.python.org/downloads/) to install python in your system.
1. Install SQLITE - Ensure that [SQLITE](https://www.mysql.com/downloads/ "Click to download MYSQL") is installed in the system. 

NOTE! Ensure that the insallation path of python and sqlite  are copied to the system's environmental variable. You can learn about that [here](https://www3.ntu.edu.sg/home/ehchua/programming/howto/Environment_Variables.html).

1. Create a folder in C drive , you can name it directory_saver or any other name. Paste the six required files provided.
1. Create a virtual environment for the project in the folder by typing the command below in the command window. make sure you vavigate to the folder before typing in the code:
    * C:\directory_saver> python -m venv venv
1. Activate the the virtual environment using the command:
    * C:\directory_saver> .venv\Scripts\Activate.

    * It wil now show: (venv)C:\directory_saver>
1. Create package directory - create another directory in the present directory and copy all the provided files into the directory
1. Install the required packages in the virtual environment container using the  command below: Note the packages are provided in the requirements.txt
    * C:\directory_saver>pip install -r requirements.txt
1. After the istallation you can type the command:

    * C:\directory_saver>pip freeze

        to see the installed packages.

After that, you are ready to use the API package in your system.
## Using The API Package
Open the command window and navigate to the directory where the Api package is copied to. Activate the virtual environment following the steps already describe above. Make sure the requirements.txt is installed as already described. type pip freeze to ensure the installation as shown below:
![Installed requirements.txt](images\pip_freeze.png)

After thatyou can type < python app.py> to run the API package as shown in the figure below;
![Running the app](images\apprun.png)
That starts the Api server on the local host 127.0.0.1:5000

### Testing with Postman
Open the Postman application and set to 127.0.0.1:5000 setting at GET. 127.0.0.1:5000/ and 127.0.0.1:5000/home will display the same as shown below: ![Postman display](relative%20images\post1.png)

A care look into the Postman displayed above, we discover that one of the request body params filePath is set to "D:/Desktop/Pictures" and that is what is required in running the url < 127.0.0.1:5000/view_directory_content>
which is the url required to display the files in the given folder.
The figures below shows the images after running the url as a POST request in preety and preview pane . ![Postman display](images\post2.png)![Postman display](images\post3.png)

A care look in the package directory will discover the creation of sqlite database "document.db" which contains the database created by the request made.
![Created database](images\post4.png)

 Everytime the request is made, the database is deleted and a fresh one created depending on the document path thats served in the request body. The database also contain a single table which bears the same same as the last name in the request parameter supplied. 

e.g <>"filePath": "D:/Pictures">

will create sqlite database document.db having a single table Pictures.

The next section lookes into accessing the database using sqlite commands in the command window.
### Accessing Database in command window
After ensuring correct installation and copying the sqlite path to the environment variables, call up the command window, navigate to the package folder and type sqlite3 to display the figure below with the cursor blinking ready to accept other sqlite commands: ![SQLITE command line](images\post5.png)
To access the databde document.db follow the sqlte commands as listed below:
* .open document.db - to open the database
* .tables - to display the tables in the database which in our example is < Pictures>
* .width - to use the entire width
* .mode markdown - to show the tables heasers
* select * from Pictures; to display the table 

The figure below shows the displayed figure after issuing the commands as stiuplated.
![SQLITE command line](.\images\post6.png)
## A look into the different files that comprises the API Package
