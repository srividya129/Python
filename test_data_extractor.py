import unittest
import json
from src.data_extractor import get_emp_data

class MyTestCase(unittest.TestCase):
    def test_get_emp_data(self):
        expected_keys=2
        actual_res = get_emp_data()
        print(actual_res)
        data = json.loads(actual_res)
        actual_res_keys = len(data)
        assert actual_res_keys==expected_keys

    def test_employee_name_forid(self):
        actual_res = get_emp_data()
        data = json.loads(actual_res)
        for item in data['data']:
            if item["id"] == '1':
                emp_name = item['employee_name']
        actual_name ="Tiger Nixon"
        assert actual_name == emp_name

    def test_emp_sal(self):
        actual_res=get_emp_data()
        data=json.loads(actual_res)
        for item in data['data']:
            if item['id']=='2':
                emp_sal=item['employee_salary']
        actual_sal="20000"
        assert actual_sal==emp_sal

if __name__ == '__main__':
    unittest.main()
