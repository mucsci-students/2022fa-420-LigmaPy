# Ligma Py UML Editor

## Table of Contents
- [Setup](#setup)
- [How to Run](#how-to-run)
- [CLI Commands](#cli-commands)
- [Team](#team)

## Setup
1. Before running the program, you must have [Python](https://www.python.org/downloads/) installed (3.10.7 at the time).
2. Download the most recent version of the repository.
```bash
git clone https://github.com/mucsci-students/2022fa-420-LigmaPy.git
```
3. Once the repo is downloaded, install the required libraries with the below commands.
```bash
python3 -m pip install -r requirements.txt
```
## How to Run
1. Download the latest version from the [repo](https://github.com/mucsci-students/2022fa-420-LigmaPy).
2. Python 3.10 or higher is installed.
3. In a terminal, navigate to the `/2022fa-420-Ligmapy/` directory.
4. To run the UML editor type:
```bash
python uml.py [--cli]
```
Note: Add the --cli flag to run the CLI editor

<details>

<summary style="font-weight:bold;font-size:18.5pt;">CLI Commands</summary>

### `addClass` - <i>Creates a class</i>

```bash
addClass <name>
```

### `deleteClass` - <i>Removes a class</i>
```bash
deleteClass <name>
```

### `renameClass` - <i>Updates name of a class</i>
```bash
renameClass <currentName> <newName>
```

### `addField` - <i>Creates a field in a class</i>
```bash
addField <class> <name> <type>
```

### `deleteField` - <i>Removes a field from a class</i>
```bash
deleteField <class> <name>
```

### `renameField` - <i>Updates the name of a classes field</i>
```bash
renameField <class> <old_name> <new_name>
```

### `addMethod` - <i>Creates a method in a class</i>
```bash
addMethod <class> <name> <return_type> [-p <name>:<type>...]
```

### `deleteMethod` - <i>Removes a method from a class</i>
```bash
deleteMethod <class> <name>
```

### `renameMethod` - <i>Updates the name of a method in a class</i>
```bash
renameMethod <class> <old_name> <new_name>
```

### `addParam` - <i>Creates a list of parameters for a method in a class</i>
```bash
addParam <class> <method> <name>:<type>...
```

### `deleteParam` - <i>Removes the parameter(s) from a method in a class</i>
```bash
deleteParam <class> <method> [-a] [<name>...]
```

### `addRelationship` - <i>Creates a relationship between two classes</i>
```bash
addRelationship <source> <destination>
```

### `deleteRelationship` - <i>Removes a relationship between two classes</i>
```bash
deleteRelationship <source> <destination>
```

### `changeRelType` - <i>Updates the type of a relationship</i>
```bash
changeRelType <source> <destination> <new_type>
```

### `save` - <i>Saves the current state of the program</i>
```bash
save <filename>
```

### `load` - <i>Loads a previously saved state</i>
```bash
load <filename>
```

### `listClasses` - <i>Lists all classes and their contents</i>
```bash
listClasses
```

### `listClass` - <i>Lists the contents of a specified class</i>
```bash
listClass <name>
```

### `listRelationships` - <i>Lists all existing relationships between classes</i>
```bash
listRelationships
```

### `help` - <i>Lists all available commands and their descriptions</i>
```bash
help [command]
```

### `exit` - <i>Exits the program</i>
```bash
exit
```
</details>
<br>
<details>

<summary style="font-weight:bold;font-size:18.5pt;">Design Patterns</summary>

## MVC
## Memento
## Observer
## Singleton
</details>
<br>

## Team
[![Aaron Heinbaugh](https://avatars.githubusercontent.com/u/98050840?v=4)](https://github.com/aaheinba) | [![Christian Shepperson](https://avatars.githubusercontent.com/u/8421245?v=4)](https://github.com/Sh3p) | [![Julia Geesaman](https://avatars.githubusercontent.com/u/111717589?v=4)](https://github.com/jgeesaman) | [![Samantha Noggle](https://avatars.githubusercontent.com/u/44234583?v=4)](https://github.com/astruxie) | [![Trevor Bender](https://avatars.githubusercontent.com/u/31744774?v=4)](https://github.com/Spyder-Monkey)
---|---|---|---|---
[Aaron Heinbaugh](https://github.com/aaheinba) | [Christian Shepperson](https://github.com/Sh3p) | [Julia Geesaman](https://github.com/jgeesaman) | [Samantha Noggle](https://github.com/astruxie) | [Trevor Bender](https://github.com/Spyder-Monkey)

<br><br><br>
<i>Dedicated to JSMACH <3</i>
