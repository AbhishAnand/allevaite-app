To run the app in your system ,
1. Create a directory of your choice 
 eg . mkdir MyFlaskApp
2.Navigate to the diretory
  eg. cd MyFlaskApp
3. Place the flask_install.bat file inside the directory and run it . It will create a venv folder.
4.Place the project and static folder  and requiremnts.txt in the MyFlaskApp directory.
5. Run the following command to install dependencies 
pip install -r requirements.txt

6. Run the flask app by -
set FLASK_APP=project
flask run