#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Getopt
%define		pnam	Auto
%include	/usr/lib/rpm/macros.perl
Summary:	Getopt::Auto - framework for command-line applications
Summary(pl.UTF-8):	Getopt::Auto - szkielet do aplikacji działających z linii poleceń
Name:		perl-Getopt-Auto
Version:	1.00
Release:	3
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f3362fa348d4ef2770b691d5d261f60d
URL:		http://search.cpan.org/dist/Getopt-Auto/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Pod::Parser)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unix command line applications, rather than simple filters, are pretty
unpleasant to write; as well as actually writing the functionality,
there's the boring parsing of the command line arguments and so on.
Even with Getopt::Long or equivalent, you still have to dispatch the
appropriate commands to the right subroutines, write a --help and
- --version handler, and so on. This module abstracts out that code,
  leaving you free just to concentrate on the functional part.

%description -l pl.UTF-8
Uniksowe aplikacje działające z linii poleceń, bardziej niż proste
filtry, są dość nieprzyjemne przy pisaniu; oprócz właściwego pisania
funkcjonalności, jest jeszcze nudne analizowanie argumentów linii
poleceń itp. Nawet z użyciem Getopt::Long lub ekwiwalentu, nadal
trzeba przekierowywać odpowiednie polecenia do właściwych funkcji,
pisać obsługę --help i --version itd. Ten moduł umożliwia
wyabstrahowanie tego kodu, pozwalając skoncentrować się na części
funkcjonalnej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
