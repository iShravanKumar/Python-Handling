import pdfkit
from log_generator import logging
from os.path import exists


GENERATED_FILES = []


class OutputHandler:
    """
    Base Class
    """

    def __init__(self):
        """
        Constructor
        """
        self.dataframe = None
        self.file_name = None

    def output_csv(self, dataframe, file_name):
        """
        Export to CSV

        :param file_name: string, file name
        :param dataframe: pandas.DataFrame()
        """
        try:
            self.dataframe = dataframe
            self.file_name = file_name
            self.dataframe.to_csv(f'{file_name}.csv')
            logging.info('Successful export to CSV')
            GENERATED_FILES.append(f'{file_name}.csv')
        except AttributeError:
            logging.error(f"Attribute error during Export to CSV with {self.dataframe}")
        except Exception as err:
            logging.error(f'Unknown error during Export to CSV, {err}')

    def output_xls(self, dataframe, file_name):
        """
        Export to Excel

        :param file_name: string, file name
        :param dataframe: pandas.DataFrame()
        """
        try:
            self.dataframe = dataframe
            self.file_name = file_name
            self.dataframe.to_excel(f'{file_name}.xls', engine='openpyxl')
            logging.info('Successful export to Excel')
            GENERATED_FILES.append(f'{file_name}.xls')
        except AttributeError:
            logging.error(f"Attribute error during Export to EXCEL with {self.dataframe}")
        except Exception as err:
            logging.error(f'Unknown error during Export to EXCEL, {err}')

    def output_html(self, dataframe, file_name):
        """
        Export to HTML

        :param file_name: string, file name
        :param dataframe: pandas.DataFrame()
        """
        try:
            self.dataframe = dataframe
            self.file_name = file_name
            self.dataframe.to_html(f'{file_name}.html')
            logging.info('Successful export to HTML')
            GENERATED_FILES.append(f'{file_name}.html')
        except AttributeError:
            logging.error(f"Attribute error during Export to HTML with {self.dataframe}")
        except Exception as err:
            logging.error(f'Unknown error during Export to HTML, {err}')


class ExportAs(OutputHandler):
    """
    Sub Class
    """

    def __init__(self):
        """
        Constructor
        """
        OutputHandler.__init__(self)

    def __str__(self):
        """
        Special Method
        """
        return 'Export options CSV, EXCEL, HTML, PDF'

    def output_pdf(self, dataframe, file_name):
        """
        Export to PDF
        """
        self.dataframe = dataframe
        self.file_name = file_name
        try:
            if not exists(f'{file_name}.html'):
                OutputHandler.output_html(self, dataframe=self.dataframe)
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
            pdfkit.from_file(f'{file_name}.html', f'{file_name}.pdf', configuration=wkhtml_path, options=options)
            logging.info('Successful export to PDF')
            GENERATED_FILES.append(f'{file_name}.pdf')
        except AttributeError:
            logging.error("Attribute error during Export to PDF")
        except Exception as err:
            logging.error(f'Unknown error during Export to PDF, {err}')
