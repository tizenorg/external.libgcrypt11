Name: libgcrypt
Version: 1.4.4
Release: 5
Source0: ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-%{version}.tar.gz

License: LGPLv2+
Summary: A general-purpose cryptography library
BuildRequires: gawk libgpg-error-devel pkgconfig
Group: System/Libraries

%package devel
Summary: Development files for the %{name} package
Group: Development/Libraries
Requires: libgpg-error-devel
Requires: %{name} = %{version}-%{release}

%description
Libgcrypt is a general purpose crypto library based on the code used
in GNU Privacy Guard.  This is a development version.

%description devel
Libgcrypt is a general purpose crypto library based on the code used
in GNU Privacy Guard.  This package contains files needed to develop
applications using libgcrypt.

%prep
%setup -q

%build
%reconfigure --disable-static --enable-malloc0returnsnull \
           --with-gpg-error-prefix=%{_prefix}
make %{?jobs:-j%jobs}

%install
rm -fr $RPM_BUILD_ROOT
%make_install

%remove_docs

%clean
rm -fr $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
/%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%exclude %{_bindir}/libgcrypt-config
%exclude %{_prefix}/share/aclocal/*

