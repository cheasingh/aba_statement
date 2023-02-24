### installation

make sure you have at least python 3.6 installed and install the below requirements

```
pip install -r requirements.txt
```

### usage

```python
python3 convert_xlsx.py aba_statement.xlsx
```

- add `--saveto` to specified the location to save the converted file
- add `--app` to specified what format you want to convert aba statement to.

**noted**: the default app is [**homebank**](http://homebank.free.fr/en/) and converted statement will be saved to the application root installation folder as default.

Example:

```python
python3 convert_xlsx.py aba_statement.xlsx --app homebank --saveto "c:\users\void\desktop"
```

#### batch script shortcut for windows

if you are using windows, you can configured the application to run anywhere from command (cmd) or (terminal) by creating a batch command and directory that storing it to the system environment.

add system environment: [learn.microsoft.com](<https://learn.microsoft.com/en-us/previous-versions/office/developer/sharepoint-2010/ee537574(v=office.14)>)

example of batch code that point to python file

```batch
@echo off
@C:\tools\aba_statement\venv\Scripts\python.exe C:\tools\aba_statement\convert_xlsx.py %*
@pause
```

### contribution

feel free to add more app in.
