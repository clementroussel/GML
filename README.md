# GML - Get My LiDAR !

**GML** is a simple but useful tool to easily download multiple IGN LiDAR HD tiles of a same block.

[Instructions to build **GML** from sources](#Instructions-to-build-GML-from-sources)

## Instructions to build GML from sources

The easiest way to build *GML** from sources is to use *Conda*.

1. Install *Conda* for your operating system: [miniconda](https://docs.conda.io/en/latest/miniconda.html)
2. Download *pyLong main repository* : [GML-main](https://github.com/clementroussel/GML/archive/refs/heads/main.zip)
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