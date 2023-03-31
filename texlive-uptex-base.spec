Name:		texlive-uptex-base
Version:	64072
Release:	2
Summary:	Plain TeX formats and documents for upTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uptex-base
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uptex-base.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uptex-base.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle contains plain TeX format files and documents for
upTeX and and e-upTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/uptex/uptex-base
%doc %{_texmfdistdir}/doc/uptex/uptex-base

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
