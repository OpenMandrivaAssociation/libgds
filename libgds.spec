# This is packaged because it's needed when building Qt4 with iBase /
# Firebird support. See http://forum.mandriva.com/viewtopic.php?t=100963
# AdamW 2008/12

%define major		1.4.5
%define libname		%mklibname gds %{major}
%define develname	%mklibname gds -d

Summary:	A library of functions and generic data structures
Name:		libgds
Version:	1.4.5
Release:	%{mkrel 1}
# The website claims 'LGPL' but the tarball includes a copy of the GPL,
# no copy of the LGPL, and no info in any source file headers. I am
# mailing upstream for a clarification. - AdamW 2008/12
License:	GPL+
Group:		System/Libraries
Source0:	http://libgds.info.ucl.ac.be/downloads/%{name}-%{version}.tar.gz
URL:		http://libgds.info.ucl.ac.be/index.php
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	doxygen

%description
libGDS is a library of functions and generic data structures that is
used in various projects such as C-BGP. The library contains dynamic
arrays, hash tables, radix trees, Patricia trees, tokenizers, FIFO
queues, stacks, string management functions and memory management
functions.

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
libGDS is a library of functions and generic data structures that is
used in various projects such as C-BGP. The library contains dynamic
arrays, hash tables, radix trees, Patricia trees, tokenizers, FIFO
queues, stacks, string management functions and memory management
functions.

%package -n %{develname}
Summary:	Development headers for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
libGDS is a library of functions and generic data structures that is
used in various projects such as C-BGP. The library contains dynamic
arrays, hash tables, radix trees, Patricia trees, tokenizers, FIFO
queues, stacks, string management functions and memory management
functions. This package contains the development headers.

%prep
%setup -q

%build
# Note: libxml support is available, but broken, it fails to build
# - AdamW 2008/12
%configure2_5x --enable-doxygen
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/%{name}-%{major}.so

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/%{name}.*a
%{_libdir}/pkgconfig/%{name}.pc

