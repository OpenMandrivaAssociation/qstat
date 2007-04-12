Summary:        Real-time Game Server Status for FPP/FPS servers
Name:           qstat
Version:        2.11
Release:        %mkrel 1
License:        Artistic
Group:          Networking/Other
URL:            http://sourceforge.net/projects/qstat/
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-root

%description
QStat is a command-line utility for collecting real-time 
statistics from on-line game servers. The games supported 
are generally limited to the first-person-shooter genre 
(Quake, Half-Life, Unreal, etc). 
Statistics may be output in a variety of form

%prep

%setup -q %{name}-%{version}

%build

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

mv %{buildroot}%{_bindir}/qstat %{buildroot}%{_bindir}/qstat-quake

rm -f template/Makefile*

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc CHANGES.txt COMPILE.txt ChangeLog contrib.cfg info/* qstatdoc.html template
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/qstat.cfg
%attr(0755,root,root) %{_bindir}/qstat-quake

