# Automatically generated by Net-Ping.spec.PL
%define perlmod Net-Ping
Summary:	%{perlmod} perl module
Name:		perl-%{perlmod}
Version:	2.15
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org./authors/id/B/BB/BBB/%{perlmod}-%{version}.tar.gz
Packager:	Rob Brown <bbb@cpan.org>
Prefix: 	/usr
BuildRequires:	perl
Requires:	perl
BuildRoot:	/var/tmp/%{name}-%{version}-root
Provides:	%{perlmod}

%description
%{perlmod} Perl Module

%prep
%setup -q -n %{perlmod}-%{version}

%build
perl Makefile.PL
make
make test

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT%{prefix} install
find $RPM_BUILD_ROOT%{prefix} -type f -print | perl -p -e "s@^$RPM_BUILD_ROOT(.*)@\$1*@g" | grep -v perllocal.pod | grep -v packlist > %{name}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-filelist
%defattr(-,root,root)

%post

%changelog
* Sat Apr 06 2002 Rob Brown <bbb@cpan.org>
- Hack to let this version override the default
* Thu Nov 15 2001 Rob Brown <bbb@cpan.org>
- initial creation
