Summary:	A config handling library
Summary(pl):	Biblioteka obs³uguj±ca konfiguracjê
Name:		varconf
Version:	0.5.4
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/worldforge/%{name}-%{version}.tar.gz
# Source0-md5:	0a23cf727b8d8e55a60129fa9605c23b
Patch0:		%{name}-ac.patch
URL:		http://www.worldforge.org/dev/eng/libraries/varconf/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsigc++1-devel
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

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe potrzebne do tworzenia programów z
u¿yciem biblioteki varconf.

%package static
Summary:	Static libraries for varconf development
Summary(pl):	Statyczne biblioteki varconf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/varconf-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/varconf
%{_aclocaldir}/varconf.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
