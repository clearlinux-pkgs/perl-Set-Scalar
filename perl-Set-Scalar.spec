#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Set-Scalar
Version  : 1.29
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAVIDO/Set-Scalar-1.29.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAVIDO/Set-Scalar-1.29.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libset-scalar-perl/libset-scalar-perl_1.29-2.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Set-Scalar-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
The first priority of Set::Scalar is to be a convenient interface
to sets (as in: unordered colletions of Perl scalars.)  While not
designed to be slow or big, neither has it been designed to be
fast or compact.

%package dev
Summary: dev components for the perl-Set-Scalar package.
Group: Development
Provides: perl-Set-Scalar-devel = %{version}-%{release}
Requires: perl-Set-Scalar = %{version}-%{release}

%description dev
dev components for the perl-Set-Scalar package.


%package perl
Summary: perl components for the perl-Set-Scalar package.
Group: Default
Requires: perl-Set-Scalar = %{version}-%{release}

%description perl
perl components for the perl-Set-Scalar package.


%prep
%setup -q -n Set-Scalar-1.29
cd %{_builddir}
tar xf %{_sourcedir}/libset-scalar-perl_1.29-2.debian.tar.xz
cd %{_builddir}/Set-Scalar-1.29
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Set-Scalar-1.29/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Set::Scalar.3
/usr/share/man/man3/Set::Scalar::Base.3
/usr/share/man/man3/Set::Scalar::Null.3
/usr/share/man/man3/Set::Scalar::Real.3
/usr/share/man/man3/Set::Scalar::Universe.3
/usr/share/man/man3/Set::Scalar::Valued.3
/usr/share/man/man3/Set::Scalar::ValuedUniverse.3
/usr/share/man/man3/Set::Scalar::Virtual.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
