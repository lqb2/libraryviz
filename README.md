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

# update the html page scraping my latest goodreads library update
make update

# commit the master branch
git commit -am "updated"

# update the master branch on github
git push origin HEAD

# update the gh-pages branch on github
make publish
```

## Notes

* [ideal bookshelf](https://www.idealbookshelf.com/)
