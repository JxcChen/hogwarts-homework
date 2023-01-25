from web.page.main_page import MainPage
from web.testcase.assert_screenshot import fail_screenshot
from web.testcase.test_base import TestBase


class TestContact(TestBase):
    main = MainPage()

    @fail_screenshot
    def test_add_member(self):
        assert 'name02' == self.main.into_contact_page() \
            .add_member('name03', 'english03', '11113335', 'qweasd', '14421422326', '广州研发中心') \
            .search_member_or_department('name04') \
            .get_member_search_detail()

    @fail_screenshot
    def test_add_department(self):
        assert self.main.into_contact_page()\
            .add_department('test_department02', '研发部') \
            .search_member_or_department('test_department02') \
            .get_department_search_detail() == 'test_department02'
