%global tl_name thinsp
%global tl_revision 39669

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	A stretchable \thinspace for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/thinsp
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thinsp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thinsp.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package redefines \thinspace to have a stretch component.

