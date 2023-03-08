from PyPDF2 import PdfMerger
from time import sleep
import os
from sys import argv


string = """
$$  __$$\ $$  __$$\ $$  _____|      $$$\    $$$ |$$  _____|$$  __$$\ $$  __$$\ $$  _____|$$  __$$\ 
$$ |  $$ |$$ |  $$ |$$ |            $$$$\  $$$$ |$$ |      $$ |  $$ |$$ /  \__|$$ |      $$ |  $$ |
$$$$$$$  |$$ |  $$ |$$$$$\          $$\$$\$$ $$ |$$$$$\    $$$$$$$  |$$ |$$$$\ $$$$$\    $$$$$$$  |
$$  ____/ $$ |  $$ |$$  __|         $$ \$$$  $$ |$$  __|   $$  __$$< $$ |\_$$ |$$  __|   $$  __$$< 
$$ |      $$ |  $$ |$$ |            $$ |\$  /$$ |$$ |      $$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |
$$ |      $$$$$$$  |$$ |            $$ | \_/ $$ |$$$$$$$$\ $$ |  $$ |\$$$$$$  |$$$$$$$$\ $$ |  $$ |
\__|      \_______/ \__|            \__|     \__|\________|\__|  \__| \______/ \________|\__|  \__|
"""


print(string)

print(argv)
if len(argv) <= 1:
    print('No target directory was specified!')
    print('Please call the program as follows -> pdf_merger <path to folder>')
    print('Press enter to continue...')
    input()
    exit(0)

if os.path.isfile(f'{argv[1]}\merged-pdf.pdf'):
    print('Merged file already exists on current directory...')
    print('Press enter to continue...')
    input()
    exit(0)

merger = PdfMerger()
for file in os.listdir(argv[1]):
    if file.endswith('.pdf'):
        path = f'{argv[1]}\{file}'
        print(f'Merging - {path}...')
        merger.append(path)
print('Files successfully merged!')
try:
    merger.write(f'{argv[1]}\merged-pdf.pdf')
    print(f'Wrote file to {argv[1]}\merged-pdf.pdf')
except Exception as e:
    print(f'Error while trying to Write file to {argv[1]}\merged-pdf.pdf')
    print(f'Exception: {e}')
finally:
    merger.close()
    print('Press enter to continue...')
    input()
    exit(0)
