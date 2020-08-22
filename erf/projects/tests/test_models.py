from django.test import TestCase

from ..models import Project


class TestProject(TestCase):
    def test_it_should_have_defined_fields(self):
        expected_name = 'Fish Tank'
        Project.objects.create(name=expected_name)

        project = Project.objects.last()

        assert project.name == expected_name
        assert project.created is not None
        assert project.modified is not None
