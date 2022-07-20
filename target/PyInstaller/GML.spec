# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\clement\\Documents\\GitHub\\GML\\src\\main\\python\\main.py'],
             pathex=['C:\\Users\\clement\\Documents\\GitHub\\GML\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['C:\\Users\\clement\\miniconda3\\envs\\gml-venv\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['C:\\Users\\clement\\Documents\\GitHub\\GML\\target\\PyInstaller\\fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='GML',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True , version='C:\\Users\\clement\\Documents\\GitHub\\GML\\target\\PyInstaller\\version_info.py', icon='C:\\Users\\clement\\Documents\\GitHub\\GML\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='GML')
