# Known to work for:
# - Mageia 5 (i586, x86_64)

Name: regina-normal
Summary: Mathematical software for low-dimensional topology
Version: 5.0
Release: 1.%{_vendor}
License: GPL
# I wish there were a more sane group (like Applications/Mathematics).
Group: Sciences/Mathematics
Source: http://prdownloads.sourceforge.net/regina/regina-%{version}.tar.gz
URL: http://regina.sourceforge.net/
Packager: Ben Burton <bab@debian.org>
BuildRoot: %{_tmppath}/%{name}-buildroot

Requires: mimehandler(application/pdf)
Requires: python
Conflicts: regina

BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: cppunit-devel
BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: gmp-devel
BuildRequires: gmpxx-devel
BuildRequires: graphviz-devel
BuildRequires: libstdc++-devel
BuildRequires: libxml2-devel
BuildRequires: qtbase5-devel
BuildRequires: qtsvg5-devel
BuildRequires: pkgconfig
BuildRequires: popt-devel
BuildRequires: python-devel
BuildRequires: shared-mime-info
BuildRequires: source-highlight-devel
BuildRequires: tokyocabinet-devel
BuildRequires: xsltproc
BuildRequires: zlib-devel

Prereq: /sbin/ldconfig

%description
Regina is a software package for 3-manifold and 4-manifold topologists,
with a focus on triangulations, normal surfaces and angle structures.

For 3-manifolds, it includes high-level tasks such as 3-sphere recognition,
connected sum decomposition and Hakenness testing, comes with a rich
database of census manifolds, and incorporates the SnapPea kernel for
working with hyperbolic manifolds.  For 4-manifolds, it offers a range of
combinatorial and algebraic tools, plus support for normal hypersurfaces.

Regina comes with a full graphical user interface, as well as Python bindings
and a low-level C++ programming interface.

%prep
%setup -n regina-%{version}

%build
export CFLAGS="${CFLAGS:-%optflags}"
export CPPFLAGS="${CPPFLAGS:-%optflags}"
export QTDIR="%qt4dir"
export PATH="%qt4dir/bin:$PATH"
export LIB_SUFFIX=$(echo %_lib | cut -b4-)

%cmake -DDISABLE_RPATH=1 -DCMAKE_INSTALL_PREFIX=/usr -DLIB_SUFFIX=$LIB_SUFFIX \
  -DDISABLE_MPI=1 -DPACKAGING_MODE=1
%make
LD_LIBRARY_PATH=`pwd`/engine:"$LD_LIBRARY_PATH" %make test ARGS=-V

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%post
/sbin/ldconfig
%update_menus
%update_desktop_database
%update_mime_database
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%clean_menus
%clean_desktop_database
%clean_mime_database
%update_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES.txt
%doc HIGHLIGHTS.txt
%doc LICENSE.txt
%docdir %{_datadir}/regina/docs/en/regina
%docdir %{_datadir}/regina/docs/en/regina-xml
%docdir %{_datadir}/regina/engine-docs
%{_bindir}/*
%{_datadir}/applications/regina.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/regina.xml
%{_datadir}/regina/
%{_includedir}/regina/
%{_libdir}/libregina-engine.so
%{_libdir}/libregina-engine.so.%{version}
%{_libdir}/python2.7/site-packages/regina/
%{_mandir}/*/*

%changelog
* Tue Sep 20 2016 Ben Burton <bab@debian.org> 5.0
- New upstream release.

* Fri Aug 29 2014 Ben Burton <bab@debian.org> 4.96
- New upstream release.

* Sun Nov 10 2013 Ben Burton <bab@debian.org> 4.95
- New upstream release.

* Tue Sep 17 2013 Ben Burton <bab@debian.org> 4.94
- New upstream release.
- Transitioned from Mandriva to Mageia.

* Tue May 29 2012 Ben Burton <bab@debian.org> 4.93
- New upstream release.

* Wed Mar 28 2012 Ben Burton <bab@debian.org> 4.92
- New upstream release.
- Ported from KDE4 to Qt4-only.

* Mon Sep 12 2011 Ben Burton <bab@debian.org> 4.90
- New upstream release.
- Ported from KDE3 to KDE4, and from autotools to cmake.

* Sat May 16 2009 Ben Burton <bab@debian.org> 4.6
- New upstream release.

* Tue Oct 28 2008 Ben Burton <bab@debian.org> 4.5.1
- New upstream release.
- Now requires kdegraphics-kpdf, which provides an embedded viewer for
  Regina's new PDF packets.

* Sat May 17 2008 Ben Burton <bab@debian.org> 4.5
- New upstream release.

* Sun Nov 25 2007 Ben Burton <bab@debian.org> 4.4
- New upstream release.
- Removed MPI-enabled utilities from packages, since this causes hassles
  for ordinary desktop users who need to hunt down MPICH dependencies.

* Fri May 5 2006 Ben Burton <bab@debian.org> 4.3.1
- New upstream release.

* Mon Mar 27 2006 Ben Burton <bab@debian.org> 4.3
- New upstream release.

* Sun Sep 18 2005 Ben Burton <bab@debian.org> 4.2.1
- New upstream release.

* Thu Jul 7 2005 Ben Burton <bab@debian.org> 4.2
- New upstream release.
- Reenabled Python scripting for Mandrake >= 10.1.
- Note that regina-normal now includes MPI support.  These packages are
  built against the MPICH implementation of MPI.

* Sun Jul 25 2004 Ben Burton <bab@debian.org> 4.1.3
- New upstream release.

* Fri Jun 25 2004 Ben Burton <bab@debian.org> 4.1.2
- Initial packaging using Mandrake 10.0 Official.
- Python scripting is initially disabled because of bugs in Mandrake 10.0's
  boost.python packaging (see Mandrake bug #9648).
