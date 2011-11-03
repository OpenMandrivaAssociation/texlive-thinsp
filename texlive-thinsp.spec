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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package redefines \thinspace to have a stretch component.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/thinsp/thinsp.sty
%doc %{_texmfdistdir}/doc/latex/thinsp/COPYIRIGHT
%doc %{_texmfdistdir}/doc/latex/thinsp/README
%doc %{_texmfdistdir}/doc/latex/thinsp/thinsp.pdf
%doc %{_texmfdistdir}/doc/latex/thinsp/thinsp.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
