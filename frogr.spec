#
# Conditional build:
%bcond_without	libsoup2	# libsoup 2.x instead of libsoup3

Summary:	Frogr - Flickr Remote Organizer for GNOME
Summary(pl.UTF-8):	Frogr - zdalny organizator Flickra dla GNOME
Name:		frogr
Version:	1.8.1
Release:	3
License:	GPL v3
Group:		X11/Applications/Graphics
Source0:	https://download.gnome.org/sources/frogr/1.8/%{name}-%{version}.tar.xz
# Source0-md5:	907498b2d9d6c4f5e593fd00416695f4
URL:		https://wiki.gnome.org/Apps/Frogr
BuildRequires:	gettext-tools >= 0.19.7
BuildRequires:	glib2-devel >= 1:2.56
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gtk+3-devel >= 3.16
BuildRequires:	json-glib-devel >= 1.2
BuildRequires:	libexif-devel >= 1:0.6.14
BuildRequires:	libgcrypt-devel >= 1.5.0
%{?with_libsoup2:BuildRequires:	libsoup-devel >= 2.42}
%{!?with_libsoup2:BuildRequires:	libsoup3-devel >= 3.0}
BuildRequires:	libxml2-devel >= 1:2.6.8
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	glib2 >= 1:2.56
Requires:	gtk+3 >= 3.16
Requires:	hicolor-icon-theme
Requires:	json-glib >= 1.2
Requires:	libexif >= 1:0.6.14
Requires:	libgcrypt >= 1.5.0
%{?with_libsoup2:Requires:	libsoup >= 2.42}
%{!?with_libsoup2:Requires:	libsoup3 >= 3.0}
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

# build fails on deprecated glib functions, disable -Werror
#%{__sed} -i -e "/'werror=true'/d" meson.build

%build
%meson \
	%{?with_libsoup2:-Dwith-libsoup2=true}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README THANKS TRANSLATORS
%attr(755,root,root) %{_bindir}/frogr
%{_datadir}/frogr
%{_datadir}/metainfo/org.gnome.frogr.appdata.xml
%{_desktopdir}/org.gnome.frogr.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.frogr.png
%{_iconsdir}/hicolor/scalable/apps/org.gnome.frogr.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.frogr-symbolic.svg
%{_mandir}/man1/frogr.1*
