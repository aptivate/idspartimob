# IDS, UNICEF and RuralNet Participatory Mobile Project

See http://blog.aptivate.org/2011/12/05/rough-guide-to-rural-data-collection-with-odk/ for details.

## build_and_validate.py

Compiles a specific file (zambia-ranq-round3.xls) in the current directory
from Excel to XForms (using XLS2XForm) and then validates it.

Under Windows it pops up a message box indicating success or failure.
Failures are usually caused by errors in the Excel spreadsheets, such as
using an undefined question type, or a "begin group" without a matching
"end group".

## build_and_validate_custom.py

Compiles the form named on the command line from Excel (XLS) to XForms
and validates it.

