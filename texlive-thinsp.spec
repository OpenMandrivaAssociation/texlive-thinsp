# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/thinsp
# catalog-date 2008-08-24 14:46:50 +0200
# catalog-license gpl
# catalog-version 0.1
Name:		texlive-thinsp
Version:	0.1
Release:	1
Summary:	A stretchable \thinspace for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/thinsp
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thinsp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thinsp.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package redefines \thinspace to have a stretch component.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/thinsp/thinsp.sty
%doc %{_texmfdistdir}/doc/latex/thinsp/COPYIRIGHT
%doc %{_texmfdistdir}/doc/latex/thinsp/README
%doc %{_texmfdistdir}/doc/latex/thinsp/thinsp.pdf
%doc %{_texmfdistdir}/doc/latex/thinsp/thinsp.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
