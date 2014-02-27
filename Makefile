init:
	sudo apt-get install apache2
	pip install -r requirements.txt
doc:
	cd ./docs; make html
