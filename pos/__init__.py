__author__ = 'rhvonlehe'

"""
omnivore API wrapper
"""

from restnavigator import Navigator
from employee import Employee
from revenue_center import RevenueCenter
from order_type import OrderType
from table import Table


class Pos:

    # TODO: possibly move some of this to separate Config class
    #
    _version = '0.1'
    _location_base = 'https://api.omnivore.io/' + _version + '/locations/'

    def __init__(self, api_key, location):
        self._api_key = api_key
        self._url_base = self._location_base + location + '/'
        self._headers={'Api-Key': self._api_key}
        self._navigator = Navigator.hal(self._url_base, headers=self._headers)

    def revenue_centers(self):
        revs = self._navigator['revenue_centers']
        revenue_center_list = []

        for index in range(0, revs()['count']):
            state = revs['revenue_centers'][index].state
            revenue_center_list += [RevenueCenter(state)]

        return revenue_center_list

    def employees(self):
        emps = self._navigator['employees']
        employee_list = []

        for index in range(0, emps()['count']):
            state = emps['employees'][index].state
            employee_list += [Employee(state)]

        return employee_list

    def order_types(self):
        ords = self._navigator['order_types']
        order_type_list = []

        for index in range(0, ords()['count']):
            state = ords['order_types'][index].state
            order_type_list += [OrderType(state)]

        return order_type_list

    def tables(self):
        tabs = self._navigator['tables']
        table_list = []

        for index in range(0, tabs()['count']):
            state = tabs['tables'][index].state
            table_list += [Table(state)]

        return table_list


    def create_ticket(self, employee, order_type, revenue_center,
                      table, guest_count, name, auto_send = True):
        # print self._navigator['tickets']
        # print employee.id()
        # print order_type.id()
        # print revenue_center.id()
        # print table
        # print name

        print self._navigator['tickets'].create({'employee': employee.id(),
                                                 'order_type': order_type.id(),
                                                 'revenue_center': revenue_center.id(),
                                                 'table': table.id(),
                                                 'guest_count' : guest_count,
                                                 'name' : name,
                                                 'auto_send': auto_send})















