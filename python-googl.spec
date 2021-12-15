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
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/p/python-googl/python-googl-%{version}.tar.gz
# Source0-md5:	7be46ada5eaa87effa6380c43563b583
URL:		https://pypi.python.org/pypi/python-googl
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-httplib2
BuildRequires:	python-setuptools >= 1:7.0
%endif
%if %{with python3}
BuildRequires:	python3-httplib2
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools >= 1:7.0
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

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/python_%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/python_%{module}-%{version}-py*.egg-info
%endif
