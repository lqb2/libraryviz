install:
	pip install -r requirements.txt


serve:
	http-server
	open http://0.0.0.0:8080


update:
	python update.py


publish: 
	# switch to the gh-pages branch
	git checkout gh-pages
	# merge in new changes from master
	git merge master
	# push new changes to github (publish)
	git push origin gh-pages
	# switch back to master
	git checkout master

open:
	open https://lqb2.github.io/libraryviz/

virtch: 
	source bin/activate

# How to refresh the list of books: 5 steps

# 1. activate the virtual environment
# source bin/activate

# 2. update the html page scraping my latest goodreads library update
# make update

# 3. commit the master branch
# git commit -am "updated"

# 4. update the master branch on github
# git push origin HEAD

# 5. update the gh-pages branch on github
# make publish