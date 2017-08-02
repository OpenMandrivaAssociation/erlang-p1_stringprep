%global srcname p1_stringprep
# Erlang packages don't seem to ship debug files, as the build process does not generate them
%global debug_package %{nil}


Name: erlang-%{srcname}
Version: 1.0.0
Release: %mkrel 2
Group:   Development/Erlang
Summary: A framework for preparing Unicode strings to help input and comparison
License: ASL 2.0 and TCL
URL: https://github.com/processone/stringprep/
Source0: https://github.com/processone/stringprep/archive/%{version}.tar.gz

Requires: erlang-erts
Requires: erlang-p1_utils
BuildRequires: erlang-rebar
BuildRequires: erlang-rpm-macros
BuildRequires: erlang-eunit
BuildRequires: erlang-p1_utils


%description
Stringprep is a framework for preparing Unicode test strings in order to
increase the likelihood that string input and string comparison work. The
principle are defined in RFC-3454: Preparation of Internationalized Strings.
This library is leverage Erlang native NIF mechanism to provide extremely fast
and efficient processing.


%prep
%autosetup -n stringprep-%{version}


%build
%rebar_compile


%install
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/ebin
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib

install -pm644 ebin/* $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/ebin/
install -pm755 priv/lib/* $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/

%files
%license LICENSE.txt LICENSE.TCL LICENSE.ALL
%doc README.md
%{_erllibdir}/%{srcname}-%{version}



%changelog
* Fri May 06 2016 neoclust <neoclust> 1.0.0-2.mga6
+ Revision: 1009922
- imported package erlang-p1_stringprep

