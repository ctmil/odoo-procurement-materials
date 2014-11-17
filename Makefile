PROYECT=procurement_materials
DESIGNDIR=design
WORKDIR=${DESIGNDIR}/tmp
ZARGO=${DESIGNDIR}/${PROYECT}.zargo
XMI=${WORKDIR}/${PROYECT}.xmi
DB=${WORKDIR}/${PROYECT}.db

all: rebase-addons

notify:
	while inotifywait -e close_write ${ZARGO}; do make addons; done

${XMI}: ${ZARGO}
	unzip -o -d ${WORKDIR} ${ZARGO}
	touch ${XMI}


prepare-addons:
	-git branch argouml
	-git branch ${USER}_dev
	git diff argouml master > argouml-master.diff
	git diff argouml ${USER}_dev > argouml-${USER}_dev.diff
	git checkout argouml
	git checkout ${USER}_dev Makefile ${ZARGO}
	git add Makefile ${ZARGO}
	git commit -m '[XMI2ODOO] Update Makefile ${ZARGO}'
	git log --source -1 | grep HEAD | awk '{ printf $$2 }' > .last.commit

addons: ${DB}
	xmi2odoo -r --dbfile $< --logfile $?.log --loglevel=2 --target $@

commit-addons: prepare-addons addons
	-git commit -am "[ARGOUML] $$(date)"

rebase-addons: commit-addons
	git checkout ${USER}_dev
	git rebase argouml

revert:
	git checkout argouml
	git reset --hard $$(cat .last.commit) 
	git checkout ${USER}_dev

${DB}: ${XMI}
	xmi2odoo --infile $< --dbfile $@ ${XMI2OERP_OPT}

clean:
	rm -rf ${WORKDIR}

.PHONY: notify addons commit-addons prepare-addons

.SUFFIXES:

