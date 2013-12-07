%define major	6
%define libname	%mklibname IlmImf %{major}
%define devname	%mklibname IlmImf -d

Summary:	A high dynamic-range (HDR) image file format
Name:		openexr
Version:	1.7.0
Release:	8
License:	BSD
Group:		Graphics
Url:		http://www.openexr.com
Source0:	http://savannah.nongnu.org/download/openexr/%{name}-%{version}.tar.gz
Patch0:		openexr-1.7.0-gcc43.patch
Patch1:		openexr-automake-1.13.patch
BuildRequires:	fltk-devel
BuildRequires:	pkgconfig(IlmBase)

%description
Industrial Light & Magic developed the OpenEXR format in response to the demand
for higher color fidelity in the visual effects industry.

%package utils
Summary:	A high dynamic-range (HDR) image file format
Group:		Graphics
Obsoletes:	OpenEXR < 1.7.0-5

%description utils
Industrial Light & Magic developed the OpenEXR format in response to the demand
for higher color fidelity in the visual effects industry.

%package -n %{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries
Obsoletes:	%{_lib}OpenEXR6 < 1.7.0-5

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n %{devname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}OpenEXR-devel < 1.7.0-5

%description -n %{devname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q
%apply_patches
./bootstrap

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

# Remove doc files installed by make install, we package them in %files
rm -rf %{buildroot}%{_docdir}/OpenEXR-%{version}

%files utils
%doc AUTHORS ChangeLog NEWS README doc/*
%{_bindir}/exr*

%files -n %{libname}
%{_libdir}/libIlmImf.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/aclocal/*.m4
%{_libdir}/pkgconfig/*.pc

