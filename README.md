# Day-night-plasma-wallpapers
KDE Plasma utility to automatically change to a night wallpaper when the sun is reaching sunset.

#### Demos
![Demos 1](https://github.com/SCOTT-HAMILTON/Ressources/raw/master/Day-night-plasma-wallpapers/demos/demos1.gif)

# What is this ?
Day-night-plasma-wallpapers lets you configure the wallpapers you want for the day and those
you want when working at night.

# Requirements
 - A plasma 5 desktop environment
 - qdbus (in qttools package)

# Configuration
 - Create the directories Night and Light in ~/.local/share/wallpapers
 - Put your day wallpaper in ~/.local/share/wallapers/Light
 - Put you night wallpaper in ~/.local/share/wallpapers/Night

# Installing (Nix or NixOS only)
## Home-manager setup (recommanded)
It is recommanded to use the home-manager setup as it's the easiest.

The first thing to add to your home.nix file is to import the the nur-no-packages repo : 
```nix
let
  home-manager = builtins.fetchGit {
    url = "https://github.com/rycee/home-manager.git";
    rev = "dd94a849df69fe62fe2cb23a74c2b9330f1189ed"; # CHANGEME 
    ref = "release-18.09";
  };
  nur-no-pkgs = import (builtins.fetchTarball {
    url = "https://github.com/nix-community/NUR/archive/master.tar.gz";
    sha256 = "18wa9n11p8wa9zh07p04rk90arld8155mzbcrx3bwfl42fcvha4m" ;
  }) {};
in
{
}
```

Next you need to add the day-night-plasma-wallpapers module : this is 
what links the package's service file and autostart script to your home directory.

```nix
  imports = [
    nur-no-pkgs.repos.shamilton.modules.home-manager.day-night-plasma-wallpapers 
  ];
```
Now you need to install the day-night-plasma-wallpapers package.

```nix
  # This is needed to install nur packages see https://github.com/nix-community/nur#installation
  nixpkgs.config.packageOverrides = pkgs: {
    nur = import (builtins.fetchTarball "https://github.com/nix-community/NUR/archive/master.tar.gz") {
      inherit pkgs;
    };
  };
	
  # Here we install the day-night-plasma-wallpapers package
  # (or derivation should I say), from my repository
  home.packages = [
    nur.repos.shamilton.day-night-plasma-wallpapers 
  ];

```
Lastly you can enable the service with : 

```nix
services.day-night-plasma-wallpapers.enable = true;
```

Here is an overview of what a minimal home.nix file looks like : 
```nix
{ pkgs ? import <nixpkgs>{}
, ... }:

with builtins;
with lib;
with pkgs;

let
  home-manager = builtins.fetchGit {
    url = "https://github.com/rycee/home-manager.git";
    rev = "dd94a849df69fe62fe2cb23a74c2b9330f1189ed"; # CHANGEME 
    ref = "release-18.09";
  };
  nur-no-pkgs = import (builtins.fetchTarball {
    url = "https://github.com/nix-community/NUR/archive/master.tar.gz";
    sha256 = "18wa9n11p8wa9zh07p04rk90arld8155mzbcrx3bwfl42fcvha4m" ;
  }) {};
in
{
  imports = [
    nur-no-pkgs.repos.shamilton.modules.home-manager.day-night-plasma-wallpapers 
  ];
  
  nixpkgs.config.packageOverrides = pkgs: {
    nur = import (builtins.fetchTarball "https://github.com/nix-community/NUR/archive/master.tar.gz") {
      inherit pkgs;
    };
  };

  home.packages = [
    nur.repos.shamilton.day-night-plasma-wallpapers 
  ];

  services.day-night-plasma-wallpapers.enable = true;
}
```

# TODO
 * Make a configuration system
 * Make a GUI for the configuration
 * Package for other distros
 * Convert the script to native code
 * Find another solution than sleeping for 10 seconds before running the script : 
	This sleep is the only solution found to be able to use qdbus after session boot with ~/.config/autostart-script script
 * Manage multiple wallpapers

# Recommandations
This package works well with the macMojave desert wall papers : 
[MacMojave day wallpaper](https://github.com/SCOTT-HAMILTON/Ressources/raw/master/Day-night-plasma-wallpapers/macMojaveWallPapers/macOS-Mojave-Day-wallpaper.jpg)
[MacMojave night wallpaper](https://github.com/SCOTT-HAMILTON/Ressources/blob/master/Day-night-plasma-wallpapers/macMojaveWallPapers/macOS-Mojave-Night-wallpaper.jpg)
