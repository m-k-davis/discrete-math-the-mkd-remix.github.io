#!/usr/local/bin/py
import os, sys, copy, shutil
from bs4 import BeautifulSoup

def get_soup(html_file):
	return BeautifulSoup(open(html_file, 'rb').read(), 'html.parser')

# build master toc
#print('Hello')
#os.system("asciidoctor-latex -b html " + 'book.adoc')
# MKD altered this call to try to implement collapsible toc
#os.system("asciidoctor-latex -a toc=left -a docinfo=shared --doctype book -b html " + 'book.adoc')
#os.system("/opt/homebrew/lib/ruby/gems/3.3.0/gems/asciidoctor-latex-1.5.0.17.dev/bin/asciidoctor-latex -a toc=left -a docinfo=shared --doctype book -b html " + 'book.adoc')
os.system("/opt/homebrew/Cellar/ruby/3.3.4/lib/ruby/gems/3.3.0/gems/asciidoctor-latex-1.5.0.17.dev/bin/asciidoctor-latex -a toc=left -a docinfo=shared --doctype book -b html " + 'book.adoc')


# get list of chapter files for asciidoctor
# chap_adocs = sorted([f for f in os.listdir() if f.startswith("chapter") and f.endswith(".adoc")])
# chap_adocs = ['index.adoc', 'introduction_discrete_math.adoc', 'python_intro.adoc', 'logic.adoc', 'set_theory.adoc', 'functions.adoc', 'growth_functions.adoc', 'algorithms.adoc', 'counting.adoc', 'number_theory.adoc', 'induction_recursion.adoc', 'graph_theory.adoc', 'appendix_one.adoc', 'appendix_two.adoc']
# chap_htmls = [f.replace('.adoc', '.html') for f in chap_adocs]
# MKD addded lines below
#chap_adocs = ['index.adoc', 'introduction_discrete_math.adoc', 'set_theory.adoc', 'logic.adoc', 'proofs.adoc', 'recursion.adoc', 'algorithms_and_big_o.adoc', 'induction.adoc', 'functions.adoc', 'relations.adoc', 'counting.adoc', 'probability.adoc', 'number_bases.adoc', 'graph_theory.adoc', 'trees.adoc', 'appendix_math.adoc', 'appendix_library.adoc', 'appendix_pyintro.adoc', 'appendix_pysyntax.adoc']
#chap_adocs = ['index.adoc', 'introduction_discrete_math.adoc', 'set_theory.adoc', 'logic.adoc', 'proofs.adoc', 'recursion.adoc', 'functions.adoc', 'relations.adoc', 'number_bases.adoc', 'algorithms_and_big_o.adoc', 'induction.adoc', 'counting.adoc', 'graph_theory.adoc', 'trees.adoc', 'probability.adoc', 'appendix_math.adoc', 'appendix_library.adoc', 'appendix_pyintro.adoc', 'appendix_pysyntax.adoc']
#chap_adocs = ['index.adoc', 'introduction_discrete_math.adoc', 'set_theory.adoc', 'logic.adoc', 'proofs.adoc', 'recursion.adoc', 'functions.adoc', 'relations.adoc', 'number_bases.adoc', 'algorithms.adoc', 'induction.adoc', 'growth_functions.adoc', 'counting.adoc', 'graph_theory.adoc', 'trees.adoc', 'appendix_math.adoc', 'appendix_library.adoc', 'appendix_pyintro.adoc', 'appendix_pysyntax.adoc']
#chap_adocs = ['index.adoc', 'introduction_discrete_math.adoc', 'set_theory.adoc', 'logic.adoc', 'proofs.adoc', 'recursion.adoc', 'functions.adoc', 'relations.adoc', 'number_bases.adoc', 'growth_of_functions.adoc', 'algorithms.adoc', 'induction.adoc', 'counting.adoc', 'graph_theory.adoc', 'trees.adoc', 'appendix_math.adoc', 'appendix_library.adoc', 'appendix_pyintro.adoc', 'appendix_pysyntax.adoc']
# Following is is the Fall 2024 chapter order
#chap_adocs = ['index.adoc', 'introduction_discrete_math.adoc', 'counting_arithmetic.adoc', 'number_bases.adoc', 'counting_binomial.adoc', 'set_theory.adoc', 'logic.adoc', 'proofs.adoc', 'recursion.adoc', 'functions.adoc', 'relations.adoc', 'growth_of_functions.adoc', 'algorithms.adoc', 'induction.adoc', 'graph_theory.adoc', 'trees.adoc', 'appendix_math.adoc', 'appendix_library.adoc', 'appendix_pyintro.adoc', 'appendix_pysyntax.adoc']
# Following is is the Spring 2024 chapter order
#chap_adocs = ['index.adoc', 'introduction_discrete_math.adoc', 'counting_arithmetic.adoc', 'set_theory.adoc', 'counting_binomial.adoc', 'logic.adoc', 'proofs.adoc', 'recursion.adoc', 'functions.adoc', 'growth_of_functions.adoc', 'number_bases.adoc', 'algorithms.adoc', 'induction.adoc', 'relations.adoc', 'graph_theory.adoc', 'trees.adoc', 'appendix_math.adoc', 'appendix_library.adoc', 'appendix_pyintro.adoc', 'appendix_pysyntax.adoc']
#MKD Jan 22 2025 order 
#chap_adocs = ['index.adoc', 'introduction_discrete_math.adoc', 'counting_arithmetic.adoc', 'set_theory.adoc', 'counting_binomial.adoc', 'logic.adoc', 'proofs.adoc', 'recursion.adoc', 'functions.adoc', 'growth_of_functions.adoc', 'number_bases.adoc', 'algorithms.adoc', 'induction.adoc', 'relations.adoc', 'graph_theory.adoc', 'trees.adoc', 'appendix_math.adoc', 'appendix_library.adoc', 'appendix_pyintro.adoc', 'appendix_pysyntax.adoc']
#MKD Jan 26 2025 order 
#chap_adocs = ['index.adoc', 'introduction_discrete_math.adoc', 'counting_arithmetic.adoc', 'set_theory.adoc', 'logic.adoc', 'proofs.adoc', 'number_bases.adoc', 'recursion.adoc', 'functions.adoc', 'relations.adoc', 'growth_of_functions.adoc', 'counting_binomial.adoc', 'induction.adoc', 'algorithms.adoc', 'graph_theory.adoc', 'trees.adoc', 'appendix_math.adoc', 'appendix_library.adoc', 'appendix_pyintro.adoc', 'appendix_pysyntax.adoc']
#MKD Feb 2 2025 order 
#chap_adocs = ['index.adoc', 'introduction_discrete_math.adoc', 'counting_arithmetic.adoc', 'set_theory.adoc', 'logic.adoc', 'proofs.adoc', 'number_bases.adoc', 'recursion.adoc', 'functions.adoc', 'relations.adoc', 'counting_binomial.adoc', 'induction.adoc', 'growth_of_functions.adoc', 'algorithms.adoc', 'graph_theory.adoc', 'trees.adoc', 'appendix_math.adoc', 'appendix_library.adoc', 'appendix_pyintro.adoc', 'appendix_pysyntax.adoc', 'appendix_for_instructors.adoc']
#MKD Aug 24 2025 bis order 
chap_adocs = ['index.adoc', 'introduction_discrete_math.adoc', 'number_bases.adoc', 'counting_arithmetic.adoc', 'set_theory.adoc', 'logic.adoc', 'proofs.adoc', 'recursion.adoc', 'functions.adoc', 'relations.adoc', 'counting_binomial.adoc', 'induction.adoc', 'growth_of_functions.adoc', 'algorithms.adoc', 'graph_theory.adoc', 'trees.adoc', 'appendix_math.adoc', 'appendix_library.adoc', 'appendix_pyintro.adoc', 'appendix_pysyntax.adoc', 'appendix_for_instructors.adoc']

