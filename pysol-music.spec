%define name pysol-music
%define version 4.40
%define release %mkrel 7
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

