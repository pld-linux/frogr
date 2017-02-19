Summary:	Frogr - Flickr Remote Organizer for GNOME
Summary(pl.UTF-8):	Frogr - zdalny organizator Flickra dla GNOME
Name:		frogr
Version:	1.2
Release:	1
License:	GPL v3
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/GNOME/sources/frogr/1.2/%{name}-%{version}.tar.xz
# Source0-md5:	17ee73bb497daca2e16aa5df46e398d1
URL:		https://wiki.gnome.org/Apps/Frogr
BuildRequires:	gettext-tools >= 0.19.7
BuildRequires:	glib2-devel >= 1:2.44
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gtk+3-devel >= 3.12
BuildRequires:	json-glib-devel >= 0.12
BuildRequires:	libexif-devel >= 1:0.6.14
BuildRequires:	libgcrypt-devel >= 1.5.0
BuildRequires:	libsoup-devel >= 2.34
BuildRequires:	libxml2-devel >= 1:2.6.8
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	glib2 >= 1:2.44
Requires:	gtk+3 >= 3.12
Requires:	hicolor-icon-theme
Requires:	json-glib >= 0.12
Requires:	libexif >= 1:0.6.14
Requires:	libgcrypt >= 1.5.0
Requires:	libsoup >= 2.34
Requires:	libxml2 >= 1:2.6.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Frogr is a small application for the GNOME desktop that allows users
to manage their accounts in the Flickr image hosting website.

%description -l pl.UTF-8
Frogr to mały program dla środowiska GNOME, umożliwiający użytkownikom
zarządzanie swoimi kontami w serwisie zdjęciowym Flickr.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README THANKS TRANSLATORS
%attr(755,root,root) %{_bindir}/frogr
%{_datadir}/frogr
%{_datadir}/appdata/frogr.appdata.xml
%{_desktopdir}/frogr.desktop
%{_iconsdir}/hicolor/*x*/apps/frogr.png
%{_iconsdir}/hicolor/scalable/apps/frogr.svg
%{_iconsdir}/hicolor/scalable/apps/frogr-symbolic.svg
%{_pixmapsdir}/frogr.xpm
%{_mandir}/man1/frogr.1*
