Summary:        Real-time Game Server Status for FPP/FPS servers
Name:           qstat
Version:        2.11
Release:        7
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


%changelog
* Tue Sep 15 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.11-6mdv2010.0
+ Revision: 442594
- rebuild

* Sat Mar 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2.11-5mdv2009.1
+ Revision: 355014
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.11-4mdv2009.0
+ Revision: 269055
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.11-3mdv2009.0
+ Revision: 194507
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.11-2mdv2008.1
+ Revision: 140742
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 14 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.11-2mdv2008.0
+ Revision: 85636
- spec file clean
- use program-suffix rather that rename binary


* Sun Dec 31 2006 Tomasz Pawel Gajc <tpg@mandriva.org> 2.11-1mdv2007.0
+ Revision: 102903
- Import qstat

