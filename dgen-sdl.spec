Name:		dgen-sdl
Summary:	DGen Sega Genesis emulator, ported to SDL
Version:	1.29
Release:	%mkrel 1
Source0:	http://sourceforge.net/projects/dgen/files/dgen/%{version}/%{name}-%{version}.tar.gz
URL:		http://dgen.sourceforge.net/
Group:		Emulators
License:	BSD
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
%doc AUTHORS ChangeLog COPYING README BUGS
%{_bindir}/dgen
%{_bindir}/dgen_tobin
%{_mandir}/man1/dgen.1*
%{_mandir}/man1/dgen_tobin.1*
%{_mandir}/man5/dgenrc.5*

