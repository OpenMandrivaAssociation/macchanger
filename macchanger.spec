%define	name	macchanger 
%define	version	1.5.0
%define release	%mkrel 6
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

%post
%_install_info %{name}.info

%postun
%_remove_install_info %{name}.info

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
