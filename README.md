## Smart File Inclusion Using importlib module

importlib python module  can be  used for importing python module/package at runtime dynamically

Please visit [importlib](https://docs.python.org/3/library/importlib.html#importlib.import_module) for details

Modules going to be imported at runtime should be placed under /magic_files folder. Currentlye there are two files 

To run applıcation and load and execute selected module at runtime:

```sh
python main.py file1
```

You should see /files/file1.py included and run dynamically

```sh
running magic file 1 
file1
0:00:00.001981
```
