# Task Manager 1.0.0

A simple task manager with dependency resolution.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Task Manager.

```bash
cd TaskManager
pip install .
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
managet get task name
```

to run tests:
```bash
manager test
```

follow the instructions in the command line (terminal)

## Examples
Windows:
```bash
PS C:\Users\User\Documents\tasktest> manager manage
Successfully managed builds in build.yaml. Open output.txt to see the result.
PS C:\Users\User\Documents\tasktest> more output.txt
To do in pack_test :  enable_lime_leprechauns, train_blue_centaurs, read_lime_leprechauns, train_black_leprechauns, upgrade_white_witches, train_lime_leprechauns, update_blue_witches, upgrade_black_cyclops, create_grey_cyclops, design_blue_witches
To do in important_things :  train_orange_witches, build_blue_cyclops, design_blue_witches
To do in urgent_stuff :  upgrade_lime_witches, build_red_cyclops, upgrade_grey_witches
To do in important_game :  bring_grey_cyclops, bring_lime_centaurs, create_red_witches, train_blue_centaurs, upgrade_grey_leprechauns, train_orange_fairies, enable_orange_centaurs, design_grey_cyclops, train_purple_fairies
To do in important_stuff :  create_blue_cyclops, update_black_witches, build_grey_witches, read_lime_fairies
To do in urgent_stuff :  build_lime_cyclops, enable_orange_centaurs, create_grey_cyclops, upgrade_purple_leprechauns
Invalid build do_things: this build contains cycles
To do in cool_game :  enable_white_leprechauns, read_white_witches, design_lime_fairies, upgrade_orange_fairies, train_purple_fairies, upgrade_grey_fairies, train_purple_fairies, design_blue_witches
```
```bash
PS C:\Users\User\Documents\tasktest> manager get build important_things
Build info:
* name:  important_things
* tasks:  train_orange_witches, build_blue_cyclops, design_blue_witches
```

```bash
PS C:\Users\User\Documents\tasktest> manager test
Debug mode

Running tests
Enter seed (unsigned int): 13
C:\Users\User\Documents\tasktest
Build class: test passed
Graph class: test passed
Topological sort: test passed
Generating random input data...
Output written in test_output.txt
PS C:\Users\User\Documents\tasktest> more test_output.txt
To do in pack_test :  enable_lime_leprechauns, train_blue_centaurs, read_lime_leprechauns, train_black_leprechauns, upgrade_white_witches, train_lime_leprechauns, update_blue_witches, upgrade_black_cyclops, create_grey_cyclops, design_blue_witches
To do in important_things :  train_orange_witches, build_blue_cyclops, design_blue_witches
To do in urgent_stuff :  upgrade_lime_witches, build_red_cyclops, upgrade_grey_witches
To do in important_game :  bring_grey_cyclops, bring_lime_centaurs, create_red_witches, train_blue_centaurs, upgrade_grey_leprechauns, train_orange_fairies, enable_orange_centaurs, design_grey_cyclops, train_purple_fairies
To do in important_stuff :  create_blue_cyclops, update_black_witches, build_grey_witches, read_lime_fairies
To do in urgent_stuff :  build_lime_cyclops, enable_orange_centaurs, create_grey_cyclops, upgrade_purple_leprechauns
Invalid build do_things: this build contains cycles
To do in cool_game :  enable_white_leprechauns, read_white_witches, design_lime_fairies, upgrade_orange_fairies, train_purple_fairies, upgrade_grey_fairies, train_purple_fairies, design_blue_witches
```
