PY?=python
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

FTP_HOST=localhost
FTP_USER=anonymous
FTP_TARGET_DIR=/

SSH_HOST=localhost
SSH_PORT=22
SSH_USER=root
SSH_TARGET_DIR=/var/www

S3_BUCKET=my_s3_bucket

CLOUDFILES_USERNAME=my_rackspace_username
CLOUDFILES_API_KEY=my_rackspace_api_key
CLOUDFILES_CONTAINER=my_cloudfiles_container

DROPBOX_DIR=~/Dropbox/Public/

GITHUB_REPO_SLUG=fkztw/blog.fkz.tw
GITHUB_REMOTE_NAME=origin
GITHUB_SOURCE_CODES_BRANCH=source
GITHUB_PAGES_BRANCH=master
GITHUB_COMMIT_MSG=$(shell git --no-pager log --format=%s -n 1 | sed 's/[\$"]/\\&/g')

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

# For quick create/edit
PAGESDIR=$(INPUTDIR)/pages
POSTSDIR=$(INPUTDIR)/posts
DRAFTSDIR=$(INPUTDIR)/drafts

DATE := $(shell date +'%Y-%m-%d %H:%M:%S')
SLUG := $(shell echo '${NAME}' | sed -e 's/[^[:alnum:]]/-/g' | tr -s '-' | tr A-Z a-z)
EXT ?= md
AUTHOR=fkz

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make publish                     generate using production settings '
	@echo '   make serve [PORT=8000]           serve site at http://localhost:8000'
	@echo '   make devserver [PORT=8000]       start/restart develop_server.sh    '
	@echo '   make stopserver                  stop local server                  '
	@echo '   make ssh_upload                  upload the web site via SSH        '
	@echo '   make rsync_upload                upload the web site via rsync+ssh  '
	@echo '   make dropbox_upload              upload the web site via Dropbox    '
	@echo '   make ftp_upload                  upload the web site via FTP        '
	@echo '   make s3_upload                   upload the web site via S3         '
	@echo '   make cf_upload                   upload the web site via Cloud Files'
	@echo '   make github                      upload the web site via gh-pages   '
	@echo '   make newdraft  NAME=             create a new draft under DRAFTSDIR '
	@echo '   make editdraft NAME=             edit a post under DRAFTSDIR         '
	@echo '   make editpost  NAME=             edit a post under POSTDIR          '
	@echo '   make newpage   NAME=             create a new post under PAGESDIR   '
	@echo '   make editpage  NAME=             edit a post under PAGESDIR         '
	@echo '                                                                       '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html'
	@echo '                                                                       '

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	cd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT)
else
	cd $(OUTPUTDIR) && $(PY) -m pelican.server
endif

devserver:
ifdef PORT
	$(BASEDIR)/develop_server.sh restart $(PORT)
else
	$(BASEDIR)/develop_server.sh restart
endif

stopserver:
	kill -9 `cat pelican.pid`
	kill -9 `cat srv.pid`
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

ssh_upload: publish
	scp -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

rsync_upload: publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzc --delete $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude

dropbox_upload: publish
	cp -r $(OUTPUTDIR)/* $(DROPBOX_DIR)

ftp_upload: publish
	lftp ftp://$(FTP_USER)@$(FTP_HOST) -e "mirror -R $(OUTPUTDIR) $(FTP_TARGET_DIR) ; quit"

s3_upload: publish
	s3cmd sync $(OUTPUTDIR)/ s3://$(S3_BUCKET) --acl-public --delete-removed --guess-mime-type

cf_upload: publish
	cd $(OUTPUTDIR) && swift -v -A https://auth.api.rackspacecloud.com/v1.0 -U $(CLOUDFILES_USERNAME) -K $(CLOUDFILES_API_KEY) upload -c $(CLOUDFILES_CONTAINER) .

github: publish
	git push $(GITHUB_REMOTE_NAME) $(GITHUB_SOURCE_CODES_BRANCH)

ci: publish
	git config --global user.name "fkztw - CI"
	git config --global user.email "gh@fkz.tw"
	ghp-import -n -m "$(GITHUB_COMMIT_MSG)" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push -f https://$(GITHUB_TOKEN)@github.com/$(GITHUB_REPO_SLUG).git $(GITHUB_PAGES_BRANCH):$(GITHUB_PAGES_BRANCH) > /dev/null

newdraft:
ifdef NAME
	echo "Title: $(NAME)  " > $(DRAFTSDIR)/$(SLUG).$(EXT)
	echo "Slug: $(SLUG)  " >> $(DRAFTSDIR)/$(SLUG).$(EXT)
	echo "Date: $(DATE)  " >> $(DRAFTSDIR)/$(SLUG).$(EXT)
	echo "Authors: $(AUTHOR)  " >> $(DRAFTSDIR)/$(SLUG).$(EXT)
	echo "Category:   "    >> $(DRAFTSDIR)/$(SLUG).$(EXT)
	echo "Tags:   "        >> $(DRAFTSDIR)/$(SLUG).$(EXT)
	echo "Summary:   "     >> $(DRAFTSDIR)/$(SLUG).$(EXT)
	echo ""     >> $(DRAFTSDIR)/$(SLUG).$(EXT)
	${EDITOR} ${DRAFTSDIR}/${SLUG}.${EXT}
else
	@echo 'Variable NAME is not defined.'
	@echo 'Do make newdraft NAME='"'"'Title of the article'"'"
endif

editdraft:
ifdef NAME
	echo "Modified: $(DATE)  " >> $(DRAFTSDIR)/$(SLUG).$(EXT)
	${EDITOR} ${DRAFTSDIR}/${SLUG}.${EXT}
else
	@echo 'Variable NAME is not defined.'
	@echo 'Do make editpost NAME='"'"'Title of the article'"'"
endif

editpost:
ifdef NAME
	echo "Modified: $(DATE)  " >> $(POSTSDIR)/$(SLUG).$(EXT)
	${EDITOR} ${POSTSDIR}/${SLUG}.${EXT}
else
	@echo 'Variable NAME is not defined.'
	@echo 'Do make editpost NAME='"'"'Title of the article'"'"
endif

newpage:
ifdef NAME
	echo "Title: $(NAME)  " > $(PAGESDIR)/$(SLUG).$(EXT)
	echo "Slug: $(SLUG)  " >> $(PAGESDIR)/$(SLUG).$(EXT)
	echo "Date: $(DATE)  " >> $(PAGESDIR)/$(SLUG).$(EXT)
	echo ""                >> $(PAGESDIR)/$(SLUG).$(EXT)
	${EDITOR} ${PAGESDIR}/${SLUG}.$(EXT)
else
	@echo 'Variable NAME is not defined.'
	@echo 'Do make newpage NAME='"'"'Page Name'"'"
endif

editpage:
ifdef NAME
	echo "Modified: $(DATE)  " >> $(PAGESDIR)/$(SLUG).$(EXT)
	${EDITOR} ${PAGESDIR}/${SLUG}.$(EXT)
else
	@echo 'Variable NAME is not defined.'
	@echo 'Do make editpage NAME='"'"'Page Name'"'"
endif

.PHONY: html help clean regenerate serve devserver publish ssh_upload rsync_upload dropbox_upload ftp_upload s3_upload cf_upload github newdraft editdraft editpost newpage editpage
