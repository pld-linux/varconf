Summary:	A config handling library
Summary(pl):	Biblioteka obs≥uguj±ca konfiguracjÍ
Name:		varconf
Version:	0.5.0
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	ftp://victor.worldforge.org/pub/worldforge/libs/varconf/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsigc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
varconf is a configuration system originally designed for the STAGE
server. varconf can parse configuration files, command-line arguments
and environment variables. It supports callbacks through libsigc++ and
can store configuration data in configuration objects or one global
configuration instance.

%description -l pl
varconf to system konfiguracji oryginalnie zaprojektowany dla serwera
STAGE. varconf moøe parsowaÊ pliki konfiguracyjne, parametry z linii
poleceÒ i zmienne ∂rodowiskowe. Obs≥uguje callbacki poprzez libsigc++
oraz moøe zapisywaÊ dane z konfiguracji w obiektach konfiguracyjnych
lub jednej globalnej instancji konfiguracji.

%package devel
Summary:	Header files for varconf development
Summary(pl):	Pliki nag≥Ûwkowe do tworzenia programÛw z uøyciem varconf
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Requires:	libsigc++-devel

%description devel
varconf is a configuration system originally designed for the STAGE
server. varconf can parse configuration files, command-line arguments
and environment variables. It supports callbacks through libsigc++ and
can store configuration data in configuration objects or one global
configuration instance.

This package contains the header files needed to develop programs that
use these varconf.

%description devel -l pl
Ten pakiet zawiera pliki nag≥Ûwkowe potrzebne do tworzenia programÛw z
uøyciem biblioteki varconf.

%package static
Summary:	Static libraries for varconf development
Summary(pl):	Statyczne biblioteki varconf
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
varconf is a configuration system originally designed for the STAGE
server. varconf can parse configuration files, command-line arguments
and environment variables. It supports callbacks through libsigc++ and
can store configuration data in configuration objects or one global
configuration instance.

This package contains the static varconf libraries.

%description static -l pl
Ten pakiet zawiera statyczne biblioteki varconf.

%prep
%setup -q

%build
rm -f missing
libtoolize --copy --force
aclocal
autoheader
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog README 

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/varconf
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
