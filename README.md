# GML - Get My LiDAR !

**GML** est un outil permettant de télécharger facilement un ensemble de dalles LiDAR HD de l'IGN d'un même bloc. 

1. [Télécharger GML pour votre OS](#Télécharger-GML-pour-votre-OS)
2. [Comment utiliser GML](#How-to-use-GML)
3. [Instructions pour exécuter GML depuis le code source](#Instructions-to-build-GML-from-sources)

## Télécharger GML pour votre OS

- [GML installer for Windows 10](https://sourceforge.net/projects/get-my-lidar/files/GML_22-07.exe/download)
- [GML portable for Windows 10](https://sourceforge.net/projects/get-my-lidar/files/GML_22-07.zip/download)

## How to use GML

Work in progress...

## Instructions to build GML from sources

The easiest way to build **GML** from sources is to use *Conda*.

1. Install *Conda* for your operating system: [miniconda](https://docs.conda.io/en/latest/miniconda.html)
2. Download *GML main repository* : [GML-main](https://github.com/clementroussel/GML/archive/refs/heads/main.zip)
3. Unzip the archive and keep only the *src* and *requirements* folders
4. Open a *Conda Powershell Prompt* and move to the **GML** directory
5. Create and activate a virtual environment dedicated to **GML**:

    ```conda create --name gml-venv python=3.6```  
    ```conda activate gml-venv```

6. Install the required modules:

    ```pip install -r requirements/base.txt```

7. Run **gml**:

    ```fbs run```

### About *fbs*

To learn more about *fbs* module, visit https://build-system.fman.io/.