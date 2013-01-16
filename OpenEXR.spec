# this package should be renamed and the lib & devel resember the true lib
%define fname	openexr

%define major		6
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:		OpenEXR
Summary:	A high dynamic-range (HDR) image file format
Version:	1.7.0
Release:	4
Source:		http://savannah.nongnu.org/download/openexr/%{fname}-%{version}.tar.gz
Patch0:		openexr-1.7.0-gcc43.patch
Patch1:		openexr-automake-1.13.patch
URL:		http://www.openexr.com
License:	BSD
Group:		Graphics

BuildRequires:	fltk-devel
BuildRequires:	pkgconfig(IlmBase)

%description
Industrial Light & Magic developed the OpenEXR format in response to the demand
for higher color fidelity in the visual effects industry.

%package -n %{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n %{develname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname OpenEXR 4 -d} < 1.7.0-4

%description -n %{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -qn %{fname}-%{version}
%apply_patches
./bootstrap

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

# Remove doc files installed by make install, we package them in %files
rm -rf %{buildroot}%{_docdir}/%{name}-%{version}

%files
%doc AUTHORS ChangeLog NEWS README doc/*
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/aclocal/*.m4
%{_libdir}/pkgconfig/*.pc



%changelog
* Fri Dec 23 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.7.0-3
+ Revision: 744649
- rebuild
- disabled static
- cleaned up spec

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.7.0-2
+ Revision: 671967
- mass rebuild

* Mon Sep 20 2010 Tomas Kindl <supp@mandriva.org> 1.7.0-1mdv2011.0
+ Revision: 580287
- bump to 1.7.0
- remove most patches (not necessary anymore)
- fix missing header

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6.1-5mdv2010.1
+ Revision: 521911
- rebuilt for 2010.1

* Sun Aug 02 2009 Oden Eriksson <oeriksson@mandriva.com> 1.6.1-4mdv2010.0
+ Revision: 407569
- P3: security fix for CVE-2009-1720
- P4: security fix for CVE-2009-1720
- P5: security fix for CVE-2009-1721

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.6.1-3mdv2009.0
+ Revision: 265273
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed May 21 2008 Oden Eriksson <oeriksson@mandriva.com> 1.6.1-2mdv2009.0
+ Revision: 209727
- added a gcc43 patch from fedora

  + Thierry Vignaud <tv@mandriva.org>
    - fix description-line-too-long

* Thu Jan 03 2008 Olivier Blin <blino@mandriva.org> 1.6.1-1mdv2008.1
+ Revision: 141036
- restore BuildRoot

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - update to 1.6.1 version
    - new version
    - update summary and description
    - rediff patch 0
    - correct buildrequires
    - make use of %%major
    - new devel library policy
    - run bootstrap (needed by p0)

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 16 2007 Adam Williamson <awilliamson@mandriva.org> 1.4.0-3mdv2008.0
+ Revision: 64649
- remove unpackaged doc files in %%install
- package license (required for BSD)
- update autoconf buildrequire
- correct license
- new devel policy
- patch0: set it up so that -lpthread will be used when building against this lib rather than -pthread


* Sun Feb 25 2007 Giuseppe Ghibò <ghibo@mandriva.com> 1.4.0-2mdv2007.0
+ Revision: 125587
- Rebuilt against rpm-mandriva-setup 1.37.

* Tue Jan 30 2007 Giuseppe Ghibò <ghibo@mandriva.com> 1.4.0-1mdv2007.1
+ Revision: 115610
- Release 1.4.0.
- Remoted Patch0, Patch1.
- Added sources for release 1.4.0a.

* Sun Jan 28 2007 Giuseppe Ghibò <ghibo@mandriva.com> 1.2.2-4mdv2007.1
+ Revision: 114595
- %%{mkrel}.
- Import OpenEXR

* Thu Aug 18 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.2.2-3mdk
- C++ & libtool fixes

* Fri Jun 10 2005 Austin Acton <austin@mandriva.org> 1.2.2-2mdk
- rebuild
- lost Per Oyvind's changes somehow :-(

* Thu Jun 09 2005 Austin Acton <austin@mandriva.org> 1.2.2-1mdk
- 1.2.2
- source URL

* Tue May 03 2005 Per �yvind Karlsen <pkarlsen@mandriva.com> 1.2.1-3mdk
- fix build on older releases (libtool problem)
- %%{1}mdv2007.1

* Mon Oct 11 2004 Austin Acton <austin@mandrake.org> 1.2.1-2mdk
- fix license

* Mon Oct 11 2004 Austin Acton <austin@mandrake.org> 1.2.1-1mdk
- initial package

