#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Set-Scalar
Version  : 1.29
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAVIDO/Set-Scalar-1.29.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAVIDO/Set-Scalar-1.29.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libset-scalar-perl/libset-scalar-perl_1.29-2.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl
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

%description dev
dev components for the perl-Set-Scalar package.


%prep
%setup -q -n Set-Scalar-1.29
cd ..
%setup -q -T -D -n Set-Scalar-1.29 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Set-Scalar-1.29/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
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
/usr/lib/perl5/vendor_perl/5.28.2/Set/Scalar.pm
/usr/lib/perl5/vendor_perl/5.28.2/Set/Scalar/Base.pm
/usr/lib/perl5/vendor_perl/5.28.2/Set/Scalar/Null.pm
/usr/lib/perl5/vendor_perl/5.28.2/Set/Scalar/Real.pm
/usr/lib/perl5/vendor_perl/5.28.2/Set/Scalar/Universe.pm
/usr/lib/perl5/vendor_perl/5.28.2/Set/Scalar/Valued.pm
/usr/lib/perl5/vendor_perl/5.28.2/Set/Scalar/ValuedUniverse.pm
/usr/lib/perl5/vendor_perl/5.28.2/Set/Scalar/Virtual.pm

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
