Summary:	Library for interacting with RFC2229 dictionary servers
Summary(pl):	Biblioteka do komunikacji z serwerami s³ówników zgodnymi z RFC2229
Name:		libdict
Version:	0.9
Release:	2
License:	BSD-like
Group:		Development/Libraries
Source0:	ftp://ftp.dict.org/pub/dict/%{name}-%{version}.tar.gz
# Source0-md5:	42cc35f1bef8bbfbf7cecad716337081
Patch0:		%{name}-c++.patch
URL:		http://www.dict.org/
# for test program
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdict is a small C library that provides access to RFC2229
dictionary servers. This is done through a series of functions, each
representing a major function of the dict server.

%description -l pl
libdict to ma³a biblioteka w C daj±ca dostêp do serwerów s³owników
zgodnych z RFC2229. S³u¿y do tego szereg funkcji, z których ka¿da
reprezentuje du¿± funkcjê serwera dict.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -C src \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Iinclude -I../include -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_mandir}/man3} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install src/libdict.a $RPM_BUILD_ROOT%{_libdir}
install src/include/*.h $RPM_BUILD_ROOT%{_includedir}
install src/examples/*.c* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install doc/libdict.3 $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{LICENSE,responses,version-history}
%{_libdir}/lib*.a
%{_includedir}/*.h
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
