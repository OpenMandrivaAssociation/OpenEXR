%define major 23
%define devname %mklibname IlmImf_2_2 -d

Summary:	A high dynamic-range (HDR) image file format
Name:		openexr
Version:	2.2.1
Release:	4
License:	BSD
Group:		Graphics
Url:		http://www.openexr.com
Source0:	http://savannah.nongnu.org/download/openexr/%{name}-%{version}.tar.gz
# fix tests for big endian arches
# https://github.com/openexr/openexr/issues/81
Patch0:		openexr-2.1.0-bigendian.patch
BuildRequires:	fltk-devel
BuildRequires:	pkgconfig(IlmBase) >= 2.2.1
BuildRequires:	pkgconfig(zlib)

%libpackage IlmImf 2_2 %{major}
%libpackage IlmImfUtil 2_2 %{major}

%description
Industrial Light & Magic developed the OpenEXR format in response to the demand
for higher color fidelity in the visual effects industry.

%package utils
Summary:	A high dynamic-range (HDR) image file format
Group:		Graphics
Obsoletes:	OpenEXR < 1.7.0-6

%description utils
Industrial Light & Magic developed the OpenEXR format in response to the demand
for higher color fidelity in the visual effects industry.

%package -n %{devname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{mklibname IlmImf 2_2 %{major}} = %{EVRD}
Requires:	%{mklibname IlmImfUtil 2_2 %{major}} = %{EVRD}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}OpenEXR-devel < 1.7.0-6

%description -n %{devname}
Libraries and includes files for developing programs based on %{name}.

%prep
%autosetup -p1
./bootstrap

%build
%configure
%make_build

%install
%make_install

# Remove doc files installed by make install, we package them in %files
rm -rf %{buildroot}%{_docdir}/OpenEXR-%{version}

%files utils
%doc AUTHORS NEWS README doc/*
%{_bindir}/exr*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/aclocal/*.m4
%{_libdir}/pkgconfig/*.pc
