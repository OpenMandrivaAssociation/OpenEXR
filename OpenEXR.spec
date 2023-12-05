%define major 30
%define api 3_1
%define devname %mklibname %{name} -d
%define libname %mklibname openexr %{api} %{major}
%define libname_core %mklibname openexrcore %{api} %{major}
%define libname_ilm %mklibname ilmbase %{api} %{major}
%define develname_ilm %mklibname ilmbase -d

%define oldlibname %mklibname openexr 3_0 29

Summary:	A high dynamic-range (HDR) image file format
Name:		openexr
Version:	3.2.1
Release:	1
License:	BSD
Group:		Graphics
Url:		http://www.openexr.com
Source0:	https://github.com/AcademySoftwareFoundation/openexr/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(Imath)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(python)

Provides:	OpenEXR = %{version}-%{release}
Provides:	openexr = %{version}-%{release}

%description
Industrial Light & Magic developed the OpenEXR format in response to the demand
for higher color fidelity in the visual effects industry.

%package -n %{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries
Obsoletes:	%{oldlibname} < 3.1.0-0
Obsoletes:	%{mklibname openexr 3_0 28} < 3.1.0-0

#Obsoletes: %{_lib}IlmImf2_2_23 =< 3.0.4
#Obsoletes: %{_lib}IlmImfUtil2_2_23 =< 3.0.4
#Obsoletes: %{_lib}IlmImf2_2_23 =< 3.0.4
#Obsoletes: %{_lib}IlmThread2_2_23 =< 3.0.4

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n %{libname_ilm}
Summary:	Dynamic libraries from ilmbase
Group:		System/Libraries

%description -n %{libname_ilm}
Dynamic libraries from ilmbase.

%package -n %{develname_ilm}
Summary:	Header files and static libraries from ilmbase
Group:		Development/C
Requires:	%{libname_ilm} = %{version}-%{release}
Requires:	%{devname} = %{version}-%{release}
Provides:	libilmbase-devel = %{version}-%{release}
Provides:	ilmbase-devel = %{version}-%{release}

%description -n %{develname_ilm}
Libraries and includes files for developing programs based on ilmbase.

%package -n %{libname_core}
Summary:	Dynamic libraries for OpenEXR Core
Group:		System/Libraries

%description -n %{libname_core}
Dynamic libraries for OpenEXR Core.

%package -n %{devname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	%{develname_ilm} = %{EVRD}
Requires:	%{name} = %{EVRD}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Libraries and includes files for developing programs based on %{name}.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

# Remove doc files installed by make install, we package them in %files
rm -rf %{buildroot}%{_docdir}/OpenEXR-%{version}
rm -rf %{buildroot}%{_docdir}/OpenEXR

%files
%{_bindir}/exr*
%doc *.md CODEOWNERS
#doc doc/*

%files -n %{libname}
%{_libdir}/libOpenEXR-%{api}.so.%{major}{,.*}
%{_libdir}/libOpenEXRUtil-%{api}.so.%{major}{,.*}

%files -n %{libname_ilm}
%{_libdir}/libIex-%{api}.so.%{major}{,.*}
%{_libdir}/libIlmThread-%{api}.so.%{major}{,.*}

%files -n %{libname_core}
%{_libdir}/libOpenEXRCore-%{api}.so.%{major}{,.*}

%files -n %{devname}
%dir %{_includedir}/OpenEXR
%{_includedir}/OpenEXR/Imf*.h
%{_includedir}/OpenEXR/openexr.h
%{_includedir}/OpenEXR/openexr_*.h
%{_includedir}/OpenEXR/OpenEXRConfig.h
%{_libdir}/libOpenEXR.so
%{_libdir}/libOpenEXR-%{api}.so
%{_libdir}/libOpenEXRCore.so
%{_libdir}/libOpenEXRCore-%{api}.so
%{_libdir}/libOpenEXRUtil.so
%{_libdir}/libOpenEXRUtil-%{api}.so
%{_libdir}/pkgconfig/OpenEXR.pc
%{_libdir}/cmake/OpenEXR/

%files -n %{develname_ilm}
%{_includedir}/OpenEXR/Iex*.h
%{_includedir}/OpenEXR/Ilm*.h
%{_libdir}/libIex.so
%{_libdir}/libIex-%{api}.so
%{_libdir}/libIlmThread.so
%{_libdir}/libIlmThread-%{api}.so
