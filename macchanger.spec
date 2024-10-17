%define	lib_name_orig	lib%{name}
%define	lib_major	0
%define	lib_name	%mklibname %{name} %{lib_major}

Name:           macchanger
Summary: 	Uility for viewing/manipulating the MAC address of network interfaces
Group:		System/Configuration/Networking
Version:        1.7.0
Release:        1
License:	GPL 
URL:		https://www.alobbs.com/macchanger/
Source:         %{name}-%{version}.tar.gz


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
%makeinstall



%clean

%files
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/*
%{_infodir}/%{name}.info*
%defattr(755,root,root,755)
%{_bindir}/*