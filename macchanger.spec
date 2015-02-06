%define	name	macchanger 
%define	version	1.5.0
%define release 	8
%define	lib_name_orig	lib%{name}
%define	lib_major	0
%define	lib_name	%mklibname %{name} %{lib_major}

Name:           %{name}
Summary: 	Uility for viewing/manipulating the MAC address of network interfaces
Group:		System/Configuration/Networking
Version:        %{version}
Release:        %{release}
License:	GPL 
URL:		http://www.alobbs.com/macchanger/
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-buildroot


%description
A GNU/Linux utility for viewing/manipulating the MAC address of network 
interfaces.
Features
* Set specific MAC address of a network interface
* Set the MAC randomly
* Set a MAC of another vendor
* Set another MAC of the same vendor
* Set a MAC of the same kind (eg: wireless card)
* Display a vendor MAC list (today, 6200 items) to choose from

Possible usages
* You're in a DHCP network with some kind of IP-based restriction
* You've a cluster that boot with BOOTP and you want to have a
* clean set of MACs
* Debug MAC based routes
	    
%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall



%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING ChangeLog INSTALL AUTHORS
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/*
%{_infodir}/%{name}.info*
%defattr(755,root,root,755)
%{_bindir}/*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-6mdv2011.0
+ Revision: 620286
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.5.0-5mdv2010.0
+ Revision: 439695
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 1.5.0-4mdv2009.0
+ Revision: 251620
- rebuild

* Tue Feb 12 2008 Antoine Ginies <aginies@mandriva.com> 1.5.0-2mdv2008.1
+ Revision: 165895
- re-add buildroot tag
- remove buildroot

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 21 2007 Antoine Ginies <aginies@mandriva.com> 1.5.0-2mdv2008.0
+ Revision: 29315
- update URL
- Import macchanger



* Fri Jun 23 2006 Antoine Ginies <aginies@mandriva.com> 1.5.0-2mdv2007.0
- rebuild

* Fri May 21 2004 Antoine Ginies <aginies@n2.mandrakesoft.com> 1.5.0-1mdk
- release 1.5.0

* Sun Jan 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.4.0-1mdk
- 1.4.0
- rm -rf $RPM_BUILD_ROOT in %%install, not %%prep
- drop redundant provides
- use %%configure and %%make macro
- macroize
- cleanups
- use %%mklibname macro
- add info file

* Fri Jan 03 2003 Antoine Ginies <aginies@mandrakesoft.com> 1.3.0-1mdk
- first release for mandrakesoft
