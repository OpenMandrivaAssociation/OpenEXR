%define name	OpenEXR
%define fname	openexr
%define version	1.6.1
%define	fver	1.6.1
%define release %mkrel 1

%define major		6
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:		%{name}
Summary:	A high dynamic-range (HDR) image file format
Version:	%{version}
Release:	%{release}
Source:		http://savannah.nongnu.org/download/openexr/%{fname}-%{fver}.tar.bz2
# Switches detection order in acinclude.m4 so that -lpthread will be
# used rather than -pthread: this is to fix a problem where building
# against this library would cause undefined references to pthreads
# stuff, in e.g. pfstools - AdamW 2007/08
Patch0:		openexr-1.6.0-threads.patch
URL:		http://www.openexr.com
License:	BSD
Group:		Graphics
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	fltk-devel
BuildRequires:	libilmbase-devel

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
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes:	%mklibname OpenEXR 4 -d
#Provides:	%mklibname OpenEXR 4 -d

%description -n %{develname}
Libraries and includes files for developing programs based on %name.

%prep
%setup -q -n %{fname}-%{version}
%patch0 -p1 -b .threads
./bootstrap

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# Remove doc files installed by make install, we package them in %files
rm -rf %{buildroot}%{_docdir}/%{name}-%{version}

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README doc/*
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_datadir}/aclocal/*.m4
%{_libdir}/pkgconfig/*.pc
