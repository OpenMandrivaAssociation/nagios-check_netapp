Summary:	Check Network Appliance (NetApp) filers
Name:		nagios-check_netapp
Version:	20060619
Release:	5
Group:		Networking/Other
License:	BSD
URL:		https://nerhood.homeip.net/wordpress/archives/2006/06/19/monitoring-netapp-with-nagios-and-nagiosgraph/
Source0:	http://nerhood.homeip.net/code/check_netapp
BuildArch:  noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Use this plugin with Nagios to check Network Appliance (NetApp) filers.

%prep

%build

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/nagios/plugins
install -m 755 %{SOURCE0} %{buildroot}%{_datadir}/nagios/plugins

perl -pi -e 's|/usr/local/nagios/libexec|%{_datadir}/nagios/plugins|' \
    %{buildroot}%{_datadir}/nagios/plugins/check_netapp

install -d -m 755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
cat > %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_netapp.cfg <<'EOF'
define command{
	command_name	check_netapp
	command_line	%{_datadir}/nagios/plugins/check_netapp -H $HOSTADDRESS$
}
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/nagios/plugins/check_netapp
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_netapp.cfg


%changelog
* Sat Dec 11 2010 Oden Eriksson <oeriksson@mandriva.com> 20060619-4mdv2011.0
+ Revision: 620461
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 20060619-3mdv2010.0
+ Revision: 440218
- rebuild

* Mon Dec 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20060619-2mdv2009.1
+ Revision: 314638
- now a noarch package

  + Oden Eriksson <oeriksson@mandriva.com>
    - this is no noarch package

* Fri Feb 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20060619-1mdv2008.1
+ Revision: 176824
- import nagios-check_netapp


* Fri Feb 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20060619-1mdv2008.1
- first mdv release
