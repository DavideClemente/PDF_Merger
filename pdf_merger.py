from PyPDF2 import PdfMerger
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

target_dir = " ".join(argv[1:])

if not os.path.exists(target_dir):
    print(f'The specified target directory does not exist: {target_dir}')
    print('Press enter to continue...')
    input()
    exit(0)

merged_pdf_path = os.path.join(target_dir, 'merged-pdf.pdf')

if os.path.isfile(merged_pdf_path):
    print('Merged file already exists on current directory...')
    print('Press enter to continue...')
    input()
    exit(0)

merger = PdfMerger()
for file in os.listdir(target_dir):
    if file.endswith('.pdf'):
        path = os.path.join(target_dir, file)
        print(f'Merging - {path}...')
        merger.append(path)
print('Files successfully merged!')
try:
    merger.write(merged_pdf_path)
    print(f'Wrote file to {merged_pdf_path}.')
except Exception as e:
    print(f'Error while trying to Write file to {merged_pdf_path}')
    print(f'Exception: {e}')
finally:
    merger.close()
    print('Press enter to continue...')
    input()
    exit(0)
