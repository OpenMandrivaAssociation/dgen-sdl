%define name dgen-sdl
%define version 1.27
%define release %mkrel 1

Name:		%{name}
Summary:	DGen Sega Genesis emulator, ported to SDL
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
URL:		http://dgen.sourceforge.net/
Group:		Emulators
License:	BSD
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	SDL-devel
%ifarch %{ix86}
BuildRequires:	nasm
%endif

%description
DGen/SDL is a free, open source emulator for Sega Genesis/MegaDrive systems. 
The latest version supports save states, interlace mode, Game Genie, 
Linux joystick support, compressed ROM images, and other nice features.

Warning! There is no GUI yet so you need to either run DGen/SDL from
terminal or use front-end (if there are any).

%prep
%setup -q

%build
%configure --without-star \
           --enable-opengl
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog COPYING INSTALL README
%{_bindir}/dgen
%{_bindir}/tobin
%{_mandir}/man1/dgen.1*
%{_mandir}/man1/tobin.1*
%{_mandir}/man5/dgenrc.5*

