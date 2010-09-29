Summary:	toric varieties and some combinatorial geometry computations
Name:		gap-toric
Version:	1.6
Release:	0.1
License:	GPL v2
Group:		Applications/Math
Source0:	http://www.opensourcemath.org/toric/toric%{version}.tar.gz
# Source0-md5:	9a58c542cca1d24ac2ae8e22c53c54c0
URL:		http://www.opensourcemath.org/toric/
Requires:	gap >= 4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Toric is a package that implements some computations related to
toric varieties and combinatorial geometry in GAP. With toric,
affine toric varieties can be created and related information
about them can be calculated.

%prep
%setup -q -n toric%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gap/pkg/toric

install -p *.g $RPM_BUILD_ROOT%{_datadir}/gap/pkg/toric
cp -a lib html doc $RPM_BUILD_ROOT%{_datadir}/gap/pkg/toric

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGES}.toric
%{_datadir}/gap/pkg/toric
