#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	googl
Summary:	Python goo.gl url shortener wrapper
Name:		python-%{module}
Version:	0.2.2
Release:	1
License:	Unknown
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/p/python-googl/python-googl-%{version}.tar.gz#md5=7be46ada5eaa87effa6380c43563b583
# Source0-md5:	7be46ada5eaa87effa6380c43563b583
URL:		https://pypi.python.org/pypi/python-googl
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%if %{with python2}
BuildRequires:	python-httplib2
BuildRequires:	python-setuptools >= 7.0
%endif
%if %{with python3}
BuildRequires:	python3-httplib2
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools >= 7.0
%endif
Requires:	python-httplib2
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python goo.gl url shortener wrapper.

%package -n python3-%{module}
Summary:	Python goo.gl url shortener wrapper
Group:		Libraries/Python
Requires:	python3-httplib2
Requires:	python3-modules

%description -n python3-%{module}
Python goo.gl url shortener wrapper.

%prep
%setup -q

# setup copy of source in py3 dir
set -- *
install -d py3
cp -a "$@" py3

%build
%if %{with python2}
%{__python} setup.py build --build-base build-2 %{?with_tests:test}
%endif

%if %{with python3}
%{__python3} setup.py build --build-base build-3 %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/python_%{module}-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/python_%{module}-%{version}-py*.egg-info
%endif
