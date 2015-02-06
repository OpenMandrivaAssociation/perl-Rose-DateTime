%define upstream_name	 Rose-DateTime
%define upstream_version 0.540

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	DateTime helper functions and objects
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Rose/Rose-DateTime-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DateTime)
BuildRequires:	perl(Rose::Object)

BuildArch:	noarch

%description
The Rose::DateTime::* modules provide a few convenience functions and
objects for use with DateTime dates.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man*/*
%{perl_vendorlib}/Rose


%changelog
* Mon May 09 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.537.0-1mdv2011.0
+ Revision: 672864
- update to new version 0.537

* Wed Feb 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.535.0-1
+ Revision: 635216
- update to new version 0.535

* Tue Mar 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.534.0-1mdv2011.0
+ Revision: 526819
- update to 0.534

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.533.0-1mdv2010.1
+ Revision: 461350
- update to 0.533

* Wed May 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.532.0-1mdv2010.0
+ Revision: 378117
- use new %%perl_convert_version macro

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.53.02-1mdv2009.0
+ Revision: 136347
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri May 04 2007 Olivier Thauvin <nanardon@mandriva.org> 0.53.02-1mdv2008.0
+ Revision: 22238
- 0.532


* Mon Jun 19 2006 Scott Karns <scottk@mandriva.org> 0.53-1mdv2007.0
- Version 0.53

* Fri May 19 2006 Scott Karns <scottk@mandriva.org> 0.52.2-1mdk
- Initial MDV release




