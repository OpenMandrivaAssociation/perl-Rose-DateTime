%define upstream_name	 Rose-DateTime
%define upstream_version 0.534

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	DateTime helper functions and objects
License:	Artistic/GPL
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Rose/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(DateTime)
BuildRequires:	perl(Rose::Object)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The Rose::DateTime::* modules provide a few convenience functions and
objects for use with DateTime dates.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{perl_vendorlib}/Rose
