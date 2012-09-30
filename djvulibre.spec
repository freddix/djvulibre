Summary:	DjVu viewers, encoders and utilities
Name:		djvulibre
Version:	3.5.25.3
Release:	2
License:	GPL
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/djvu/%{name}-%{version}.tar.gz
# Source0-md5:	5f45d6cd5700b4dd31b1eb963482089b
Patch0:		%{name}-opt.patch
URL:		http://djvu.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	rsvg-convert
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DjVu is a web-centric format and software platform for distributing
documents and images. DjVu content downloads faster, displays and
renders faster, looks nicer on a screen, and consume less client
resources than competing formats. DjVu was originally developed at
AT&T Labs-Research by Leon Bottou, Yann LeCun, Patrick Haffner, and
many others. In March 2000, AT&T sold DjVu to LizardTech Inc. who now
distributes Windows/Mac plug-ins, and commercial encoders (mostly on
Windows).

%package devel
Summary:	Header file for DjVu library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for DjVu library.

%prep
%setup -qn %{name}-3.5.25
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub config
%{__aclocal} -I config
%{__autoconf}
%configure \
	PTHREAD_LIBS="-lpthread"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

# pass dtop_* to allow build w/o gnome/kde/etc. installed
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT			\
	plugindir=%{_plugindir}			\
	dtop_applications=%{_desktopdir}	\
	dtop_icons=%{_iconsdir}			\
	dtop_mimelnk=%{_datadir}/mimelnk	\
	dtop_applnk=				\
	dtop_pixmaps=%{_pixmapsdir}		\
	dtop_mime_info=				\
	dtop_application_registry=

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT NEWS README doc/*
%attr(755,root,root) %{_bindir}/[!d]*
%attr(755,root,root) %{_bindir}/d[!j]*
%attr(755,root,root) %{_bindir}/djv[!i]*
%attr(755,root,root) %ghost %{_libdir}/libdjvulibre.so.??
%attr(755,root,root) %{_libdir}/libdjvulibre.so.*.*.*

%dir %{_datadir}/djvu
%dir %{_datadir}/djvu/osi
%{_datadir}/djvu/osi/languages.xml
%{_datadir}/djvu/osi/en
%{_datadir}/djvu/pubtext

%lang(de) %{_datadir}/djvu/osi/de
%lang(fr) %{_datadir}/djvu/osi/fr
%lang(zh) %{_datadir}/djvu/osi/zh
%{_mandir}/man1/[!dn]*
%{_mandir}/man1/d[!j]*
%{_mandir}/man1/djv[!i]*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdjvulibre.so
%{_libdir}/libdjvulibre.la
%{_includedir}/libdjvu
%{_pkgconfigdir}/*.pc

