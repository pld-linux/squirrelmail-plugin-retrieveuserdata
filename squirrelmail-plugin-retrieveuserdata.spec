%define		_plugin	retrieveuserdata
%define		mversion	1.4.0
Summary:	Plugin for retrieving user data from external sources
Summary(pl.UTF-8):	Wtyczka do pobierania danych użytkowników z zewnętrznych źródeł
Name:		squirrelmail-plugin-%{_plugin}
Version:	0.9
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}.%{version}-%{mversion}.tar.gz
# Source0-md5:	dfe469f7ab473fd2292b30800e3141d5
Patch0:		%{name}-passwd.patch
URL:		http://www.squirrelmail.org/plugin_view.php?id=11
Requires:	squirrelmail >= 1.4.6-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_datadir}/squirrelmail/plugins/%{_plugin}
%define		_sysconfdir	/etc/webapps/squirrelmail

%description
This plugin retrieves the full name and the email address of a
SquirrelMail user from an external source and writes them to the
user's preferences. Your users don't have to enter their name and
email address before they write their first email.

%description -l pl.UTF-8
Ta wtyczka pobiera pełne imię i nazwisko oraz adres email użytkownika
Wiewiórczej Poczty z zewnętrznego źródła i zapisuje je w ustawieniach.
Użytkownicy nie będą musieli wpisywać swoich danych przed wysłaniem
swojego pierwszego maila.

%prep
%setup -q -n %{_plugin}
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir} $RPM_BUILD_ROOT%{_sysconfdir}

mv config.php $RPM_BUILD_ROOT%{_sysconfdir}/%{_plugin}_config.php
install *.php $RPM_BUILD_ROOT%{_plugindir}
ln -s %{_sysconfdir}/%{_plugin}_config.php $RPM_BUILD_ROOT%{_plugindir}/config.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL users_example.txt
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{_plugin}_config.php
%dir %{_plugindir}
%{_plugindir}/*.php
