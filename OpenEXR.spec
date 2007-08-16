%define name	OpenEXR
%define fname	openexr
%define version	1.4.0
%define	fver	1.4.0a
%define release %mkrel 3

%define major		4
%define libname		%mklibname %name %major
%define develname	%mklibname %name -d

Name: 	 	%{name}
Summary: 	High-quality video format
Version: 	%{version}
Release: 	%{release}

Source:		http://savannah.nongnu.org/download/openexr/%{fname}-%{fver}.tar.bz2
# Switches detection order in acinclude.m4 so that -lpthread will be
# used rather than -pthread: this is to fix a problem where building
# against this library would cause undefined references to pthreads
# stuff, in e.g. pfstools - AdamW 2007/08
Patch0:		openexr-1.4.0-threads.patch
URL:		http://www.openexr.net/
License:	BSD
Group:		Graphics
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	fltk-devel
BuildRequires:	autoconf

%description
ILM developed the OpenEXR format in response to the demand for higher color
fidelity in the visual effects industry.

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries
#Provides:	%name
#Obsoletes:	%name = %version-%release

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{develname}
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides: 	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%{name}-devel
Obsoletes:	%{mklibname OpenEXR 4 -d}

%description -n %{develname}
Libraries and includes files for developing programs based on %name.

%prep
%setup -q -n %{fname}-%{version}
%patch0 -p1 -b .threads
autoconf

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog LICENSE NEWS README doc/*
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_datadir}/aclocal/*.m4
%{_libdir}/pkgconfig/*.pc


