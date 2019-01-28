%define debug_package %{nil}
Summary: 32 bits gcc lib
Name: libgcc32
Version: 4.8.5
Release: 4.1%dist
License: LGPL
# 32 bit binaries are extracted from the built RPMs directly
# The RPMs come from CentOS
Source0: libgcc-4.8.5-4.el7.i686.rpm
ExclusiveArch: x86_64

BuildRequires: cpio
BuildRequires: genisoimage

%description
i686 libgcc, needed to build xen.

%build
rpm2cpio %{SOURCE0} | cpio -idmv

%install
cp -a * %{buildroot}/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc /usr/share/doc/*/*
/lib/*
