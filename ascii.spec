Summary:	Interactive ASCII name and synonym chart
Summary(pl.UTF-8):	Interaktywna tablica kodów i synonimów ASCII
Name:		ascii
Version:	3.30
Release:	1
License:	BSD
Group:		Applications/Text
Source0:	http://www.catb.org/~esr/ascii/%{name}-%{version}.tar.gz
# Source0-md5:	6268c89a81638c7a6ce9101de6046c93
URL:		http://www.catb.org/~esr/ascii/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ascii utility provides easy conversion between various byte
representations and the American Standard Code for Information
Interchange (ASCII) character table. It knows about a wide variety of
hex, binary, octal, Teletype mnemonic, ISO/ECMA code point, slang
name, and other representations. Given any one on the command line, it
will try to display all others. Called with no arguments it displays a
handy small ASCII chart.

%description -l pl.UTF-8
Program ascii umożliwia łatwą konwersję pomiędzy tablicą znaków ASCII
i ich różnymi odpowiednikami w postaci heksadecymalnej, binarnej,
oktalnej, Teletype mnemonic, ISO/ECMA, nazw potocznych, etc.
Jakikolwiek z nich podany w linii poleceń spowoduje wyświetlenie
pozostałych odpowiedników. Wywołany bez argumentów wyświetla poręczny
zestaw znaków ASCII.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install ascii $RPM_BUILD_ROOT%{_bindir}
cp -p ascii.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS.adoc README
%attr(755,root,root) %{_bindir}/ascii
%{_mandir}/man1/ascii.1*
