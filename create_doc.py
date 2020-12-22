from docxcompose.composer import Composer
from docx import Document
master = Document(r".\template\base.docx")
composer = Composer(master)
tail = Document(r".\template\tail.docx")
composer.append(tail)
composer.save(r".\template\combined.docx")

