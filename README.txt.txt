This is a list of steps I took to set up and run the programs listed

DATABASE SETUP
> Install MySQL Workbench using the following link: https://dev.mysql.com/downloads/workbench/)
> Import the .sql files included in the SQL folder
> Run the 'Initializing Tables' first, then run the rest of the files to fill the table
> If foreign key errors are encountered,fill the table for which that foreign key is the primary key

GUI SETUP
> Install the latest version of python
> Install conda 
> Open up command line to start running the commands listed below
> Set up an environment using: conda create --name dbenv python = 3.10
> Create/allocate a folder to store the files in GUI files and unpack them there
> Navigate to that folder using cd command
> Run: conda activate dbenv
> Run 'pip install flask' and 'pip install mysql-connector-python' in cmd
> Run: python app.py
> A link should pop up in the console of app.py. Click that to access the GUI. By default that is usually http://127.0.0.1:5000/

Incase you want to run the jupyter notebooks in the 'Data Generation Files'
> Install jupyter notebook and the latest version of anaconda
> Inport the given .ipynb files using the upload feature
> Depending on the notebook, you may need to upload the datasets present in the 'Raw Data' folder
