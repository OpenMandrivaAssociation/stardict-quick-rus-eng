%define	version	2.4.2
%define release %mkrel 8
%define dict_format_version	2.4.2

Summary:	Russian -> English *Quick dictionary for StarDict 2
Name:		stardict-quick-rus-eng
Version:	%{version}
Release:	%{release}
License:	Distributable
Group:		Databases
URL:		http://stardict.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

Source0:	ftp://osdn.dl.sourceforge.net/pub/sourceforge/s/st/stardict/stardict-quick_rus-eng-%{version}.tar.bz2

Provides:	stardict-dictionary = %{dict_format_version}
Requires:	stardict >= %{dict_format_version}

%description
Russian -> English *Quick dictionary in StarDict 2 format.
*Quick is an open source translation application. For more info, visit

http://www.futureware.at/.

%prep
%setup -q -n stardict-quick_rus-eng-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/stardict/dic
install -m 0644 * %{buildroot}%{_datadir}/stardict/dic

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/stardict/dic/*


