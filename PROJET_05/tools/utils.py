# ----------------------------------
# -- MODULE FOR VARIOUS FUNCTIONS --
# ----------------------------------


def teminal_loop_for_displaying_items(table, line_color, separator_color):
	for line in table:
		print(line_color + (str(line)), end = " * ")
	print()
	for _ in range (125):
		print(separator_color + ".", end = "")
	print()
