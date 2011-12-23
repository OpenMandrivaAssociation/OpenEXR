# this package should be renamed and the lib & devel resember the true lib
%define fname	openexr

%define major		6
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:		OpenEXR
Summary:	A high dynamic-range (HDR) image file format
Version:	1.7.0
Release:	3
Source:		http://savannah.nongnu.org/download/openexr/%{fname}-%{version}.tar.gz
Patch0:		openexr-1.7.0-gcc43.patch
URL:		http://www.openexr.com
License:	BSD
Group:		Graphics

BuildRequires:	fltk-devel
BuildRequires:	pkgconfig(IlmBase)

%description
Industrial Light & Magic developed the OpenEXR format in response to the demand
for higher color fidelity in the visual effects industry.

%package -n %{libname}
Summary:	Dynamic libraries from %name
Group:		System/Libraries

%description -n %{libname}
Dynamic libraries from %name.

%package -n %{develname}
Summary:	Header files and static libraries from %name
Group:		Development/C
Requires:	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes:	%mklibname OpenEXR 4 -d

%description -n %{develname}
Libraries and includes files for developing programs based on %name.

%prep
%setup -qn %{fname}-%{version}
%apply_patches
./bootstrap

%build
%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot}
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

