serve:
	http-server

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
