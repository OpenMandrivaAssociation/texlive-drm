Name:		texlive-drm
Version:	38157
Release:	2
Summary:	A complete family of fonts written in Metafont
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/drm
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/drm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/drm.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/drm.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides access to the DRM (Don's Revised Modern)
family of fonts, which includes a variety of optical sizes in
Roman (in four weights), italic, and small caps, among other
shapes, along with a set of symbols and ornaments. It is
intended to be a full-body text font, but its larger sizes can
also be used for simple display purposes, and its significant
body of symbols can stand on its own. It comes complete with
textual ("old-style") and lining figures, and even has
small-caps figures. It also comes with extensible decorative
rules to be used with ornaments from itself or other fonts,
along with an extremely flexible ellipsis package.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/fonts/drm
%{_texmfdistdir}/tex/latex/drm
%{_texmfdistdir}/fonts/type1/public/drm
%{_texmfdistdir}/fonts/tfm/public/drm
%doc %{_texmfdistdir}/fonts/source/public/drm
%{_texmfdistdir}/fonts/opentype/public/drm
%{_texmfdistdir}/fonts/map/dvips/drm
%{_texmfdistdir}/fonts/afm/public/drm
%doc %{_texmfdistdir}/doc/fonts/drm

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
