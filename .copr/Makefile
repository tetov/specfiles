# from https://quentin.dufour.io/blog/2018-05-20/build-a-rpm-package-and-publish-it-on-copr/
rpmbuild_src = $(shell rpmbuild --eval '%{_sourcedir}')
.PHONY: prepare srpm rpm

prepare:
	dnf -y install rpmdevtools rpm-build
	cp $(spec)/*.patch $(rpmbuild_src)
	spectool -g -R $(spec)/*.spec

srpm: prepare
	rpmbuild -bs --define "_srcrpmdir $(outdir)" "$(spec)/*.spec"

rpm: prepare
	rpmbuild -bb --define "_rpmdir $(outdir)" "$(spec)/*.spec"
