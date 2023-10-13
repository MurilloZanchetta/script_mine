import subprocess as s
import glob as g

pasta_downloads = '/home/murillo/Downloads/'
arquivos_jar = g.glob(pasta_downloads + 'TLauncher-*.jar')

if arquivos_jar:
    caminho_jar = arquivos_jar[0]  

    s.run(['java', '-jar', caminho_jar])