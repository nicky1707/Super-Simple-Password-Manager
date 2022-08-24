# Super-Simple-Password-Manager
Simple CLI Password Manager written in python.

## Compile this into a exe with pyinstaller
- 1.Create a virtural environment 
```python
pip install virtualenv

virtualenv env

env/scripts/activate
```

- 2. Install pyinstaller
```python
pip install pyinstaller
```

- (OPTIONAL) Add a icon 
- copy place your .ico format file in the directory

- 3. Run the command the the directory while virtual env activated
```python
pyinstaller -F -i icon.ico main.py
```
- this will compile the python script into binary file that is exe file.