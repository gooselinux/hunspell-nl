Name: hunspell-nl
Summary: Dutch hunspell dictionaries
Version: 1.10
Release: 2%{?dist}
Source: http://www.opentaal.org/bestanden/1_10/nl-dict.oxt
Group: Applications/Text
URL: http://www.opentaal.org/english.php
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: BSD or CC-BY
BuildArch: noarch

Requires: hunspell

%description
Dutch hunspell dictionaries.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
nl_NL_aliases="nl_AW nl_BE"
for lang in $nl_NL_aliases; do
        ln -s nl_NL.aff $lang.aff
        ln -s nl_NL.dic $lang.dic
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc description/desc_en_US.txt description/desc_nl_NL.txt README_EN.txt README_NL.txt           
%{_datadir}/myspell/*

%changelog
* Thu Jan 07 2010 Caolan McNamara <caolanm@redhat.com> - 1.10-2
- Resolves: rhbz#553299 fix License tag

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.10-1.1
- Rebuilt for RHEL 6

* Tue Aug 25 2009 Caolan McNamara <caolanm@redhat.com> - 1.10-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00g-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 1.00g-5
- retain timestamp

* Fri Jun 22 2009 Caolan McNamara <caolanm@redhat.com> - 1.00g-4
- extend coverage

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00g-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 09 2007 Caolan McNamara <caolanm@redhat.com> - 1.00g-2
- clarify license version

* Fri Jun 08 2007 Caolan McNamara <caolanm@redhat.com> - 1.00g-1
- OpenTaal project publishes Dutch Language Union approved dictionary

* Wed Feb 14 2007 Caolan McNamara <caolanm@redhat.com> - 0.20050720-1
- update to match upstream id

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20050617-1
- initial version
