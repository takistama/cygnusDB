# CygnusDB

CygnusDB is a lightweight python database that uses no external libraries.

  - Uses JSON for data storage with the .db file extension.
  - Uses OS for file path.
  - Basic functionality: `set`, `get`, `delete`, and `reset`

## Why use CygnusDB?

  - It's simple. It takes very few lines of code to modify a database file, and it works for basic applications where MongoDB or SQLITE are overkill.
  - It's easy to get started with. All you do is import `cygnusdb`, set the file path to your `.db` file, and write whatever code you need to utilize the database.

### Installation

Woohoo! CygnusDB is now on PyPi: https://pypi.org/project/cygnusdb/
Just install it with `pip install cygnusdb`

### Usage

In order to use CygnusDB, you need to install it like is outlined above. After installation, you simply need to import it:

```py
from cygnusdb import CygnusDB
```

Then, define the file path of your `.db` file:

```py
db = CygnusDB("./user.db")
```

Once that is done, you can modify database data with simple code:

```py
db.set("name" , "Xhsted")
```

And retrieve the data:

```py
db.get("name")
```

Since it uses JSON, the data is very versatile, and you can save data under any name you may want, such as a name, email, or even a personal bio.