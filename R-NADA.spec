#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-NADA
Version  : 1.6.1.1
Release  : 47
URL      : https://cran.r-project.org/src/contrib/NADA_1.6-1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/NADA_1.6-1.1.tar.gz
Summary  : Nondetects and Data Analysis for Environmental Data
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n NADA
cd %{_builddir}/NADA

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641065643

%install
export SOURCE_DATE_EPOCH=1641065643
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library NADA
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library NADA
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library NADA
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc NADA || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/NADA/DESCRIPTION
/usr/lib64/R/library/NADA/INDEX
/usr/lib64/R/library/NADA/Meta/Rd.rds
/usr/lib64/R/library/NADA/Meta/data.rds
/usr/lib64/R/library/NADA/Meta/features.rds
/usr/lib64/R/library/NADA/Meta/hsearch.rds
/usr/lib64/R/library/NADA/Meta/links.rds
/usr/lib64/R/library/NADA/Meta/nsInfo.rds
/usr/lib64/R/library/NADA/Meta/package.rds
/usr/lib64/R/library/NADA/NAMESPACE
/usr/lib64/R/library/NADA/R/NADA
/usr/lib64/R/library/NADA/R/NADA.rdb
/usr/lib64/R/library/NADA/R/NADA.rdx
/usr/lib64/R/library/NADA/data/Ag.rda
/usr/lib64/R/library/NADA/data/Arsenic.rda
/usr/lib64/R/library/NADA/data/AsExample.rda
/usr/lib64/R/library/NADA/data/Atra.rda
/usr/lib64/R/library/NADA/data/AtraAlt.rda
/usr/lib64/R/library/NADA/data/Atrazine.rda
/usr/lib64/R/library/NADA/data/Bloodlead.rda
/usr/lib64/R/library/NADA/data/Cadmium.rda
/usr/lib64/R/library/NADA/data/ChlfmCA.rda
/usr/lib64/R/library/NADA/data/CuZn.rda
/usr/lib64/R/library/NADA/data/CuZnAlt.rda
/usr/lib64/R/library/NADA/data/DFe.rda
/usr/lib64/R/library/NADA/data/DOC.rda
/usr/lib64/R/library/NADA/data/Golden.rda
/usr/lib64/R/library/NADA/data/Hatchery.rda
/usr/lib64/R/library/NADA/data/HgFish.rda
/usr/lib64/R/library/NADA/data/MDCu.rda
/usr/lib64/R/library/NADA/data/NADA.As.rda
/usr/lib64/R/library/NADA/data/Oahu.rda
/usr/lib64/R/library/NADA/data/Recon.rda
/usr/lib64/R/library/NADA/data/Roach.rda
/usr/lib64/R/library/NADA/data/SedPb.rda
/usr/lib64/R/library/NADA/data/ShePyrene.rda
/usr/lib64/R/library/NADA/data/Silver.rda
/usr/lib64/R/library/NADA/data/TCE.rda
/usr/lib64/R/library/NADA/data/TCEReg.rda
/usr/lib64/R/library/NADA/data/Tbl1one.rda
/usr/lib64/R/library/NADA/data/Thames.rda
/usr/lib64/R/library/NADA/help/AnIndex
/usr/lib64/R/library/NADA/help/NADA.rdb
/usr/lib64/R/library/NADA/help/NADA.rdx
/usr/lib64/R/library/NADA/help/aliases.rds
/usr/lib64/R/library/NADA/help/paths.rds
/usr/lib64/R/library/NADA/html/00Index.html
/usr/lib64/R/library/NADA/html/R.css
