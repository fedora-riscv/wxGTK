Name:           wxGTK
Version:        2.4.1
Release:        0.fdr.4.rh80
Epoch:          0
Summary:        %{name} is the GTK+ port of the wxWindows GUI library
License:        BSD
Group:          System Environment/Libraries
URL:            http://www.wxwindows.org/
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gtk+-devel gtk2-devel pkgconfig zlib-devel >= 0:1.1.4
BuildRequires:  libpng-devel libjpeg-devel libtiff-devel
Requires:       %{name}-common = %{epoch}:%{version}-%{release}

%description
wxWindows/GTK is the GTK+ (1.2) port of the C++ cross-platform wxWindows
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.

%package        devel
Group:          Development/Libraries
Summary:        Development files for the wxGTK library
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-common-devel = %{epoch}:%{version}-%{release}
Requires:       gtk+-devel
Conflicts:      %{name}2-devel

%description    devel
This package includes files needed to link with the wxGTK library.

%package     -n %{name}2
Group:          System Environment/Libraries
Summary:        %{name}2 is the GTK2 port of the wxWindows GUI library
Requires:       %{name}-common = %{epoch}:%{version}-%{release}

%description -n %{name}2
wxWindows/GTK2 is the GTK2 port of the C++ cross-platform wxWindows
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.

%package     -n %{name}2-devel
Group:          Development/Libraries
Summary:        Development files for the wxGTK2 library
Requires:       %{name}2 = %{epoch}:%{version}-%{release}
Requires:       %{name}-common-devel = %{epoch}:%{version}-%{release}
Requires:       gtk2-devel
Conflicts:      %{name}-devel

%description -n %{name}2-devel
This package include files needed to link with the wxGTK2 library.

%package        common
Group:          System Environment/Libraries
Summary:        wxGTK* common files

%description    common
Common files for wxWindows/GTK1 and GTK2.

%package        common-devel
Group:          Development/Libraries
Summary:        wxGTK* common development files

%description    common-devel
Common development files for wxWindows/GTK1 and GTK2.

%package        gl
Summary:        OpenGL add-on for the wxWindows library
Group:          System Environment/Libraries
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    gl
%{summary}.

%package     -n %{name}2-gl
Summary:        OpenGL add-on for the wxWindows library
Group:          System Environment/Libraries
Requires:       %{name}2 = %{epoch}:%{version}-%{release}

%description -n %{name}2-gl
%{summary}.

%package        stc
Summary:        Styled text control add-on for the wxWindows library
Group:          System Environment/Libraries
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    stc
Styled text control add-on for wxGTK. Based on the Scintillia project.

%package     -n %{name}2-stc
Summary:        Styled text control add-on for the wxWindows library
Group:          System Environment/Libraries
Requires:       %{name}2 = %{epoch}:%{version}-%{release}

%description -n %{name}2-stc
Styled text control add-on for wxGTK2. Based on the Scintillia project.

%package        xrc
Summary:        The XML-based resource system for the wxWindows library
Group:          System Environment/Libraries
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    xrc
The XML-based resource system, known as XRC, allows user interface
elements such as dialogs, menu bars and toolbars, to be stored in
text files and loaded into the application at run-time.
This package is for the GTK 1.2 backend

%package     -n %{name}2-xrc
Summary:        The XML-based resource system for the wxWindows library
Group:          System Environment/Libraries
Requires:       %{name}2 = %{epoch}:%{version}-%{release}

%description -n %{name}2-xrc
The XML-based resource system, known as XRC, allows user interface
elements such as dialogs, menu bars and toolbars, to be stored in
text files and loaded into the application at run-time.
This package is for the GTK2 backend.


%prep
%setup -q -n %{name}-%{version}


%build
mkdir _gtk1 _gtk2
export APPEXTRACFLAGS="$RPM_OPT_FLAGS"
export APPEXTRACXXFLAGS="$RPM_OPT_FLAGS"

cd _gtk1
../configure \
  --prefix=%{_prefix} \
  --with-opengl \
  --enable-shared \
  --enable-soname
make %{?_smp_mflags}
make %{?_smp_mflags} -C contrib/src/stc
make %{?_smp_mflags} -C contrib/src/xrc

cd ../_gtk2
../configure \
  --prefix=%{_prefix} \
  --with-opengl \
  --enable-shared \
  --enable-soname \
  --enable-gtk2
make %{?_smp_mflags}
make %{?_smp_mflags} -C contrib/src/stc
make %{?_smp_mflags} -C contrib/src/xrc

cd ..

# -----------------------------------------------------------------------------

%install
rm -rf $RPM_BUILD_ROOT

cd _gtk1
%makeinstall
%makeinstall -C contrib/src/stc
%makeinstall -C contrib/src/xrc
cd ../_gtk2
%makeinstall
%makeinstall -C contrib/src/stc
%makeinstall -C contrib/src/xrc
cd ..

