Summary: Reverse Proxy Add Forward module for Apache
Name: mod_rpaf
Version: 0.6
Release: 1
License: Apache
Group: System Environment/Daemons
URL: https://github.com/gnif/mod_rpaf
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: httpd-devel
Requires: httpd httpd-devel

%description
rpaf is for backend Apache servers what mod_proxy_add_forward is for
frontend Apache servers. It does excactly the opposite of
mod_proxy_add_forward written by Ask Bjørn Hansen. It will also work
with mod_proxy that is distributed with Apache2 from version 2.0.36.

%prep
%setup -q

%build
make rpaf

%install
rm -rf $RPM_BUILD_ROOT
install -m0755 -d $RPM_BUILD_ROOT$(apxs -q LIBEXECDIR)
make DESTDIR=$RPM_BUILD_ROOT install
install -m0644 -D rpaf.conf $RPM_BUILD_ROOT/etc/httpd/conf.d/rpaf.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/httpd/modules/mod_rpaf-2.0.so
%config(noreplace) %{_sysconfdir}/httpd/conf.d/rpaf.conf

%post
/usr/sbin/apxs -e -A -n rpaf $(apxs -q LIBEXECDIR)/mod_rpaf-2.0.so

%preun
/usr/sbin/apxs -e -A -n rpaf $(apxs -q LIBEXECDIR)/mod_rpaf-2.0.so


%changelog
* Sun Aug 19 2012 Kentaro Yoshida <y.ken.studio@gmail.com>
- improbe forward compatibility
* Mon Oct 17 2011 Ben Walton <bwalton@artsci.utoronto.ca>
- Initial spec file creation
