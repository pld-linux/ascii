Summary:	Interactive ASCII name and synonym chart
Summary(pl):	Interaktywna tablica kod�w i synonim�w ASCII
Name:		ascii
Version:	2.7
Release:	1
Copyright:	distributable
Group:		Utilities/Text
Group(pl):	Narz�dzia/Tekst
Source:		ftp://locke.ccil.org/pub/esr/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ascii utility provides easy conversion between various byte 
representations and the American Standard Code for Information Interchange 
(ASCII) character table.  It knows about a wide variety of hex, binary, 
octal, Teletype mnemonic, ISO/ECMA code point, slang name, and other 
representations.  Given any one on the command line, it will try to display 
all others.  Called with no arguments it displays a handy small ASCII 
chart.   

%description -l pl
Program ascii umo�liwia �atw� konwersj� pomi�dzy tablic� znak�w ASCII i ich 
r�nymi odpowiednikami w postaci heksadecymalnej, binarnej, oktalnej,  
Teletype mnemonic, ISO/ECMA, nazw potocznych, etc. Jakikolwiek z nich  
podany w linii polece� spowoduje wy�wietlenie pozosta�ych odpowiednik�w. 
Wywo�any bez argument�w wy�wietla por�czny zestaw znak�w ASCII.   

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -s ascii $RPM_BUILD_ROOT%{_bindir}
install ascii.1  $RPM_BUILD_ROOT%{_mandir}/man1/ascii.1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/ascii.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ascii
%{_mandir}/man1/*
