#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-coverage
Version  : 6.3.3
Release  : 119
URL      : https://files.pythonhosted.org/packages/f4/14/33067650d3be989870acacbd3ec3f493a15d350f90b6607dd8b3b26a0194/coverage-6.3.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/f4/14/33067650d3be989870acacbd3ec3f493a15d350f90b6607dd8b3b26a0194/coverage-6.3.3.tar.gz
Summary  : Code coverage measurement for Python
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: pypi-coverage-bin = %{version}-%{release}
Requires: pypi-coverage-filemap = %{version}-%{release}
Requires: pypi-coverage-lib = %{version}-%{release}
Requires: pypi-coverage-license = %{version}-%{release}
Requires: pypi-coverage-python = %{version}-%{release}
Requires: pypi-coverage-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
.. Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
.. For details: https://github.com/nedbat/coveragepy/blob/master/NOTICE.txt

%package bin
Summary: bin components for the pypi-coverage package.
Group: Binaries
Requires: pypi-coverage-license = %{version}-%{release}
Requires: pypi-coverage-filemap = %{version}-%{release}

%description bin
bin components for the pypi-coverage package.


%package filemap
Summary: filemap components for the pypi-coverage package.
Group: Default

%description filemap
filemap components for the pypi-coverage package.


%package lib
Summary: lib components for the pypi-coverage package.
Group: Libraries
Requires: pypi-coverage-license = %{version}-%{release}
Requires: pypi-coverage-filemap = %{version}-%{release}

%description lib
lib components for the pypi-coverage package.


%package license
Summary: license components for the pypi-coverage package.
Group: Default

%description license
license components for the pypi-coverage package.


%package python
Summary: python components for the pypi-coverage package.
Group: Default
Requires: pypi-coverage-python3 = %{version}-%{release}

%description python
python components for the pypi-coverage package.


%package python3
Summary: python3 components for the pypi-coverage package.
Group: Default
Requires: pypi-coverage-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(coverage)

%description python3
python3 components for the pypi-coverage package.


%prep
%setup -q -n coverage-6.3.3
cd %{_builddir}/coverage-6.3.3
pushd ..
cp -a coverage-6.3.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653010841
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-coverage
cp %{_builddir}/coverage-6.3.3/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-coverage/598f87f072f66e2269dd6919292b2934dbb20492
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/coverage
/usr/bin/coverage-3.10
/usr/bin/coverage3

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-coverage

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-coverage/598f87f072f66e2269dd6919292b2934dbb20492

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
