Name:       scopebuddy
Version:    1.3.0
Release:    1%{?dist}
Summary:    Manager script for gamescope
License:    Apache-2.0

# NOTE: The "/usr/bin/env bash" shebang in scopebuddy is automatically
#       converted to "/usr/bin/bash" when packaged as an rpm.
#          https://docs.fedoraproject.org/en-US/packaging-guidelines/#_shebang_lines

Requires:   bash
Requires:   gamescope
Requires:   perl
Recommends: jq
Recommends: (kscreen if plasma-desktop)
# TODO: if GNOME is installed, make sure gdctl has --format=json support,
#       if not then either install a version that does or install gnome-randr

BuildArch:  noarch
URL:        https://github.com/HikariKnight/ScopeBuddy
Source0:    %{name}-%{version}.tar.gz

%description
A manager script to make gamescope easier to use on desktop.

%prep
%autosetup -n ScopeBuddy-main

%build
# nothing to build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{SOURCE0} %{buildroot}%{_bindir}/scopebuddy
ln -s scopebuddy %{buildroot}%{_bindir}/scb

%files
%{_bindir}/scopebuddy
%{_bindir}/scb
#TODO: fedora packaging guidelines recommend man pages to be included

%changelog
* Wed Dec 17 2025 Robert French <frenchrobertm@outlook.com> 1.3.0-1
- new package built with tito

* Wed Dec 17 2025 Robert French <frenchrobertm@outlook.com>
- new package built with tito

%autochangelog
