Name:		xmr-stak
Version:	2.2.0
Release:	0.1
Summary:	Monero/Aeon All-in-One Mining Software
Url:		https://github.com/fireice-uk/xmr-stak
Group:		Office
License:	GPLv3
Source0:	%name-%version.tar.gz
Source1:	xmr-stak.service

BuildRequires: hwloc-devel libmicrohttpd-devel libstdc++-static  openssl-devel cmake

%description
XMR-Stak is a universal Stratum pool miner. This miner version supports at this time only CPUs and can be used to mine the crypto currency Monero and Aeon.

%package server
Summary:             xmr-stak server common files
Group:               Applications/Internet
BuildArch:           noarch
Requires:            %{name} = %{version}-%{release}
Requires(pre):       shadow-utils
Requires(post):      systemd
Requires(preun):     systemd
Requires(postun):    systemd

%description server
Xmr-stak server common files


%prep
%setup -n %name-%version

%build
%cmake		\
		-DCUDA_ENABLE=OFF \
		-DOpenCL_ENABLE=OFF 

%make_build

%install
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}
#install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/xmr-stak.service
%make_install


%files
%doc LICENSE README.md 
%_bindir/*

%files server
%{_unitdir}/xmr-stak.service

%pre server
getent group xmr-stak > /dev/null || groupadd -r xmr-stak
getent passwd xmr-stak > /dev/null || \
    useradd -r -g xmr-stak -d %{_sharedstatedir}/xmr-stak -s /sbin/nologin \
    -c "Monero mining service" zmr-stak
:

%post server
%systemd_post xmr-stak.service

%preun server
%systemd_preun xmr-stak.service

%postun server
%systemd_postun_with_restart xmr-stak.service


%changelog
* Thu Mar 08 2018 Placentiusz <placentiusz@gmail.com> - 2.2.0-0.1
- Initial release placentiusz()gmail.com

