# Super-Simple-Password-Manager
Simple CLI Password Manager written in python stores passwords in sqlite3 database at appdata folder
it is not recommend to use it for daily purpose because password is not hashed into db this is for educational purpose.

## Compile this into a exe with pyinstaller
**1. Create a virtural environment and activate it**

To reduce the compiled file size while using a virtual environment only the libraries imported in the main.py will be included. 
```python
pip install virtualenv

virtualenv env

env/scripts/activate
```

**2. Install pyinstaller**
```python
pip install pyinstaller
```

- (OPTIONAL) Add a icon 
- copy place your .ico format file in the directory

**3. Run the command the the directory while virtual env activated**
```python
pyinstaller -F -i icon.ico main.py
```
- this will compile the python script into binary file that is exe file.

- compiled exe file will be found inside **dist** folder