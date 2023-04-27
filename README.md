# Task Manager 1.0.0

A simple task manager with dependency resolution. 

Tested on Windows 11 and Ubuntu 22.04.2 LTS

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) inside the Task_Manager directory to install Task Manager.

```bash
pip install .
```
## Input

builds.yaml tasks.yaml

```bash
builds.yaml syntax:
    builds:
    - name: [name]
      tasks:
      - [name]
      - [name]
      - [name]
      
tasks.yaml syntax:
    tasks:
    - name: [name]
      dependencies:
      - [name]
      - [name]
      - [name]
    
```

## Usage
open your command line (terminal) in a directory containing builds.yaml and tasks.yaml to use the utility

run one of the following commands

to get help:
```bash
manager [-h] 
```

to get an output.txt file with the proper order of tasks in every build:
```bash
manager manage
```

to print all the current builds (tasks):
```bash
manager list builds
manager list tasks
```

to print a build (task) with the name [name]:
```bash
manager get build name 
manager get task name
```

to run tests:
```bash
manager test
```

follow the instructions in the command line (terminal)

## Exceptions
```bash
return code 1: no input files found
return code 2: empty or incorrect input files
return code 3: trying to get a build(task) that does not exist
return code 4: failed to create graph
return code 5: failed to create output.txt
return code 6: failed to build test
```

## Examples
```bash
PS C:\Users\User\Documents\tasktest> manager manage
Successfully managed builds in build.yaml. Open output.txt to see the result.
PS C:\Users\User\Documents\tasktest> more output.txt
To do in pack_test :
  enable_lime_leprechauns
  train_blue_centaurs
  read_lime_leprechauns
  train_black_leprechauns
  upgrade_white_witches
  train_lime_leprechauns
  update_blue_witches
  upgrade_black_cyclops
  create_grey_cyclops
  design_blue_witches

...
```
```bash
PS C:\Users\User\Documents\tasktest> manager get build important_things
Build info:
* name:  important_things
* tasks:  
  train_orange_witches
  build_blue_cyclops
  design_blue_witches
```

```bash
PS C:\Users\User\Documents\tasktest> manager get build pack_tests
There is no build named pack_tests
```

```bash
PS C:\Users\User\Documents\tasktest> manager get build pack_tests
There is no build named pack_tests
```
