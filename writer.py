from fillpdf import fillpdfs

def process_pdf(outfile, field_dictionary, infile='ihk_blank.pdf'):
    fillpdfs.write_fillable_pdf(infile, outfile, field_dictionary)