#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Devel
%define		pnam	Timer
Summary:	Devel::Timer - track and report execution time for parts of code
Summary(pl.UTF-8):   Devel::Timer - śledzenie i raportowanie czasu wykonywania fragmentów kodu
Name:		perl-Devel-Timer
Version:	0.01
Release:	2
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ee17c11e294393d16e07acf5d2a6f04b
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::Timer allows developers to accurately time how long a specific
piece of code takes to execute. This can be helpful in locating the
slowest parts of an existing application.

%description -l pl.UTF-8
Devel::Timer pozwala programiście dokładnie zmierzyć, jak długo
wykonują się dane fragmenty kodu. Może to być pomocne przy znajdywaniu
najwolniejszych części istniejącej aplikacji.

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
%{perl_vendorlib}/Devel/Timer.pm
# MyTimer.pm is just example (in bit odd place)
%{_mandir}/man3/*
