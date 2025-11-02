%define major 33
%define api 3_4
%define devname %mklibname %{name} -d
%define libname %mklibname openexr
%define libname_core %mklibname openexrcore
%define libname_ilm %mklibname ilmbase
%define develname_ilm %mklibname ilmbase -d

%define prehistoriclibname %mklibname openexr 3_0 28
%define ancientlibname %mklibname openexr 3_0 29
%define veryoldlibname %mklibname openexr 3_2 30
%define oldlibname %mklibname openexr 3_2 31
%define oldlibname_core %mklibname openexrcore 3_2 31
%define oldlibname_ilm %mklibname ilmbase 3_2 31

Summary:	A high dynamic-range (HDR) image file format
Name:		openexr
Version:	3.4.2
Release:	3
License:	BSD
Group:		Graphics
Url:		https://www.openexr.com
Source0:	https://github.com/AcademySoftwareFoundation/openexr/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(Imath)
BuildRequires:  pkgconfig(libdeflate)
BuildRequires:  pkgconfig(openjph)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(python)

Provides:	OpenEXR = %{version}-%{release}

%description
Industrial Light & Magic developed the OpenEXR format in response to the demand
for higher color fidelity in the visual effects industry.

%package -n %{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries
Obsoletes:	%{prehistoriclibname} < 3.1.0-0
Obsoletes:	%{ancientlibname} < 3.1.0-0
Obsoletes:	%{veryoldlibname} < 3.2.1-2
%rename %{oldlibname}

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n %{libname_ilm}
Summary:	Dynamic libraries from ilmbase
Group:		System/Libraries
%rename  %{oldlibname_ilm}

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
%rename %{oldlibname_core}

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
