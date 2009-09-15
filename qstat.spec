Summary:        Real-time Game Server Status for FPP/FPS servers
Name:           qstat
Version:        2.11
Release:        %mkrel 6
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

%configure2_5x --program-suffix=-quake

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

rm -f template/Makefile*

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES.txt COMPILE.txt ChangeLog contrib.cfg info/* qstatdoc.html template
%config(noreplace) %{_sysconfdir}/qstat.cfg
%{_bindir}/%{name}-quake
