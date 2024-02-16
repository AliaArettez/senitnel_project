# Description
This is simple Python code for importing files of logs in JSON format to Azure Sentinel. It is a slightly modified script of one that is publicly available, however, it allows uploading logs without the need to edit the code. Everything is entered via the command line. The code was tested in Windows 10 enviroment as are the instructions. 
# Dependencies
You will need to install: 
- Python3 avaliable from: https://www.python.org/downloads/
 
- Python requests package

  While most of the used package is already installed within Python, this package needs to be installed separately. You can use:
  
```pip install requests ```

# Launching
From command line go to the forlder or launch comand line there, otherwise you would need a path to start the code. 
The starting file is "Import.py"

All you need to do is type this command into command line: 

```python Import.py```

# Inputs

The code will promt you to enter four parameters:

- ID of Sentinel workspace
- Shared key for authorization
- Name of the table you want to insert into. (If the table does not exist it will create it)
- Name of JSON file with logs in JSON format (If the file is not in the same folder you will need to enter full path to the file)
