#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Getopt
%define	pnam	Auto
Summary:	Getopt::Auto - Framework for command-line applications
#Summary(pl):	
Name:		perl-Getopt-Auto
Version:	1.00
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl(Pod::Parser)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unix command line applications, rather than simple filters, are pretty
unpleasant to write; as well as actually writing the functionality,
there's the boring parsing of the command line arguments and so on. Even
with C<Getopt::Long> or equivalent, you still have to dispatch the
appropriate commands to the right subroutines, write a C<--help> and
C<--version> handler, and so on. This module abstracts out that code,
leaving you free just to concentrate on the functional part.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
