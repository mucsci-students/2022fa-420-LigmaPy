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
python interface.py
```

## CLI Commands

### `addClass` - <i>Creates a class</i>

```bash
>> addClass <name>
```

### `deleteClass` - <i>Removes a class</i>
```bash
>> deleteClass <name>
```

### `renameClass` - <i>Updates name of a class</i>
```bash
>> renameClass <currentName> <newName>
```

### `addAttribute` - <i>Creates an attribute in a class</i>
```bash
>> addAttribute <name> <class>
```

### `deleteAttribute` - <i>Removes an attribute from a class</i>
```bash
>> deleteAttribute <name> <class>
```

### `renameAttribute` - <i>Updates the name of a classes attribute</i>
```bash
>> renameAttribute <currentName> <newName> <class>
```

### `addRelationship` - <i>Creates a relationship between two classes</i>
```bash
>> addRelationship <source> <destination>
```

### `deleteRelationship` - <i>Removes a relationship between two classes</i>
```bash
>> deleteRelationship <source> <destination>
```

### `save` - <i>Saves the current state of the program</i>
```bash
>> save <filename>
```

### `load` - <i>Loads a previously saved state</i>
```bash
>> load <filename>
```

### `listClasses` - <i>Lists all classes and their contents</i>
```bash
>> listClasses
```

### `listClass` - <i>Lists the contents of a specified class</i>
```bash
>> listClass <name>
```

### `listRelationships` - <i>Lists all existing relationships between classes</i>
```bash
>> listRelationships
```

### `help` - <i>Lists all available commands and their descriptions</i>
```bash
>> help [command]
```

### `exit` - <i>Exits the program</i>
```bash
>> exit
```
<br>

## Team
[![Ammanuel Amare](https://avatars.githubusercontent.com/u/63563468?v=4)](https://github.com/manwellaa) | [![Aaron Heinbaugh](https://avatars.githubusercontent.com/u/98050840?v=4)](https://github.com/aaheinba) | [![Christian Shepperson](https://avatars.githubusercontent.com/u/8421245?v=4)](https://github.com/Sh3p) | [![Julia Geesaman](https://avatars.githubusercontent.com/u/111717589?v=4)](https://github.com/jgeesaman) | [![Samantha Noggle](https://avatars.githubusercontent.com/u/44234583?v=4)](https://github.com/astruxie) | [![Trevor Bender](https://avatars.githubusercontent.com/u/31744774?v=4)](https://github.com/Spyder-Monkey)
---|---|---|---|---|---
[Ammanuel Amare](https://github.com/manwellaa) | [Aaron Heinbaugh](https://github.com/aaheinba) | [Christian Shepperson](https://github.com/Sh3p) | [Julia Geesaman](https://github.com/jgeesaman) | [Samantha Noggle](https://github.com/astruxie) | [Trevor Bender](https://github.com/Spyder-Monkey)

<br><br><br>
<i>Dedicated to JSMACH <3</i>
