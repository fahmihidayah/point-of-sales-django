from .base_setup_test import CategoryBaseTestCase

class RepositoryTestCase(CategoryBaseTestCase):

    def test_find_all_count_equal_one_true(self):
        self.assertEqual(1, self.category_repository.find_all().count())

    def test_find_by_name_true(self):
        self.assertIsNotNone(self.category_repository.get_by_name(name="food"))

    def test_find_by_name_false(self):
        self.assertIsNone(self.category_repository.get_by_name(name='drink'))
