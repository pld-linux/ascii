Name: ascii
Version: 2.6
Release: 1
Source: locke.ccil.org:/pub/esr/ascii-2.6.tar.gz
Copyright: distributable
Group: Utilities/Text
Summary: interactive ASCII name and synonym chart

%description
The ascii utility provides easy conversion between various byte representations
and the American Standard Code for Information Interchange (ASCII) character
table.  It knows about a wide variety of hex, binary, octal, Teletype mnemonic,
ISO/ECMA code point, slang name, and other representations.  Given any one on
the command line, it will try to display all others.  Called with no arguments
it displays a handy small ASCII chart.

%prep
%setup

%build
make

%install
rm -f /usr/bin/ascii
cp ascii /usr/bin
cp ascii.1 /usr/man/man1/ascii.1

%files
/usr/man/man1/ascii.1
/usr/bin/ascii
