from os.path import exists
from file_generator import ExportAs
from pandas.testing import assert_frame_equal
import PyPDF2
import unittest
import pandas
import hashlib


class TestGenerate(unittest.TestCase):
    def setUp(self):
        self.export = ExportAs()
        self.addTypeEqualityFunc(pandas.DataFrame, self.assertDataframeEqual)

    def tearDown(self):
        None

    @staticmethod
    def assertDataframeEqual(a, b):
        assert_frame_equal(a, b)

    def test_export_csv(self):
        data = {'x': ['y']}
        dataframe = pandas.DataFrame(data)
        test_path = 'TestFolder/check'
        truth_path = 'TruthFolder/check'
        self.export.output_csv(dataframe, test_path)
        if exists(f'{test_path}.csv'):
            truth_hasher = hashlib.md5()
            with open(f'{truth_path}.csv', 'rb') as file:
                buffer = file.read()
                truth_hasher.update(buffer)

            test_hasher = hashlib.md5()
            with open(f'{test_path}.csv', 'rb') as file:
                buffer = file.read()
                test_hasher.update(buffer)

            self.assertEqual(test_hasher.hexdigest(), truth_hasher.hexdigest())

    def test_export_xls(self):
        data = {'x': ['y']}
        dataframe = pandas.DataFrame(data)
        test_path = 'TestFolder/check'
        truth_path = 'TruthFolder/check'
        self.export.output_xls(dataframe, test_path)
        if exists(f'{test_path}.xls'):
            truth_frame = pandas.read_excel(f'{truth_path}.xls')
            test_frame = pandas.read_excel(f'{test_path}.xls')
            self.assertDataframeEqual(truth_frame, test_frame)
            # assert_frame_equal(truth_frame, test_frame)

    def test_export_html(self):
        data = {'x': ['y']}
        dataframe = pandas.DataFrame(data)
        test_path = 'TestFolder/check'
        truth_path = 'TruthFolder/check'
        self.export.output_html(dataframe, test_path)
        if exists(f'{test_path}.html'):
            truth_hasher = hashlib.md5()
            with open(f'{truth_path}.html', 'rb') as truth_file:
                buffer = truth_file.read()
                truth_hasher.update(buffer)

            test_hasher = hashlib.md5()
            with open(f'{test_path}.html', 'rb') as truth_file:
                buffer = truth_file.read()
                test_hasher.update(buffer)

            self.assertEqual(test_hasher.hexdigest(), truth_hasher.hexdigest())

    def test_export_pdf(self):
        data = {'x': ['y']}
        dataframe = pandas.DataFrame(data)
        test_path = 'TestFolder/check'
        truth_path = 'TruthFolder/check'
        self.export.output_pdf(dataframe, test_path)

        if exists(f'{test_path}.pdf'):
            with open(f'{truth_path}.pdf', 'rb') as file:
                pdfReader = PyPDF2.PdfFileReader(file)
                truth_pages = []
                for i in range(pdfReader.numPages):
                    pageObj = pdfReader.getPage(i)
                    truth_pages.append(pageObj.extractText())

            with open(f'{test_path}.pdf', 'rb') as file:
                pdfReader = PyPDF2.PdfFileReader(file)
                test_pages = []
                for i in range(pdfReader.numPages):
                    pageObj = pdfReader.getPage(i)
                    test_pages.append(pageObj.extractText())

            self.assertDataframeEqual(pandas.DataFrame(truth_pages), pandas.DataFrame(test_pages))


if __name__ == '__main__':
    unittest.main()
