import pandas
import pdfkit

data = {'x': ['y']}
dataframe = pandas.DataFrame(data)
path = 'TruthFolder/check'

dataframe.to_csv(f'{path}.csv')
dataframe.to_excel(f'{path}.xls', engine='openpyxl')
dataframe.to_html(f'{path}.html')

wkhtml_path = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
options = {
    'page-size': 'A0',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None
}
pdfkit.from_file(f'{path}.html', f'{path}.pdf', configuration=wkhtml_path, options=options)
