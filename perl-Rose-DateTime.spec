%define module	Rose-DateTime
%define	modprefix Rose

%define realversion	0.532
%define version		0.53.02

%define	rel	1
%define release	%mkrel %{rel}

Summary:	DateTime helper functions and objects
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{realversion}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(DateTime)
BuildRequires:	perl(Rose::Object)
BuildArch:	noarch

%description
The Rose::DateTime::* modules provide a few convenience functions and
objects for use with DateTime dates.

%prep
%setup -q -n %{module}-%{realversion}

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

