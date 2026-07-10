%global tl_name drm
%global tl_revision 38157

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.4
Release:	%{tl_revision}.1
Summary:	A complete family of fonts written in Metafont
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/drm
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/drm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/drm.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/drm.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides access to the DRM (Don's Revised Modern) family of
fonts, which includes a variety of optical sizes in Roman (in four
weights), italic, and small caps, among other shapes, along with a set
of symbols and ornaments. It is intended to be a full-body text font,
but its larger sizes can also be used for simple display purposes, and
its significant body of symbols can stand on its own. It comes complete
with textual ("old-style") and lining figures, and even has small-caps
figures. It also comes with extensible decorative rules to be used with
ornaments from itself or other fonts, along with an extremely flexible
ellipsis package.

