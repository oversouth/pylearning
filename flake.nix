{
  description = "Pylearning";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          zlib
          stdenv.cc.cc.lib
          SDL2
          SDL2_image
          SDL2_mixer
          SDL2_ttf
          (python3.withPackages (ps: with ps; [
            telethon
            pygame
            colorama
          ]))
        ];

        shellHook = ''
          export LD_LIBRARY_PATH="${pkgs.lib.makeLibraryPath [
            pkgs.zlib
            pkgs.stdenv.cc.cc.lib
            pkgs.SDL2
            pkgs.SDL2_ttf
          ]}:$LD_LIBRARY_PATH"
          echo "🚀 Python environment (Telethon, Pygame, Colorama) loaded!"
        '';
      };
    };
}
