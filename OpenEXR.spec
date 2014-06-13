%define major	21
%define devname	%mklibname IlmImf Imf_2_1 -d

Summary:	A high dynamic-range (HDR) image file format
Name:		openexr
Version:	2.1.0
Release:	2
License:	BSD
Group:		Graphics
Url:		http://www.openexr.com
Source0:	http://savannah.nongnu.org/download/openexr/%{name}-%{version}.tar.gz
BuildRequires:	fltk-devel
BuildRequires:	pkgconfig(IlmBase) >= 2.1

%libpackage IlmImf Imf_2_1 %{major}

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

%package -n %{devname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{mklibname IlmImf Imf_2_1 %{major}} = %{EVRD}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}OpenEXR-devel < 1.7.0-5

%description -n %{devname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q
%apply_patches
./bootstrap

%build
%configure
%make

%install
%makeinstall_std

# Remove doc files installed by make install, we package them in %files
rm -rf %{buildroot}%{_docdir}/OpenEXR-%{version}

%files utils
%doc AUTHORS ChangeLog NEWS README doc/*
%{_bindir}/exr*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/aclocal/*.m4
%{_libdir}/pkgconfig/*.pc
