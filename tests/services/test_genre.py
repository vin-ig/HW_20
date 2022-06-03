import pytest
from unittest.mock import MagicMock

from dao.model.genre import Genre
from service.genre import GenreService
from dao.genre import GenreDAO


@pytest.fixture
def genre_dao():
	genre = GenreDAO(None)

	d1 = Genre(id=1, name='musical')
	d2 = Genre(id=2, name='comedy')
	d3 = Genre(id=3, name='thriller')

	genre.get_one = MagicMock(return_value=d2)
	genre.get_all = MagicMock(return_value=[d1, d2, d3])
	genre.create = MagicMock(return_value=d3)
	genre.delete = MagicMock()
	genre.update = MagicMock()

	return genre


class TestGenreService:
	@pytest.fixture(autouse=True)
	def genre_service(self, genre_dao):
		self.genre_service = GenreService(dao=genre_dao)

	def test_get_one(self):
		genre = self.genre_service.get_one(2)
		assert genre is not None
		assert genre.id is not None

	def test_get_all(self):
		genres = self.genre_service.get_all()
		assert len(genres) != 0

	def test_create(self):
		new_genre = self.genre_service.create({})
		assert new_genre is not None

	def test_update(self):
		genre = self.genre_service.update({})
		assert genre is not None

	def test_partially_update(self):
		self.genre_service.partially_update({'id': 3, 'name': 'thriller'})

	def test_delete(self):
		self.genre_service.delete(3)
