# -*- mode: python -*-

block_cipher = None


a = Analysis(['pyxida_gui.py'],
             pathex=['D:\\Workspace\\PycharmProjects\\PyxidaAuebDissertationsScraper'],
             binaries=[],
             datas=[('img\\compass.png', 'img'), ('img\\help.png', 'img')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['tk'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='pyxida_gui',
          debug=False,
          strip=False,
          upx=True,
          console=True, icon='img\\compass.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='pyxida_gui')
