Name: shcov
Version: 5.0
Release: 2
Group: Development/Tools
##Source: %{name}-%{version}.tar.gz
Source: %{name}-5.tar.gz
License: GPL v2
URL: http://code.google.com/p/shcov/
Vendor: Simon Kågström
Summary: Code coverage testeri for shell scripts.
Buildroot: %{_tmppath}/%{name}-root
BuildArch: noarch
BuildRequires: python
Requires: python

%description
shcov is a gcov-like code coverage tester for bourne shell / bash scripts. It also has a lcov-like HTML output generator to present coverage results.

%prep
%setup -n %{name}-5

%build
python setup.py build

%install
python setup.py install --prefix %{buildroot}/usr

%clean
rm -fr %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/%{name}
%{_bindir}/shlcov
%{python_sitelib}/%{name}-5-py%{python_version}.egg-info
%{python_sitelib}/%{name}/__init__.py
%{python_sitelib}/%{name}/__init__.pyc
%{python_sitelib}/%{name}/config.py
%{python_sitelib}/%{name}/config.pyc
%{python_sitelib}/%{name}/file.py
%{python_sitelib}/%{name}/file.pyc
%{python_sitelib}/%{name}/utils.py
%{python_sitelib}/%{name}/utils.pyc
%{python_sitelib}/%{name}/__init__.pyo
%{python_sitelib}/%{name}/config.pyo
%{python_sitelib}/%{name}/file.pyo
%{python_sitelib}/%{name}/utils.pyo
%{_docdir}/%{name}/COPYING
%{_docdir}/%{name}/README
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/shlcov.1.gz
%{_datarootdir}/%{name}/data/amber.png
%{_datarootdir}/%{name}/data/emerald.png
%{_datarootdir}/%{name}/data/gcov.css
%{_datarootdir}/%{name}/data/glass.png
%{_datarootdir}/%{name}/data/ruby.png
%{_datarootdir}/%{name}/data/snow.png

%changelog
* Sun Nov 21 2010 Norbert Varzariu <loomsen@googlemail.com> - 5.0-2
- fix hardcoded python version (2.6 -> %{python_version})

* Thu Jul 01 2010 : Norbert Varzariu <loomsen@googlemail.com> - 5.0-1
- clean up spec file

* Thu Oct 08 2009 moulinfr@gmail.com
- Initial release.
