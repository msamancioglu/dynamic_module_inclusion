## Smart File Inclusion Using importlib module - Alternative Way

importlib python module  can be  used for importin python module/package at runtime dynamically

Visit [importlib](https://docs.python.org/3/library/importlib.html#importlib.import_module) for details

Modules goingto be imported at runtime should be placed under /files folder. Currentlye there are two files 

To run app with loading and running selected modules/functions at runtime:

```sh
python main.py file1
```

You should see /files/file1.py included and run dynamically

```sh
running magic file 1 
file1
0:00:00.001981
```
