Summary: Package - South Africa Sugar Association wordpress Site
Name: sasa-site
Version: %version
Release: 1
License: Not Applicable
Group: Development/Library
BuildRoot: %{_tmppath}/%{name}-root
Source0: %{name}-%{version}.tar.gz
Requires: php
BuildArch: noarch

%description
South Africa Sugar Association wordpress Site

%prep
%setup -q

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT/home/sites/%{name}
cp -R * $RPM_BUILD_ROOT/home/sites/%{name}

install -d -m 755 $RPM_BUILD_ROOT/home/vhosts
install -m 644 install/sasa-site.conf $RPM_BUILD_ROOT/home/vhosts/sasa-site.conf

%post
rm -f /home/sites/%{name}/install/sasa-site.conf
rmdir /home/sites/%{name}/install

/sbin/service httpd reload

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,apache,apache,-)
/home/sites/%{name}
%config /home/vhosts/sasa-site.conf
