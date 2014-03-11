%define		pkg	columnify
Summary:	Render data in text columns, supports in-column text-wrap
Name:		nodejs-%{pkg}
Version:	0.1.2
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/timoxley/columnify
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	529b3dde5144dfbd24fad26fdd27468d
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Create text-based columns suitable for console output. Supports
minimum and maximum column widths via truncation and text wrapping.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr *.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme.md
%{nodejs_libdir}/%{pkg}