chap_htmls = [f.replace('.adoc', '.html') for f in chap_adocs]

# go through master toc and update links to point to separate html files.
soup = get_soup('book.html')
toc_html = soup.find(id="toc")
anchors = toc_html.find_all('a')
# MKD added next line
#for a in anchors: print(a)

# MKD debugging Jan 19 2025
#for a in anchors:
#	print(a)

# MKD rewriting Jan 19 2025
# chap_index = 0
# for a in anchors:
# 	label = str(a.text)
# 	#print(label)
# 	if not (label.startswith(str(chap_index+1) + ".")):
# 		chap_index += 1
# 	#a['href'] = chap_htmls[chap_index] + a['href']
# 	# MKD
# 	try: 
# 		a['href'] = chap_htmls[chap_index] + a['href']
# 	except IndexError: 
# 		print(a)
# 		raise
chap_index = 0
for a in anchors:
	label = str(a.text)
	try: 
		a['href'] = chap_htmls[chap_index] + a['href']
	except IndexError: 
		print(a)
		raise
	chap_index += 1

# build copies of book with just 1 chapter in each.
for chap_index in range(0, len(chap_htmls)):
	# MKD debugging Jan 19 2025
	#print("Creating " + chap_htmls[chap_index] + "\t" + str(chap_index))
	#
	print("Creating " + chap_htmls[chap_index])
	soup_copy = copy.copy(soup)
	loop_count = 0
	for div in soup_copy.find_all('div', {"class":"sect1"}):
		if loop_count != chap_index:
			div.decompose()
		loop_count += 1

	with open(chap_htmls[chap_index], "wb") as f_output:
			f_output.write(soup_copy.prettify("utf-8"))
			f_output.close()

# # MKD float to 64 bits added Mar 6 2025
# import struct
# 
# def float_to_bits(f):
#   """Converts a float to its 64-bit binary representation as a string."""
#   # Pack the float into a 64-bit double-precision (d) byte string in little-endian (<) order
#   packed_bytes = struct.pack('<d', f)
#   # Convert the bytes to an integer and then to a binary string
#   bits = bin(int.from_bytes(packed_bytes, 'little'))[2:].zfill(64)
#   return bits
# 
# # Example usage:
# number = 12.2
# number = 1.4
# bits = float_to_bits(number)
# print(f"The 64-bit representation of {number} is: {bits}")
# #The 64-bit representation of 1.4 is: #"0011111111110110011001100110011001100110011001100110011001100110"
# #"0011111111110110011001100110011001100110011001100110011001100110"
# 
# number = 0.1
# bits = float_to_bits(number)
# print(f"The 64-bit representation of {number} is: {bits}")
# 
