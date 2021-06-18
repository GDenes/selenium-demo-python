# Selenium demo test project in python

## Start project
### Prerequisite
- Check python in your machine
or
- Install [python][python]

### Steps to setup project:
- Pull the project repo
- Open terminal in root
- Run command `python3 -m venv venv`
- Run command `pip install -r requirements.txt`

# Run tests

## Local run with pytest

- Test name pattern will be: `Test_<name-of-test>.py` or `test_<name-of-test>.py` 

### Simple run

- In project root directory run next command: `python -m pytest`

### Parallel run

- In project root directory run nex command: `pytest -n 3 --dist loadscope`
- Settings: 
  - `-n <number-of-thread>`
  - `--dist <distmode>`
    - set mode for distributing tests to exec environments. <br/>
      **each** - send each test to all available environments. <br/>
      **load** - load balance by sending any pending test to any available environment. <br/>
      **loadscope** - load balance by sending pending groups of tests in the same scope to any available environment. <br/>
      **loadfile** - load balance by sending test grouped by file to any available environment. <br/>
      (default) no - run tests inprocess, don't distribute.

## Remote run on standalone server

- Selenium standalone server download click [here][selenium-standalone].

&nbsp;
### Remote environment scripts

* Scripts are in `./scripts/grid` later referenced as `SCRIPTS_HOME_DIR`
  
&nbsp;
#### Start HUB - start hub with script command

* Open terminal in `SCRIPTS_HOME_DIR`
* Run `./start_hub.sh <options>`
    * options:
      
      Option prefix   | Option desc  | Example | Default value
      | :---:         | :---:        | :---:   | :---:
      -p              | Startup port | -p 8080 | 4444
      -f              | Executable `.jar` file | -f <path-to-file>/server.jar | search `.jar` file in the same dir


&nbsp;
#### Start NODE - connect to hub

* Open terminal in `SCRIPTS_HOME_DIR`
* Run `./start_node.sh <options>`
    * options:

      Option prefix     | Option desc                       | Example                                      | Default value
      | :---:           | :---:                             | :---:                                        | :---:
      -f                | Executable `.jar` file            | -f <path-to-file>/server.jar                 | search `.jar` file in the same dir
      --chromedriver    | path to Chrome web driver         | -p 8080                                      | search file based on `chrome*.*` in the same dir
      --edgedriver      | path to Edge(chromium) web driver | -f ./selenium-server-standalone-3.141.59     | search file based on `*edge*.*` in the same dir
      --geckodriver     | path to Firefox web driver        | --geckodriver <path-to-file>/geckodriver.exe | search file based on `gecko*.*` in the same dir
      --remoteip        | Ip of Hub                         | --remoteip http://127.0.0.1:4444             | http://127.0.0.1:4444


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
   [python]: <https://www.python.org/downloads/release/python-395/>
   [selenium-standalone]: <https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar>
