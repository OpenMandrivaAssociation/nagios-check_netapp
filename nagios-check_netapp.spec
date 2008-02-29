%define name	nagios-check_netapp
%define version	20060619
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Check Network Appliance (NetApp) filers
Group:		Networking/Other
License:	BSD
URL:		http://nerhood.homeip.net/wordpress/archives/2006/06/19/monitoring-netapp-with-nagios-and-nagiosgraph/
Source0:	http://nerhood.homeip.net/code/check_netapp
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Use this plugin with Nagios to check Network Appliance (NetApp) filers.

%prep

%build


%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_libdir}/nagios/plugins
install -m 755 %{SOURCE0} %{buildroot}%{_libdir}/nagios/plugins

install -d -m 755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
cat > %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_netapp.cfg <<'EOF'
define command{
	command_name	check_netapp
	command_line	%{_libdir}/nagios/plugins/check_netapp -H $HOSTADDRESS$
}
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_netapp
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_netapp.cfg

