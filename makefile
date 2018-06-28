.PHONY: update_code migrate_db clean restart fix_permission help

BRANCH := $(shell if [ "$(tag)" = "" ];then echo "feature/develop"; else echo "$(tag)" ;fi)
PROJECT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

update_code:
	git reset --hard
	find . -name "*.pyc" -exec rm -f {} \;
	git fetch origin
	git checkout $(BRANCH)
	git pull origin $(BRANCH)
	. $(PROJECT_DIR)/env/bin/activate && pip install -r requirements.txt

migrate_db:
	. $(PROJECT_DIR)/env/bin/activate && python manage.py migrate

clean:
	# clear cache period & can build frontend before update
	rm -rf /var/markone_server/staticfiles/*
	rm -rf $(PROJECT_DIR)/cms/markone_server-cms/*

stop_celery_work:
	$(PROJECT_DIR)/env/bin/supervisorctl -c $(PROJECT_DIR)/deploy/supervisor/supervisord.conf stop celery_worker

restart:
	$(PROJECT_DIR)/env/bin/supervisorctl -c $(PROJECT_DIR)/deploy/supervisor/supervisord.conf restart all

fix_permission:
	chown -R ubuntu:ubuntu $(PROJECT_DIR)
	chown -R ubuntu:ubuntu /var/markone_server/staticfiles
	chown -R ubuntu:ubuntu /var/markone_server-cms
	chown -R ubuntu:ubuntu /data/log/markone_server

pip_install:
	$(PROJECT_DIR)/env/bin/pip install -r $(PROJECT_DIR)/requirements.txt

help:
	@echo "make all tag=code tag"
	@echo "make [web, cms]"
	@echo "make restart need sudo permission"

all: update_code migrate_db clean restart

