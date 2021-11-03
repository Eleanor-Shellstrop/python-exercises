import typer
from ssg.site import Site

import ssg.parsers

def main(source="content", dest="dist"):
	config = {
		"source": source, 
		"dest": dest, 
		"parsers": [ssg.parsers.REsourceParser(),],
	}
	Site(**config).build()

typer.run(main)