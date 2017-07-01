# libraryviz


## dependencies

- `requests` (for making HTTP requests)
- `beautifulsoup4` (for parsing and extracting data out of HTML)
- `jinja2` (for writing HTML with a template)

## Initial setup 

Install python 3.5 or later

```sh
brew install python3
```

Create and activate the virtual environment

```sh
python3 -m venv .
source bin/activate
```

Install Python dependencies

```
make install
```

## Usage

default working branch is `master`


### How to refresh the list of books

```sh
# activate the virtual environment
source bin/activate
make update
git commit -am "updated"
make publish
```