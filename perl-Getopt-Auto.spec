#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Getopt
%define	pnam	Auto
Summary:	Getopt::Auto - framework for command-line applications
Summary(pl):	Getopt::Auto - szkielet do aplikacji dzia³aj±cych z linii poleceñ
Name:		perl-Getopt-Auto
Version:	1.00
Release:	2
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f3362fa348d4ef2770b691d5d261f60d
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Pod::Parser)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unix command line applications, rather than simple filters, are pretty
unpleasant to write; as well as actually writing the functionality,
there's the boring parsing of the command line arguments and so on. Even
with Getopt::Long or equivalent, you still have to dispatch the
appropriate commands to the right subroutines, write a --help and
--version handler, and so on. This module abstracts out that code,
leaving you free just to concentrate on the functional part.

%description -l pl
Uniksowe aplikacje dzia³aj±ce z linii poleceñ, bardziej ni¿ proste
filtry, s± do¶æ nieprzyjemne przy pisaniu; oprócz w³a¶ciwego pisania
funkcjonalno¶ci, jest jeszcze nudne analizowanie argumentów linii
poleceñ itp. Nawet z u¿yciem Getopt::Long lub ekwiwalentu, nadal trzeba
przekierowywaæ odpowiednie polecenia do w³a¶ciwych funkcji, pisaæ
obs³ugê --help i --version itd. Ten modu³ umo¿liwia wyabstrahowanie
tego kodu, pozwalaj±c skoncentrowaæ siê na czê¶ci funkcjonalnej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
