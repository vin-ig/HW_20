import pytest
from unittest.mock import MagicMock

from dao.model.director import Director
from service.director import DirectorService

from dao.director import DirectorDAO


@pytest.fixture
def director_dao():
	director = DirectorDAO(None)

	d1 = Director(id=1, name='Valera')
	d2 = Director(id=2, name='Patrik')
	d3 = Director(id=3, name='Cat')

	director.get_one = MagicMock(return_value=d2)
	director.get_all = MagicMock(return_value=[d1, d2, d3])
	director.create = MagicMock(return_value=d3)
	director.delete = MagicMock()
	director.update = MagicMock()

	return director


class TestDirectorService:
	@pytest.fixture(autouse=True)
	def director_service(self, director_dao):
		self.director_service = DirectorService(dao=director_dao)

	def test_get_one(self):
		director = self.director_service.get_one(2)
		assert director is not None
		assert director.id is not None

	def test_get_all(self):
		directors = self.director_service.get_all()
		assert len(directors) != 0

	def test_create(self):
		new_director = self.director_service.create({})
		assert new_director is not None

	def test_update(self):
		director = self.director_service.update({})
		assert director is not None

	def test_partially_update(self):
		self.director_service.partially_update({'id': 3, 'name': 'Dog'})

	def test_delete(self):
		self.director_service.delete(3)
