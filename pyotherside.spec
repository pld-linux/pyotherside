# TODO: build also Qt6 module
#
# Conditional build:
%bcond_without	doc	# API documentation

Summary:	Asynchronous Python 3 Bindings for Qt 5 and Qt 6
Summary(pl.UTF-8):	Asynchroniczne wiązania Pythona 3 dla Qt 5 i Qt 6
Name:		pyotherside
Version:	1.6.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/thp/pyotherside/tags
Source0:	https://github.com/thp/pyotherside/archive/%{version}/pyotherside-%{version}.tar.gz
# Source0-md5:	240fa11fbb774538a3e6f875f1f6d638
URL:		https://github.com/thp/pyotherside/
BuildRequires:	Qt5Core-devel >= 5.1.0
BuildRequires:	Qt5Gui-devel >= 5.1.0
BuildRequires:	Qt5Qml-devel >= 5.1.0
BuildRequires:	Qt5Quick-devel >= 5.1.0
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	qt5-qmake >= 5.1.0
BuildRequires:	rpm-build >= 4.6
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Qt QML Plugin that provides access to a Python 3 interpreter from
QML.

%description -l pl.UTF-8
Wtyczka Qt Qml zapewniająca dostęp do interpretera Pythona 3 z
poziomu QML.

%package -n Qt5Qml-module-pyotherside
Summary:	Asynchronous Python 3 Bindings for Qt 5
Summary(pl.UTF-8):	Asynchroniczne wiązania Pythona 3 dla Qt 5
Group:		Libraries
Requires:	Qt5Qml >= 5.1.0

%description -n Qt5Qml-module-pyotherside
A Qt 5 QML Plugin that provides access to a Python 3 interpreter from
QML.

%description -n Qt5Qml-module-pyotherside -l pl.UTF-8
Wtyczka Qt 5 Qml zapewniająca dostęp do interpretera Pythona 3 z
poziomu QML.

%package apidocs
Summary:	API documentation for Python pyotherside module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona pyotherside
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Python pyotherside module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona pyotherside.

%prep
%setup -q -n pyotherside-%{version}

%build
qmake-qt5

%{__make}

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files -n Qt5Qml-module-pyotherside
%defattr(644,root,root,755)
%doc LICENSE README.md
%dir %{_libdir}/qt5/qml/io
%dir %{_libdir}/qt5/qml/io/thp
%dir %{_libdir}/qt5/qml/io/thp/pyotherside
%attr(755,root,root) %{_libdir}/qt5/qml/io/thp/pyotherside/libpyothersideplugin.so
%{_libdir}/qt5/qml/io/thp/pyotherside/pyotherside.qmltypes
%{_libdir}/qt5/qml/io/thp/pyotherside/qmldir

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_images,_static,*.html,*.js}
%endif
