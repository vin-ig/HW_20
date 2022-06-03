import pytest
from unittest.mock import MagicMock

from dao.model.movie import Movie
from service.movie import MovieService
from dao.movie import MovieDAO


@pytest.fixture
def movie_dao():
	movie = MovieDAO(None)

	d1 = Movie(id=1, title='Terminator')
	d2 = Movie(id=2, title='Shrek')
	d3 = Movie(id=3, title='Ghost')

	movie.get_one = MagicMock(return_value=d2)
	movie.get_all = MagicMock(return_value=[d1, d2, d3])
	movie.create = MagicMock(return_value=d3)
	movie.delete = MagicMock()
	movie.update = MagicMock()

	return movie


class TestMovieService:
	@pytest.fixture(autouse=True)
	def movie_service(self, movie_dao):
		self.movie_service = MovieService(dao=movie_dao)

	def test_get_one(self):
		movie = self.movie_service.get_one(2)
		assert movie is not None
		assert movie.id is not None

	def test_get_all(self):
		movies = self.movie_service.get_all()
		assert len(movies) != 0

	def test_create(self):
		new_movie = self.movie_service.create({})
		assert new_movie is not None

	def test_update(self):
		movie = self.movie_service.update({})
		assert movie is not None

	def test_partially_update(self):
		self.movie_service.partially_update({'id': 3, 'title': 'Ghost'})

	def test_delete(self):
		self.movie_service.delete(3)
