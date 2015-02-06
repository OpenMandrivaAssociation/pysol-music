%define name pysol-music
%define version 4.40
%define release 11
%define pysolver 4.81-3mdk

Summary: Background music pack for PySol
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Games/Cards
URL: http://www.oberhumer.com/opensource/pysol/	
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
Requires: pysol >= %pysolver

%description
A collection of additional music adapted for use with PySol.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%_gamesdatadir/pysol
cp -r data/music %buildroot%_gamesdatadir/pysol

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README NEWS
%_gamesdatadir/pysol/music/*



%changelog
* Tue Jul 26 2011 GÃ¶tz Waschk <waschk@mandriva.org> 4.40-10mdv2012.0
+ Revision: 691696
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 4.40-9mdv2011.0
+ Revision: 242379
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sat Aug 26 2006 Götz Waschk <waschk@mandriva.org> 4.40-7mdv2007.0
- mkrel

* Thu Aug 25 2005 Götz Waschk <waschk@mandriva.org> 4.40-6mdk
- drop prefix

* Sat Aug 14 2004 Götz Waschk <waschk@linux-mandrake.com> 4.40-5mdk
- rebuild

