%define module	Rose-DateTime
%define	modprefix Rose
%define up_version  0.532
%define version     %perl_convert_version %{up_version}
%define release	%mkrel 1

Summary:	DateTime helper functions and objects
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Rose/%{module}-%{up_version}.tar.gz
BuildRequires:	perl(DateTime)
BuildRequires:	perl(Rose::Object)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The Rose::DateTime::* modules provide a few convenience functions and
objects for use with DateTime dates.

%prep
%setup -q -n %{module}-%{up_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man*/*
%{perl_vendorlib}/%{modprefix}

