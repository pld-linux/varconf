Summary:	A config handling library
Summary(pl):	Biblioteka obs³uguj±ca konfiguracjê
Name:		varconf
Version:	0.5.0
Release:	1
License:	LGPL
Group:		Libraries
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
STAGE. varconf mo¿e parsowaæ pliki konfiguracyjne, parametry z linii
poleceñ i zmienne ¶rodowiskowe. Obs³uguje callbacki poprzez libsigc++
oraz mo¿e zapisywaæ dane z konfiguracji w obiektach konfiguracyjnych
lub jednej globalnej instancji konfiguracji.

%package devel
Summary:	Header files for varconf development
Summary(pl):	Pliki nag³ówkowe do tworzenia programów z u¿yciem varconf
Group:		Development/Libraries
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
Ten pakiet zawiera pliki nag³ówkowe potrzebne do tworzenia programów z
u¿yciem biblioteki varconf.

%package static
Summary:	Static libraries for varconf development
Summary(pl):	Statyczne biblioteki varconf
Group:		Development/Libraries
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
