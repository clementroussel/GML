# GML - Get My LiDAR !

<div id="header" align="center">
  <img src="gml_icon.png" width="48"/>
</div>

---

**GML** est un outil permettant de télécharger facilement un ensemble de dalles LiDAR HD de l'IGN appartenant à un même bloc. 

1. [Télécharger GML](#Télécharger-GML)
2. [Comment utiliser GML](#Comment-utiliser-GML)
3. [Instructions pour exécuter GML depuis le code source](#Instructions-pour-exécuter-GML-depuis-le-code-source)

## Télécharger GML

- [Installateur pour Windows 10](https://sourceforge.net/projects/get-my-lidar/files/GML_22-07.exe/download)
- [Version portable for Windows 10](https://sourceforge.net/projects/get-my-lidar/files/GML_22-07.zip/download)

## Comment utiliser GML

L'url de téléchargement d'une dalle LiDAR HD de l'IGN ressemble à ceci:
`https://wxs.ign.fr/c90xknypoz1flvgojchbphgt/telechargement/prepackage/LIDARHD_PACK_PM_2021$LIDARHD_1-0_LAZ_PM-0916_6463-2021/file/LIDARHD_1-0_LAZ_PM-0916_6463-2021.7z`

<div id="header" align="center">
  <img src="gml_screenshot.png" width="800"/>
</div>

- Configurez les différents champs pour construire l'url d'accès aux données.
- Choississez le répertoire où seront écrites les données téléchargées.
- Lancez le téléchargement avec la commande **Get My LiDAR !**.
- Si certains téléchargements ont échoués, vous pouvez relancer le téléchargement des fichiers manquants avec la commande **Try again !**.
- La commande **Print downloaded file(s) name(s)** permet d'afficher le nom des fichiers téléchargés.
- La commande **Print empty url(s)** permet d'afficher l'url des fichiers non téléchargés.

## Instructions pour exécuter GML depuis le code source

1. Installez *Conda* pour votre système d'exploitation: [miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. Téléchargez le code source de **GML** : [GML-main](https://github.com/clementroussel/GML/archive/refs/heads/main.zip).
3. Décompressez l'archive et gardez uniquement les répertoires *src* et *requirements*.
4. Ouvrez *Conda Powershell Prompt* et déplacez vous dans le répertoire *GML-main*.
5. Créez et activer un environnement virtuel dédié à **GML**:

    ```conda create --name gml python=3.6```  
    ```conda activate gml```

6. Installez les dépendances du projet:

    ```pip install -r requirements/base.txt```

7. Lancez **gml**:

    ```fbs run```