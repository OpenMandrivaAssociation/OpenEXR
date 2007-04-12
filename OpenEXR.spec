%define name	OpenEXR
%define fname	openexr
%define version	1.4.0
%define	fver	1.4.0a
%define release %mkrel 2

%define major	4
%define libname %mklibname %name %major

Name: 	 	%{name}
Summary: 	High-quality video format
Version: 	%{version}
Release: 	%{release}

Source:		http://savannah.nongnu.org/download/openexr/%{fname}-%{fver}.tar.bz2
URL:		http://www.openexr.net/
License:	Freeware
Group:		Graphics
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	fltk-devel
BuildRequires:	autoconf2.5 >= 2.54

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

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides: 	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%name-devel

%description -n %{libname}-devel
Libraries and includes files for developing programs based on %name.

%prep
%setup -q -n %{fname}-%{version}
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
%doc AUTHORS ChangeLog NEWS README doc/*
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_datadir}/aclocal/*.m4
%{_libdir}/pkgconfig/*.pc


