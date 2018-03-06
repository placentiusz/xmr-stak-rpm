Name:		xmr-stak
Version:	2.2.0
Release:	0.1
Summary:	Monero/Aeon All-in-One Mining Software
Url:		https://github.com/fireice-uk/xmr-stak
Group:		Office
License:	GPLv3
Source0:	%name-%version.tar.gz


BuildRequires: hwloc-devel libmicrohttpd-devel libstdc++-static  openssl-devel cmake

%description
XMR-Stak is a universal Stratum pool miner. This miner version supports at this time only CPUs and can be used to mine the crypto currency Monero and Aeon.

%prep
%setup -n %name-%version

%build
%cmake		\
		-DCUDA_ENABLE=OFF \
		-DOpenCL_ENABLE=OFF 

%make_build

%install
%make_install


%files
%doc LICENSE README.md 
%_bindir/*

%changelog
-Initial release placentiusz()gmail.com

