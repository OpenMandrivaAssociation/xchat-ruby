%define name	xchat-ruby
%define version	1.1
%define release	%mkrel 8

# usually ruby binary compatibility only breaks between minor releases?
%define min_ruby_version	1.8
%define max_ruby_version	1.9

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	XChat Ruby plugin
Group:		Networking/IRC
License:	GPL
URL:		http://xchat-ruby.sourceforge.net/

Source:		%{name}-src-%{version}.tar.bz2
Patch0:		%{name}-global-install.patch
BuildRequires:	ruby-devel >= %{min_ruby_version}
BuildConflicts:	ruby-devel >= %{max_ruby_version}
Requires:	ruby >= %{min_ruby_version}
Conflicts:	ruby >= %{max_ruby_version}
Requires:	xchat

%description
Provides Ruby scripting capability to XChat.

%prep
%setup -q -n %{name}-src-%{version}
%patch0

%build
cd src
%make CFLAGS='-fPIC -Wall %optflags'

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/xchat/plugins/
install -m 755 src/xchat-ruby.so $RPM_BUILD_ROOT%{_libdir}/xchat/plugins/ruby.so
ruby -e 'puts $LOAD_PATH.join("\n")' > $RPM_BUILD_ROOT%{_libdir}/xchat/plugins/rubyenv

%clean
rm -fr $RPM_BUILD_ROOT


%files 
%defattr(-,root,root)
%doc README COPYING samples ChangeLog
%{_libdir}/xchat/plugins/ruby.so
%{_libdir}/xchat/plugins/rubyenv


