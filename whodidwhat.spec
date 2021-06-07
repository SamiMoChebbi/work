# 
# whodidwhat spec file
#

Name: whodidwhat
Summary: Traceability for user commands 
Version: 2.1.0
License: AGPLv3
Release: 1%{?dist}
Group: CERN-IT/ST
BuildArch: x86_64
Source: %{name}-%{version}.tar.gz

# The required Python version makes this package depend on Fedora 29 or similar recent distros to compile and run.
BuildRequires: python(abi) >= 3.6
Requires: python(abi) >= 3.6
# The following to avoid to pick up /bin/python as an automatic dependency
AutoReq: no

%description
This RPM provides the whodidwhat command for traceability for user commands 

# Don't do any post-install weirdness, especially compiling .py files
#define __os_install_post %{nil}

%prep
%setup -n %{name}-%{version}

%install
# server versioning

# installation
rm -rf %buildroot/
mkdir -p %buildroot/usr/local/sbin
mkdir -p %buildroot/etc/profile.d
install -m 755 whodidwhatV2.py	     %buildroot/usr/local/sbin/whodidwhat
install -m 755 whodidwhat.profile.sh    %buildroot/etc/profile.d

%post
pip3 install columnar

%files
%defattr(-,root,root,-)
/usr/local/sbin/whodidwhat
/etc/profile.d/whodidwhat.profile.sh


%changelog
* Mon Jun 7 2021 Sami Mohamed Chebbi <sami.mohamed.chebbi@cern.ch> 2.1.0
- Resolve crash problems
* Thu Jun 3 2021 Sami Mohamed Chebbi <sami.mohamed.chebbi@cern.ch> 2.0.0
- Python implementation of whodidwhat to fix major issues
- Add user, to and from filters
* Thu Feb 25 2021 Sami Mohamed Chebbi <sami.mohamed.chebbi@cern.ch> 1.0.0
- First Version of whodidwhat
