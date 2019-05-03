%define debug_package %{nil}
Summary: 32 bits gcc lib
Name: libgcc32
Version: 4.8.5
Release: 28.el7_5.1%dist
License: LGPL
# 32 bit binaries are extracted from the built RPMs directly
# The RPMs come from CentOS and must match the version of the
# 64-bit equivalents we have in build deps or released pkgs.
Source0: libgcc-4.8.5-28.el7_5.1.i686.rpm
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
