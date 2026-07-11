%global tl_name uptex-base
%global tl_revision 77840

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Plain TeX formats and documents for upTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/jptex/generic/uptex-base
License:	bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uptex-base.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uptex-base.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle contains plain TeX format files and documents for upTeX and
e-upTeX.

