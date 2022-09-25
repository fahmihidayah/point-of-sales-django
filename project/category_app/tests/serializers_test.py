from . import base_setup_test
from category_app.serializers import CategorySerializers


class SerializersTestCase(base_setup_test.CategoryBaseTestCase):

    def setUp(self) -> None:
        super(SerializersTestCase, self).setUp()

    def test_create_success(self):
        serializer : CategorySerializers = CategorySerializers(data={
            "name" : "category A",
            "description" : "The description"
        }, user=self.user)

        self.assertTrue(serializer.is_valid())
