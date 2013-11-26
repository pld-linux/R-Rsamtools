%define		packname	Rsamtools

Summary:	Binary alignment (BAM), variant call (BCF), or tabix file import
Name:		R-%{packname}
Version:	1.12.4
Release:	1
License:	Artistic 2.0
Group:		Applications/Math
Source0:	http://www.bioconductor.org/packages/2.12/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	75189a4203fb3eb9bd8cda03f3e8c523
Patch0:		bogus-deps.patch
URL:		http://www.bioconductor.org/packages/2.12/bioc/html/Rsamtools.html
BuildRequires:	R
BuildRequires:	R-IRanges-devel >= 1.15.35
BuildRequires:	R-GenomicRanges >= 1.11.38
BuildRequires:	R-Biostrings-devel >= 2.25.6
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-IRanges >= 1.17.33
Requires:	R-GenomicRanges >= 1.11.38
Requires:	R-Biostrings >= 2.25.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides an interface to the 'samtools', 'bcftools',
and 'tabix' utilities (see 'LICENCE') for manipulating SAM (Sequence
Alignment / Map), binary variant call (BCF) and compressed indexed
tab-delimited (tabix) files.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -c -n %{packname}
%patch0 -p1

%build
# circular dep on R-Rsamtools
#{_bindir}/R CMD build %{packname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/doc/
%doc %{_libdir}/R/library/%{packname}/html/
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/LICENSE
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/extdata/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/scripts/
%{_libdir}/R/library/%{packname}/unitTests/
%{_libdir}/R/library/%{packname}/libs/

%files devel
%defattr(644,root,root,755)
%{_libdir}/R/library/%{packname}/include
%{_libdir}/R/library/%{packname}/usretc
%{_libdir}/R/library/%{packname}/usrlib
