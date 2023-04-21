#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kdeedu-data
Version  : 23.04.0
Release  : 48
URL      : https://download.kde.org/stable/release-service/23.04.0/src/kdeedu-data-23.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.0/src/kdeedu-data-23.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.0/src/kdeedu-data-23.04.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: kdeedu-data-data = %{version}-%{release}
Requires: kdeedu-data-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
********  At the attention of packagers  *********
KHangMan, Kanagram, Parley and KWordQuiz depend on /kdeedu/data/kvtml!

%package data
Summary: data components for the kdeedu-data package.
Group: Data

%description data
data components for the kdeedu-data package.


%package license
Summary: license components for the kdeedu-data package.
Group: Default

%description license
license components for the kdeedu-data package.


%prep
%setup -q -n kdeedu-data-23.04.0
cd %{_builddir}/kdeedu-data-23.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1682093100
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1682093100
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdeedu-data
cp %{_builddir}/kdeedu-data-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kdeedu-data/4cc77b90af91e615a64ae04893fdffa7939db84c || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/apps/kvtml/bg/animals.kvtml
/usr/share/apps/kvtml/bg/easy.kvtml
/usr/share/apps/kvtml/bg/hard.kvtml
/usr/share/apps/kvtml/bg/medium.kvtml
/usr/share/apps/kvtml/ca/animals_pri.kvtml
/usr/share/apps/kvtml/ca/biografies_sec.kvtml
/usr/share/apps/kvtml/ca/capitalsdelmón_sec.kvtml
/usr/share/apps/kvtml/ca/comarques_sec.kvtml
/usr/share/apps/kvtml/ca/divises_sec.kvtml
/usr/share/apps/kvtml/ca/espai_pri.kvtml
/usr/share/apps/kvtml/ca/esports_sec.kvtml
/usr/share/apps/kvtml/ca/fruites_pri.kvtml
/usr/share/apps/kvtml/ca/invents_sec.kvtml
/usr/share/apps/kvtml/ca/objectes_pri.kvtml
/usr/share/apps/kvtml/ca/ordinadors_pri.kvtml
/usr/share/apps/kvtml/ca/professions_pri.kvtml
/usr/share/apps/kvtml/ca/províncies_sec.kvtml
/usr/share/apps/kvtml/ca/roba_pri.kvtml
/usr/share/apps/kvtml/ca/transports_pri.kvtml
/usr/share/apps/kvtml/ca/verdures_pri.kvtml
/usr/share/apps/kvtml/ca/vestit_pri.kvtml
/usr/share/apps/kvtml/cs/animals.kvtml
/usr/share/apps/kvtml/cs/easy.kvtml
/usr/share/apps/kvtml/cs/hard.kvtml
/usr/share/apps/kvtml/cs/medium.kvtml
/usr/share/apps/kvtml/da/beklaedning.kvtml
/usr/share/apps/kvtml/da/computere.kvtml
/usr/share/apps/kvtml/da/da_sports.kvtml
/usr/share/apps/kvtml/da/dyr.kvtml
/usr/share/apps/kvtml/da/easy.kvtml
/usr/share/apps/kvtml/da/frugter.kvtml
/usr/share/apps/kvtml/da/grontsager.kvtml
/usr/share/apps/kvtml/da/hard.kvtml
/usr/share/apps/kvtml/da/medium.kvtml
/usr/share/apps/kvtml/da/numre.kvtml
/usr/share/apps/kvtml/da/objekter.kvtml
/usr/share/apps/kvtml/da/opfindelser.kvtml
/usr/share/apps/kvtml/da/personer.kvtml
/usr/share/apps/kvtml/da/professioner.kvtml
/usr/share/apps/kvtml/da/rummet.kvtml
/usr/share/apps/kvtml/da/transport.kvtml
/usr/share/apps/kvtml/da/valutaer.kvtml
/usr/share/apps/kvtml/da/verdenshovedstaeder.kvtml
/usr/share/apps/kvtml/de/animals.kvtml
/usr/share/apps/kvtml/de/clothing.kvtml
/usr/share/apps/kvtml/de/computers.kvtml
/usr/share/apps/kvtml/de/currencies.kvtml
/usr/share/apps/kvtml/de/easy.kvtml
/usr/share/apps/kvtml/de/fruits.kvtml
/usr/share/apps/kvtml/de/hard.kvtml
/usr/share/apps/kvtml/de/inventions.kvtml
/usr/share/apps/kvtml/de/medium.kvtml
/usr/share/apps/kvtml/de/numbers.kvtml
/usr/share/apps/kvtml/de/objects.kvtml
/usr/share/apps/kvtml/de/people.kvtml
/usr/share/apps/kvtml/de/professions.kvtml
/usr/share/apps/kvtml/de/space.kvtml
/usr/share/apps/kvtml/de/sports.kvtml
/usr/share/apps/kvtml/de/transportation.kvtml
/usr/share/apps/kvtml/de/vegetables.kvtml
/usr/share/apps/kvtml/de/worldcapitals.kvtml
/usr/share/apps/kvtml/el/animals.kvtml
/usr/share/apps/kvtml/el/clothing.kvtml
/usr/share/apps/kvtml/el/computers.kvtml
/usr/share/apps/kvtml/el/currencies.kvtml
/usr/share/apps/kvtml/el/easy.kvtml
/usr/share/apps/kvtml/el/fruits.kvtml
/usr/share/apps/kvtml/el/hard.kvtml
/usr/share/apps/kvtml/el/inventions.kvtml
/usr/share/apps/kvtml/el/medium.kvtml
/usr/share/apps/kvtml/el/numbers.kvtml
/usr/share/apps/kvtml/el/objects.kvtml
/usr/share/apps/kvtml/el/people.kvtml
/usr/share/apps/kvtml/el/professions.kvtml
/usr/share/apps/kvtml/el/space.kvtml
/usr/share/apps/kvtml/el/sport.kvtml
/usr/share/apps/kvtml/el/transportation.kvtml
/usr/share/apps/kvtml/el/vegetables.kvtml
/usr/share/apps/kvtml/el/worldcapitals.kvtml
/usr/share/apps/kvtml/en/animals.kvtml
/usr/share/apps/kvtml/en/clothing.kvtml
/usr/share/apps/kvtml/en/computers.kvtml
/usr/share/apps/kvtml/en/currencies.kvtml
/usr/share/apps/kvtml/en/easy.kvtml
/usr/share/apps/kvtml/en/fruits.kvtml
/usr/share/apps/kvtml/en/hard.kvtml
/usr/share/apps/kvtml/en/inventions.kvtml
/usr/share/apps/kvtml/en/medium.kvtml
/usr/share/apps/kvtml/en/numbers.kvtml
/usr/share/apps/kvtml/en/objects.kvtml
/usr/share/apps/kvtml/en/people.kvtml
/usr/share/apps/kvtml/en/professions.kvtml
/usr/share/apps/kvtml/en/space.kvtml
/usr/share/apps/kvtml/en/sports.kvtml
/usr/share/apps/kvtml/en/transportation.kvtml
/usr/share/apps/kvtml/en/vegetables.kvtml
/usr/share/apps/kvtml/en/worldcapitals.kvtml
/usr/share/apps/kvtml/en_GB/animals.kvtml
/usr/share/apps/kvtml/en_GB/animals_en_gb.kvtml
/usr/share/apps/kvtml/en_GB/clothing.kvtml
/usr/share/apps/kvtml/en_GB/computers.kvtml
/usr/share/apps/kvtml/en_GB/currencies.kvtml
/usr/share/apps/kvtml/en_GB/easy.kvtml
/usr/share/apps/kvtml/en_GB/fruits.kvtml
/usr/share/apps/kvtml/en_GB/hard.kvtml
/usr/share/apps/kvtml/en_GB/inventions.kvtml
/usr/share/apps/kvtml/en_GB/medium.kvtml
/usr/share/apps/kvtml/en_GB/numbers.kvtml
/usr/share/apps/kvtml/en_GB/objects.kvtml
/usr/share/apps/kvtml/en_GB/people.kvtml
/usr/share/apps/kvtml/en_GB/professions.kvtml
/usr/share/apps/kvtml/en_GB/space.kvtml
/usr/share/apps/kvtml/en_GB/sport.kvtml
/usr/share/apps/kvtml/en_GB/transportation.kvtml
/usr/share/apps/kvtml/en_GB/vegetables.kvtml
/usr/share/apps/kvtml/en_GB/worldcapitals.kvtml
/usr/share/apps/kvtml/es/animals.kvtml
/usr/share/apps/kvtml/es/computadoras.kvtml
/usr/share/apps/kvtml/es/deportes.kvtml
/usr/share/apps/kvtml/es/easy.kvtml
/usr/share/apps/kvtml/es/espacio.kvtml
/usr/share/apps/kvtml/es/frutas.kvtml
/usr/share/apps/kvtml/es/gente.kvtml
/usr/share/apps/kvtml/es/hard.kvtml
/usr/share/apps/kvtml/es/inventos.kvtml
/usr/share/apps/kvtml/es/medium.kvtml
/usr/share/apps/kvtml/es/monedas.kvtml
/usr/share/apps/kvtml/es/numeros.kvtml
/usr/share/apps/kvtml/es/objetos.kvtml
/usr/share/apps/kvtml/es/prendas.kvtml
/usr/share/apps/kvtml/es/professiones.kvtml
/usr/share/apps/kvtml/es/transportes.kvtml
/usr/share/apps/kvtml/es/vegetales.kvtml
/usr/share/apps/kvtml/es/worldcapitals.kvtml
/usr/share/apps/kvtml/et/animals.kvtml
/usr/share/apps/kvtml/et/easy.kvtml
/usr/share/apps/kvtml/et/hard.kvtml
/usr/share/apps/kvtml/et/medium.kvtml
/usr/share/apps/kvtml/fi/animals.kvtml
/usr/share/apps/kvtml/fi/easy.kvtml
/usr/share/apps/kvtml/fi/hard.kvtml
/usr/share/apps/kvtml/fi/medium.kvtml
/usr/share/apps/kvtml/fr/animals.kvtml
/usr/share/apps/kvtml/fr/easy.kvtml
/usr/share/apps/kvtml/fr/hard.kvtml
/usr/share/apps/kvtml/fr/maison.kvtml
/usr/share/apps/kvtml/fr/medium.kvtml
/usr/share/apps/kvtml/ga/animals.kvtml
/usr/share/apps/kvtml/ga/clothing.kvtml
/usr/share/apps/kvtml/ga/computers.kvtml
/usr/share/apps/kvtml/ga/currencies.kvtml
/usr/share/apps/kvtml/ga/easy.kvtml
/usr/share/apps/kvtml/ga/fruits.kvtml
/usr/share/apps/kvtml/ga/hard.kvtml
/usr/share/apps/kvtml/ga/inventions.kvtml
/usr/share/apps/kvtml/ga/medium.kvtml
/usr/share/apps/kvtml/ga/numbers.kvtml
/usr/share/apps/kvtml/ga/objects.kvtml
/usr/share/apps/kvtml/ga/people.kvtml
/usr/share/apps/kvtml/ga/professions.kvtml
/usr/share/apps/kvtml/ga/space.kvtml
/usr/share/apps/kvtml/ga/sports.kvtml
/usr/share/apps/kvtml/ga/transportation.kvtml
/usr/share/apps/kvtml/ga/vegetables.kvtml
/usr/share/apps/kvtml/ga/worldcapitals.kvtml
/usr/share/apps/kvtml/gl/animals.kvtml
/usr/share/apps/kvtml/gl/capitaisdomundo.kvtml
/usr/share/apps/kvtml/gl/deportes.kvtml
/usr/share/apps/kvtml/gl/easy.kvtml
/usr/share/apps/kvtml/gl/espazo.kvtml
/usr/share/apps/kvtml/gl/froita.kvtml
/usr/share/apps/kvtml/gl/hard.kvtml
/usr/share/apps/kvtml/gl/informatica.kvtml
/usr/share/apps/kvtml/gl/invencions.kvtml
/usr/share/apps/kvtml/gl/medium.kvtml
/usr/share/apps/kvtml/gl/moedas.kvtml
/usr/share/apps/kvtml/gl/obxectos.kvtml
/usr/share/apps/kvtml/gl/profesions.kvtml
/usr/share/apps/kvtml/gl/roupa.kvtml
/usr/share/apps/kvtml/gl/transporte.kvtml
/usr/share/apps/kvtml/gl/verduras.kvtml
/usr/share/apps/kvtml/gl/xente.kvtml
/usr/share/apps/kvtml/hu/animals.kvtml
/usr/share/apps/kvtml/hu/clothing.kvtml
/usr/share/apps/kvtml/hu/computers.kvtml
/usr/share/apps/kvtml/hu/currencies.kvtml
/usr/share/apps/kvtml/hu/fruits.kvtml
/usr/share/apps/kvtml/hu/numbers.kvtml
/usr/share/apps/kvtml/hu/transportation.kvtml
/usr/share/apps/kvtml/hu/worldcapitals.kvtml
/usr/share/apps/kvtml/it/animali.kvtml
/usr/share/apps/kvtml/it/animals.kvtml
/usr/share/apps/kvtml/it/capitalidelmondo.kvtml
/usr/share/apps/kvtml/it/computer.kvtml
/usr/share/apps/kvtml/it/easy.kvtml
/usr/share/apps/kvtml/it/hard.kvtml
/usr/share/apps/kvtml/it/invenzioni.kvtml
/usr/share/apps/kvtml/it/medium.kvtml
/usr/share/apps/kvtml/it/numeri.kvtml
/usr/share/apps/kvtml/it/oggetti.kvtml
/usr/share/apps/kvtml/it/persone.kvtml
/usr/share/apps/kvtml/it/spazio.kvtml
/usr/share/apps/kvtml/it/trasporti.kvtml
/usr/share/apps/kvtml/it/valute.kvtml
/usr/share/apps/kvtml/nb/animals.kvtml
/usr/share/apps/kvtml/nb/easy.kvtml
/usr/share/apps/kvtml/nb/hard.kvtml
/usr/share/apps/kvtml/nb/medium.kvtml
/usr/share/apps/kvtml/nds/animals.kvtml
/usr/share/apps/kvtml/nds/clothing.kvtml
/usr/share/apps/kvtml/nds/computers.kvtml
/usr/share/apps/kvtml/nds/currencies.kvtml
/usr/share/apps/kvtml/nds/easy.kvtml
/usr/share/apps/kvtml/nds/fruits.kvtml
/usr/share/apps/kvtml/nds/hard.kvtml
/usr/share/apps/kvtml/nds/inventions.kvtml
/usr/share/apps/kvtml/nds/medium.kvtml
/usr/share/apps/kvtml/nds/numbers.kvtml
/usr/share/apps/kvtml/nds/objects.kvtml
/usr/share/apps/kvtml/nds/people.kvtml
/usr/share/apps/kvtml/nds/professions.kvtml
/usr/share/apps/kvtml/nds/space.kvtml
/usr/share/apps/kvtml/nds/sports.kvtml
/usr/share/apps/kvtml/nds/transportation.kvtml
/usr/share/apps/kvtml/nds/vegetables.kvtml
/usr/share/apps/kvtml/nds/worldcapitals.kvtml
/usr/share/apps/kvtml/nl/Europese_landen.kvtml
/usr/share/apps/kvtml/nl/Nederlandse_eilanden.kvtml
/usr/share/apps/kvtml/nl/Nederlandse_provincies.kvtml
/usr/share/apps/kvtml/nl/animals.kvtml
/usr/share/apps/kvtml/nl/easy.kvtml
/usr/share/apps/kvtml/nl/hard.kvtml
/usr/share/apps/kvtml/nl/medium.kvtml
/usr/share/apps/kvtml/nn/animals.kvtml
/usr/share/apps/kvtml/nn/easy.kvtml
/usr/share/apps/kvtml/nn/hard.kvtml
/usr/share/apps/kvtml/nn/medium.kvtml
/usr/share/apps/kvtml/pa/animals.kvtml
/usr/share/apps/kvtml/pa/clothing.kvtml
/usr/share/apps/kvtml/pa/computers.kvtml
/usr/share/apps/kvtml/pa/currencies.kvtml
/usr/share/apps/kvtml/pa/easy.kvtml
/usr/share/apps/kvtml/pa/fruits.kvtml
/usr/share/apps/kvtml/pa/hard.kvtml
/usr/share/apps/kvtml/pa/inventions.kvtml
/usr/share/apps/kvtml/pa/medium.kvtml
/usr/share/apps/kvtml/pa/numbers.kvtml
/usr/share/apps/kvtml/pa/objects.kvtml
/usr/share/apps/kvtml/pa/people.kvtml
/usr/share/apps/kvtml/pa/professions.kvtml
/usr/share/apps/kvtml/pa/space.kvtml
/usr/share/apps/kvtml/pa/sports.kvtml
/usr/share/apps/kvtml/pa/transportation.kvtml
/usr/share/apps/kvtml/pa/vegetables.kvtml
/usr/share/apps/kvtml/pa/worldcapitals.kvtml
/usr/share/apps/kvtml/pl/animals.kvtml
/usr/share/apps/kvtml/pl/easy.kvtml
/usr/share/apps/kvtml/pl/hard.kvtml
/usr/share/apps/kvtml/pl/medium.kvtml
/usr/share/apps/kvtml/pt/animals.kvtml
/usr/share/apps/kvtml/pt/easy.kvtml
/usr/share/apps/kvtml/pt/hard.kvtml
/usr/share/apps/kvtml/pt/medium.kvtml
/usr/share/apps/kvtml/pt_BR/animals.kvtml
/usr/share/apps/kvtml/pt_BR/easy.kvtml
/usr/share/apps/kvtml/pt_BR/hard.kvtml
/usr/share/apps/kvtml/pt_BR/medium.kvtml
/usr/share/apps/kvtml/ro/animals.kvtml
/usr/share/apps/kvtml/ro/easy.kvtml
/usr/share/apps/kvtml/ro/hard.kvtml
/usr/share/apps/kvtml/ro/medium.kvtml
/usr/share/apps/kvtml/ru/animals.kvtml
/usr/share/apps/kvtml/ru/astronomy.kvtml
/usr/share/apps/kvtml/ru/computers.kvtml
/usr/share/apps/kvtml/ru/currencies.kvtml
/usr/share/apps/kvtml/ru/easy.kvtml
/usr/share/apps/kvtml/ru/hard.kvtml
/usr/share/apps/kvtml/ru/medium.kvtml
/usr/share/apps/kvtml/ru/numbers.kvtml
/usr/share/apps/kvtml/ru/objects.kvtml
/usr/share/apps/kvtml/ru/people.kvtml
/usr/share/apps/kvtml/ru/space.kvtml
/usr/share/apps/kvtml/ru/transportation.kvtml
/usr/share/apps/kvtml/ru/worldcapitals.kvtml
/usr/share/apps/kvtml/sk/animals.kvtml
/usr/share/apps/kvtml/sk/easy.kvtml
/usr/share/apps/kvtml/sk/hard.kvtml
/usr/share/apps/kvtml/sk/medium.kvtml
/usr/share/apps/kvtml/sl/animals.kvtml
/usr/share/apps/kvtml/sl/clothing.kvtml
/usr/share/apps/kvtml/sl/computers.kvtml
/usr/share/apps/kvtml/sl/currencies.kvtml
/usr/share/apps/kvtml/sl/easy.kvtml
/usr/share/apps/kvtml/sl/fruits.kvtml
/usr/share/apps/kvtml/sl/hard.kvtml
/usr/share/apps/kvtml/sl/inventions.kvtml
/usr/share/apps/kvtml/sl/medium.kvtml
/usr/share/apps/kvtml/sl/numbers.kvtml
/usr/share/apps/kvtml/sl/objects.kvtml
/usr/share/apps/kvtml/sl/people.kvtml
/usr/share/apps/kvtml/sl/professions.kvtml
/usr/share/apps/kvtml/sl/space.kvtml
/usr/share/apps/kvtml/sl/sports.kvtml
/usr/share/apps/kvtml/sl/transportation.kvtml
/usr/share/apps/kvtml/sl/vegetables.kvtml
/usr/share/apps/kvtml/sl/worldcapitals.kvtml
/usr/share/apps/kvtml/sr/animals.kvtml
/usr/share/apps/kvtml/sr/easy.kvtml
/usr/share/apps/kvtml/sr/hard.kvtml
/usr/share/apps/kvtml/sr/medium.kvtml
/usr/share/apps/kvtml/sr@ijekavian/animals.kvtml
/usr/share/apps/kvtml/sr@ijekavian/easy.kvtml
/usr/share/apps/kvtml/sr@ijekavian/hard.kvtml
/usr/share/apps/kvtml/sr@ijekavian/medium.kvtml
/usr/share/apps/kvtml/sr@ijekavianlatin/animals.kvtml
/usr/share/apps/kvtml/sr@ijekavianlatin/easy.kvtml
/usr/share/apps/kvtml/sr@ijekavianlatin/hard.kvtml
/usr/share/apps/kvtml/sr@ijekavianlatin/medium.kvtml
/usr/share/apps/kvtml/sr@latin/animals.kvtml
/usr/share/apps/kvtml/sr@latin/easy.kvtml
/usr/share/apps/kvtml/sr@latin/hard.kvtml
/usr/share/apps/kvtml/sr@latin/medium.kvtml
/usr/share/apps/kvtml/sv/animals.kvtml
/usr/share/apps/kvtml/sv/clothing.kvtml
/usr/share/apps/kvtml/sv/computers.kvtml
/usr/share/apps/kvtml/sv/currencies.kvtml
/usr/share/apps/kvtml/sv/easy.kvtml
/usr/share/apps/kvtml/sv/fruits.kvtml
/usr/share/apps/kvtml/sv/hard.kvtml
/usr/share/apps/kvtml/sv/inventions.kvtml
/usr/share/apps/kvtml/sv/medium.kvtml
/usr/share/apps/kvtml/sv/numbers.kvtml
/usr/share/apps/kvtml/sv/objects.kvtml
/usr/share/apps/kvtml/sv/people.kvtml
/usr/share/apps/kvtml/sv/professions.kvtml
/usr/share/apps/kvtml/sv/space.kvtml
/usr/share/apps/kvtml/sv/sports.kvtml
/usr/share/apps/kvtml/sv/transportation.kvtml
/usr/share/apps/kvtml/sv/vegetables.kvtml
/usr/share/apps/kvtml/sv/worldcapitals.kvtml
/usr/share/apps/kvtml/tg/animals.kvtml
/usr/share/apps/kvtml/tg/easy.kvtml
/usr/share/apps/kvtml/tg/hard.kvtml
/usr/share/apps/kvtml/tg/medium.kvtml
/usr/share/apps/kvtml/tr/animals.kvtml
/usr/share/apps/kvtml/tr/easy.kvtml
/usr/share/apps/kvtml/tr/hard.kvtml
/usr/share/apps/kvtml/tr/medium.kvtml
/usr/share/apps/kvtml/uk/animals.kvtml
/usr/share/apps/kvtml/uk/clothing.kvtml
/usr/share/apps/kvtml/uk/computers.kvtml
/usr/share/apps/kvtml/uk/currencies.kvtml
/usr/share/apps/kvtml/uk/easy.kvtml
/usr/share/apps/kvtml/uk/fruits.kvtml
/usr/share/apps/kvtml/uk/hard.kvtml
/usr/share/apps/kvtml/uk/inventions.kvtml
/usr/share/apps/kvtml/uk/medium.kvtml
/usr/share/apps/kvtml/uk/numbers.kvtml
/usr/share/apps/kvtml/uk/objects.kvtml
/usr/share/apps/kvtml/uk/people.kvtml
/usr/share/apps/kvtml/uk/professions.kvtml
/usr/share/apps/kvtml/uk/space.kvtml
/usr/share/apps/kvtml/uk/sports.kvtml
/usr/share/apps/kvtml/uk/transportation.kvtml
/usr/share/apps/kvtml/uk/vegetables.kvtml
/usr/share/apps/kvtml/uk/worldcapitals.kvtml
/usr/share/icons/hicolor/16x16/actions/editplots.png
/usr/share/icons/hicolor/16x16/actions/functionhelp.png
/usr/share/icons/hicolor/16x16/actions/integral_func.png
/usr/share/icons/hicolor/16x16/actions/maximum.png
/usr/share/icons/hicolor/16x16/actions/minimum.png
/usr/share/icons/hicolor/16x16/actions/newdifferential.png
/usr/share/icons/hicolor/16x16/actions/newfunction.png
/usr/share/icons/hicolor/16x16/actions/newimplicit.png
/usr/share/icons/hicolor/16x16/actions/newparametric.png
/usr/share/icons/hicolor/16x16/actions/newpolar.png
/usr/share/icons/hicolor/16x16/actions/resetview.png
/usr/share/icons/hicolor/22x22/actions/editplots.png
/usr/share/icons/hicolor/22x22/actions/functionhelp.png
/usr/share/icons/hicolor/22x22/actions/maximum.png
/usr/share/icons/hicolor/22x22/actions/minimum.png
/usr/share/icons/hicolor/22x22/actions/newdifferential.png
/usr/share/icons/hicolor/22x22/actions/newfunction.png
/usr/share/icons/hicolor/22x22/actions/newimplicit.png
/usr/share/icons/hicolor/22x22/actions/newparametric.png
/usr/share/icons/hicolor/22x22/actions/newpolar.png
/usr/share/icons/hicolor/22x22/actions/resetview.png
/usr/share/icons/hicolor/32x32/actions/coords.png
/usr/share/icons/hicolor/32x32/actions/deriv_func.png
/usr/share/icons/hicolor/32x32/actions/editconstants.png
/usr/share/icons/hicolor/32x32/actions/editplots.png
/usr/share/icons/hicolor/32x32/actions/func.png
/usr/share/icons/hicolor/32x32/actions/functionhelp.png
/usr/share/icons/hicolor/32x32/actions/integral_func.png
/usr/share/icons/hicolor/32x32/actions/lessen.png
/usr/share/icons/hicolor/32x32/actions/magnify.png
/usr/share/icons/hicolor/32x32/actions/maximum.png
/usr/share/icons/hicolor/32x32/actions/minimum.png
/usr/share/icons/hicolor/32x32/actions/newdifferential.png
/usr/share/icons/hicolor/32x32/actions/newfunction.png
/usr/share/icons/hicolor/32x32/actions/newimplicit.png
/usr/share/icons/hicolor/32x32/actions/newparametric.png
/usr/share/icons/hicolor/32x32/actions/newpolar.png
/usr/share/icons/hicolor/32x32/actions/resetview.png
/usr/share/icons/hicolor/48x48/actions/editplots.png
/usr/share/icons/hicolor/48x48/actions/functionhelp.png
/usr/share/icons/hicolor/48x48/actions/maximum.png
/usr/share/icons/hicolor/48x48/actions/minimum.png
/usr/share/icons/hicolor/48x48/actions/newdifferential.png
/usr/share/icons/hicolor/48x48/actions/newfunction.png
/usr/share/icons/hicolor/48x48/actions/newimplicit.png
/usr/share/icons/hicolor/48x48/actions/newparametric.png
/usr/share/icons/hicolor/48x48/actions/newpolar.png
/usr/share/icons/hicolor/48x48/actions/resetview.png
/usr/share/icons/hicolor/64x64/actions/maximum.png
/usr/share/icons/hicolor/64x64/actions/minimum.png
/usr/share/icons/hicolor/scalable/actions/deriv_func.svgz
/usr/share/icons/hicolor/scalable/actions/editconstants.svgz
/usr/share/icons/hicolor/scalable/actions/editplots.svgz
/usr/share/icons/hicolor/scalable/actions/functionhelp.svgz
/usr/share/icons/hicolor/scalable/actions/integral_func.svgz
/usr/share/icons/hicolor/scalable/actions/maximum.svgz
/usr/share/icons/hicolor/scalable/actions/minimum.svgz
/usr/share/icons/hicolor/scalable/actions/newfunction.svgz
/usr/share/icons/hicolor/scalable/actions/newparametric.svgz
/usr/share/icons/hicolor/scalable/actions/newpolar.svgz
/usr/share/icons/hicolor/scalable/actions/resetview.svgz

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdeedu-data/4cc77b90af91e615a64ae04893fdffa7939db84c
