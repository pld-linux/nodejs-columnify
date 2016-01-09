%define		pkg	columnify
Summary:	Render data in text columns, supports in-column text-wrap
Name:		nodejs-%{pkg}
Version:	1.1.0
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	d94392009e452f597b1d66355e60291b
URL:		https://github.com/timoxley/columnify
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
