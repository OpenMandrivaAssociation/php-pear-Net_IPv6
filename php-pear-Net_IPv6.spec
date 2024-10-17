%define		_class		Net
%define		_subclass	IPv6
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.2.1
Release:	5
Summary:	Check and validate IPv6 addresses
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Net_IPv6/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
The class allows you to:
- check if an address is an IPv6 address
- compress/uncompress IPv6 addresses
- check for an IPv4 compatible ending in an IPv6 address

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-3mdv2012.0
+ Revision: 742147
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-2
+ Revision: 679433
- mass rebuild

* Thu Feb 17 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-1
+ Revision: 638146
- 1.2.1

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 602111
- update to new version 1.1.0

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.5-6mdv2010.1
+ Revision: 468705
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.0.5-5mdv2010.0
+ Revision: 441451
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-4mdv2009.1
+ Revision: 322447
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-3mdv2009.0
+ Revision: 236986
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-2mdv2007.0
+ Revision: 82329
- Import php-pear-Net_IPv6

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-2mdk
- new group (Development/PHP)

* Thu Sep 22 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-1mdk
- 1.0.5

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-1mdk
- initial Mandriva package (PLD import)

