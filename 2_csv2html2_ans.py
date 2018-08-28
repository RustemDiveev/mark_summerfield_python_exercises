#python 2_csv2html2_ans.py -h < 2_co2-sample.csv > 2_mydata.html
import sys
import xml.sax.saxutils

def main():
    print_params = process_options()
    if any(print_params):
        maxwidth = print_params[0]
        format = print_params[1]
        print_start()
        count = 0
        while True:
            try:
                line = input()
                if count == 0:
                    color = "lightgreen"
                elif count % 2:
                    color = "white"
                else:
                    color = "lightyellow"
                print_line(line, color, maxwidth, format)
                count += 1
            except EOFError:
                break
        print_end()

def process_options(): 
    #Check input params
    helpUsed = 0
    maxwidth = None
    format = None
    if len(sys.argv) > 1:
        if sys.argv[1] in ("-h", "--help"):
            print("usage:" + '\n' +
                   sys.argv[0] + " [maxwidth=int] [format=str] < infile.csv > outfile.html" + '\n' +
                  "maxwidth is an optional integer; if specified, it sets the maximum " + '\n' + 
                  "number of characters that can be output for string fields, " + '\n' + 
                  "otherwise a default of 100 characters is used." + '\n' + '\n' +
                  "format is the format to use for numbers; if not specified it" + '\n' +
                  "defaults to \".0f\".")
            helpUsed = 1
        else:
            for i in sys.argv[1:]:
                if 'maxwidth' in i.lower():
                    maxwidth = int(i.split("=")[1])
                elif 'format' in i.lower():
                    format = str(i.split("=")[1].strip())
    if helpUsed == 1:
        return None, None
    else:
        if maxwidth is None: 
            maxwidth = 100
        if format is None:
            format = ".0f"
        return maxwidth, format
    

def print_start():
    print("<table border='1'>")

def print_line(line, color, maxwidth, format):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                numFormat = "<td align='right'>{{0:{0}}}</td>".format(format)
                print(numFormat.format(x))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                if len(field) <= maxwidth:
                    field = escape_html(field)
                else:
                    field = "{0} ...".format(escape_html(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")

def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None: #start of quoted string
                quote = c
            elif quote == c: #end of quoted string
                quote = None
            else:
                field += c #other quote inside quoted string
            continue
        if quote is None and c == ",": #end of field
            fields.append(field)
            field = ""
        else:
            field += c #accumulating a field
    if field:
        fields.append(field) #adding the last field
    return fields

def escape_html(text):
    return xml.sax.saxutils.escape(text)

def print_end():
    print("</table>")

main()
