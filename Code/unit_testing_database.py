import unittest
import pandas
from pandas.testing import assert_frame_equal
from database_handler import CRUD
from file_generator import ExportAs


class TestGenerate(unittest.TestCase):
    def setUp(self):
        self.crud = CRUD()
        self.export = ExportAs()
        self.conn, self.check = self.crud.establish_connection('shravan', 'Vvu8z9D')
        self.test_db = 'test_db'
        self.test_table = 'test_table'
        self.addTypeEqualityFunc(pandas.DataFrame, self.assertDataframeEqual)

    def tearDown(self):
        self.conn.close()

    @staticmethod
    def assertDataframeEqual(a, b):
        assert_frame_equal(a, b)

    def test_connection(self):
        try:
            mydb, check = self.crud.establish_connection('shravan', 'Vvu8z9D')
            self.assertEqual(check, True)

            mydb, check = self.crud.establish_connection('shravan', 'not_a_password')
            self.assertEqual(check, False)

            mydb, check = self.crud.establish_connection('not_a_user', 'Vvu8z9D')
            self.assertEqual(check, False)

            mydb, check = self.crud.establish_connection('wrong_type_password', 10)
            self.assertEqual(check, False)

        except Exception as error:
            self.assertNotEqual(True, error)

    def test_create(self):
        try:
            command = f"CREATE TABLE {self.test_db}.{self.test_table} ( `ID` int NOT NULL, `TITLE` varchar(300) " \
                      f"DEFAULT NULL, PRIMARY KEY (`ID`)) "
            check = self.crud.create_table(self.conn, self.test_db, self.test_table, command)
            self.assertEqual(check, True)

            check = self.crud.create_table('Not_a_connection', self.test_db, self.test_table, command)
            self.assertEqual(check, False)

        except Exception as error:
            self.assertNotEqual(True, error)

    def test_insert(self):
        try:
            command = f"INSERT INTO {self.test_db}.{self.test_table} (ID, TITLE) VALUES (%s, %s)"
            values = [(1, 'Item 1'), (2, 'Item 2'), (3, 'Item 3'), (4, 'Item 4')]
            check = self.crud.insert_values(self.conn, self.test_db, self.test_table, command, values)
            self.assertEqual(check, True)
            check_list = []
            for i in range(len(values)):
                command = f"SELECT * FROM {self.test_db}.{self.test_table} WHERE ID={values[i][0]}"
                cursor = self.conn.cursor()
                cursor.execute(command)
                check_list.append(cursor.fetchall())
            self.assertDataframeEqual(pandas.DataFrame(check_list), pandas.DataFrame(values))

        except Exception as error:
            self.assertNotEqual(True, error)

    def test_update(self):
        try:
            command = f"UPDATE {self.test_db}.{self.test_table} SET TITLE = %s WHERE ID = %s"
            values = [('New Item 1', 1), ('New Item 2', 2)]
            check = self.crud.update_values(self.conn, self.test_db, self.test_table, command, values)
            self.assertEqual(check, True)
            check_list = []
            for i in range(len(values)):
                command = f"SELECT * FROM {self.test_db}.{self.test_table} WHERE ID={values[i][1]}"
                cursor = self.conn.cursor()
                cursor.execute(command)
                check_list.append(cursor.fetchall())
            self.assertDataframeEqual(pandas.DataFrame(check_list), pandas.DataFrame(values))

        except Exception as error:
            self.assertNotEqual(True, error)

    def test_delete(self):
        try:
            del_conn, unused = self.crud.establish_connection('shravan', 'Vvu8z9D')
            value = 1
            command = f"DELETE FROM {self.test_db}.{self.test_table} WHERE ID={value}"
            check = self.crud.delete_rows(del_conn, self.test_db, self.test_table, command)
            self.assertEqual(check, True)
            command = f"SELECT * FROM {self.test_db}.{self.test_table} WHERE ID={value}"
            cursor = self.conn.cursor()
            cursor.execute(command)
            self.assertDataframeEqual(pandas.DataFrame(cursor.fetchall()), pandas.DataFrame([]))
        except Exception as error:
            self.assertNotEqual(True, error)


if __name__ == '__main__':
    unittest.main()
