Name:           python-compas
Version:        1.15.1
Release:        1%{?dist}
Summary:        The COMPAS framework

License:        MIT
URL:            https://github.com/compas-dev/compas
Source:         %{url}/archive/v%{version}/compas-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
Suggests: python3-compas+extras

%global _description %{expand:
The COMPAS framework is an open-source, Python-based framework for computational
research and collaboration in architecture, engineering, digital fabrication and
construction.

The framework consists of a general-purpose core library, written in pure
Python, and a growing collection of extensions that provide easy access to
peer-reviewed research, state-of-the-art external libraries such as CGAL, libigl
and Triangle, and tools with specialized functionality for AEFC applications
such as Abaqus, ANSYS, SOFISTIK, ROS, etc.

COMPAS has dedicated packages for working with Rhino, Grasshopper, and Blender,
but it can be used in any environment that supports Python scripting. It is
available on PyPI and conda-forge and can be easily installed using popular
package managers on multiple platforms.}

%description %_description

%package -n python3-compas
Summary:        %{summary}

%description -n python3-compas %_description

%pyproject_extras_subpkg -n python3-compas extras

%prep
%autosetup -p1 -n compas-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files compas compas_blender compas_ghpython compas_plotters compas_rhino

%check

%pytest tests

%files -n python3-compas -f %{pyproject_files}
%doc README.md
%{_bindir}/compas_rpc

%changelog
* Thu Jun 16 2022 Anton Tetov <anton@tetov.se> - 1.15.1-1
- Initial package.
