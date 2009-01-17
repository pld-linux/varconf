Summary:	A config handling library
Summary(pl.UTF-8):	Biblioteka obsługująca konfigurację
Name:		varconf
Version:	0.6.5
Release:	0.1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.sourceforge.net/worldforge/%{name}-%{version}.tar.bz2
# Source0-md5:	24af36732c1c3addca4de60a10a6e945
Patch0:		%{name}-gcc43.patch
URL:		http://www.worldforge.org/dev/eng/libraries/varconf/
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

%description -l pl.UTF-8
varconf to system konfiguracji oryginalnie zaprojektowany dla serwera
STAGE. varconf może parsować pliki konfiguracyjne, parametry z linii
poleceń i zmienne środowiskowe. Obsługuje callbacki poprzez libsigc++
oraz może zapisywać dane z konfiguracji w obiektach konfiguracyjnych
lub jednej globalnej instancji konfiguracji.

%package devel
Summary:	Header files for varconf development
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia programów z użyciem varconf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libsigc++1-devel

%description devel
varconf is a configuration system originally designed for the STAGE
server. varconf can parse configuration files, command-line arguments
and environment variables. It supports callbacks through libsigc++ and
can store configuration data in configuration objects or one global
configuration instance.

This package contains the header files needed to develop programs that
use these varconf.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do tworzenia programów z
użyciem biblioteki varconf.

%package static
Summary:	Static libraries for varconf development
Summary(pl.UTF-8):	Statyczne biblioteki varconf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
varconf is a configuration system originally designed for the STAGE
server. varconf can parse configuration files, command-line arguments
and environment variables. It supports callbacks through libsigc++ and
can store configuration data in configuration objects or one global
configuration instance.

This package contains the static varconf libraries.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczne biblioteki varconf.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libvarconf-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvarconf-1.0.so.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvarconf-1.0.so
%{_libdir}/libvarconf-1.0.la
%{_includedir}/varconf-1.0
%{_pkgconfigdir}/varconf-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvarconf-1.0.a