%find_lang wxstd


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post -n %{name}2 -p /sbin/ldconfig
%postun -n %{name}2 -p /sbin/ldconfig

%post devel
ln -sf $(basename %{_bindir}/wxgtk-*-config) %{_bindir}/wx-config

%post -n %{name}2-devel
ln -sf $(basename %{_bindir}/wxgtk2*-config) %{_bindir}/wx-config

%post gl -p /sbin/ldconfig
%postun gl -p /sbin/ldconfig

%post -n %{name}2-gl -p /sbin/ldconfig
%postun -n %{name}2-gl -p /sbin/ldconfig

%post stc -p /sbin/ldconfig
%postun stc -p /sbin/ldconfig

%post -n %{name}2-stc -p /sbin/ldconfig
%postun -n %{name}2-stc -p /sbin/ldconfig

%post xrc -p /sbin/ldconfig
%postun xrc -p /sbin/ldconfig

%post -n %{name}2-xrc -p /sbin/ldconfig
%postun -n %{name}2-xrc -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%{_libdir}/libwx_gtk-*.so.*

%files devel
%defattr(-,root,root,-)
%ghost %{_bindir}/wx-config
%{_bindir}/wxgtk-*-config
%{_libdir}/libwx_gtk-*.so
%{_libdir}/wx/include/gtk-*

%files -n %{name}2
%defattr(-,root,root,-)
%{_libdir}/libwx_gtk2-*.so.*

%files -n %{name}2-devel
%defattr(-,root,root,-)
%ghost %{_bindir}/wx-config
%{_bindir}/wxgtk2*-config
%{_libdir}/libwx_gtk2-*.so
%{_libdir}/wx/include/gtk2*

%files common -f wxstd.lang
%defattr(-,root,root,-)
%doc CHANGES*.txt COPYING.LIB LICENCE.txt README*.txt
%dir %{_libdir}/wx
%{_datadir}/wx

%files common-devel
%defattr(-,root,root,-)
%{_datadir}/aclocal/*
%{_includedir}/wx
%dir %{_libdir}/wx/include

%files gl
%defattr(-,root,root,-)
%{_libdir}/libwx_gtk_gl-*.so*

%files -n %{name}2-gl
%defattr(-,root,root,-)
%{_libdir}/libwx_gtk2_gl-*.so*

%files stc
%defattr(-,root,root,-)
%doc contrib/src/stc/README.txt
%{_libdir}/libwx_gtk_stc-*.so*

%files -n %{name}2-stc
%defattr(-,root,root,-)
%doc contrib/src/stc/README.txt
%{_libdir}/libwx_gtk2_stc-*.so*

%files xrc
%defattr(-,root,root,-)
%{_libdir}/libwx_gtk_xrc-*.so*

%files -n %{name}2-xrc
%defattr(-,root,root,-)
%{_libdir}/libwx_gtk2_xrc-*.so*


%changelog
* Mon Aug  4 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.4.1-0.fdr.4
- Borrow Matthias Saou's -gl and -stc subpackages.

* Mon Jun 16 2003 Dams <anvil[AT]livna.org> 0:2.4.1-0.fdr.3
- Removed libwx_gtk2_xrc*so* from wxGTK2/wxGTK2-devel packages

* Sun Jun 15 2003 Dams <anvil[AT]livna.org> 0:2.4.1-0.fdr.2
- Removed *-devel postun scriptlets (from Ville Skyttä)

* Sat Jun 14 2003 Dams <anvil[AT]livna.org> 0:2.4.1-0.fdr.1
- Updated to 2.4.1

* Wed May 28 2003 Dams <anvil[AT]livna.org> 0:2.4.0-0.fdr.7
- Added xrc contrib in separate packages

* Wed May 21 2003 Dams <anvil[AT]livna.org> 0:2.4.0-0.fdr.6
- Corrected typo in postun devel

* Wed May 21 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.4.0-0.fdr.5
- Make -devel packages require the corresponding GTK devel package.
- Save .spec in UTF-8.
- Fixes from Dams:
- Don't build --with-unicode, it breaks stuff (as was already noted by Dams).
- Don't remove wx-config symlinks on upgrades.
- Remove duplicates from docs.

* Tue May 20 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.4.0-0.fdr.4
- Split into subpackages, spec file rewrite.
- Use bzipped upstream tarball.
- Clean up BuildRequirement versions.

* Fri May  9 2003 Dams <anvil[AT]livna.org> 0:2.4.0-0.fdr.3
- Now build/include both gtk/gtk2 libs
- buildroot -> RPM_BUILD_ROOT

* Mon Mar  3 2003 Dams <anvil@livna.org> 
- Initial build.
- Disable unicode as it breaks lmule
- use the %find_lang macro for locale
