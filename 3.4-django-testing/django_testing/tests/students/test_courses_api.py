import pytest

from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def courses():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture
def student():
    def factory(*args,**kwargs):
        return baker.make(Student, *args,**kwargs)
    return factory


@pytest.mark.django_db
def test_retrieve_course(client, courses):

    cours = courses(_quantity = 3)

    responce = client.get('/api/v1/courses/', format = 'json')

    assert responce.status_code == 200

    data = responce.json()

    assert len(cours) == len(data) 

    assert data[0]['name'] == cours[0].name

    assert data[0]['name'] != cours[1].name



@pytest.mark.django_db
def test_list_course(client,courses):
    cours = courses(_quantity = 5)

    responce = client.get('/api/v1/courses/', format = 'json')

    assert responce.status_code == 200

    data = responce.json()

    assert len(data) == len(cours)

    for i,d in enumerate(data):
        assert d['name'] == cours[i].name


@pytest.mark.django_db
def test_course_on_id(client,courses):
    cours = courses(_quantity = 5)
    id = cours[3].id
    responce = client.get('/api/v1/courses/', {'id':id}, format = 'json')
    
    data = responce.json()

    assert responce.status_code == 200

    assert data[0]['id'] == id
    

@pytest.mark.django_db
def test_course_on_name(client,courses):
    cours = courses(_quantity = 5)
    name = cours[3].name
    responce = client.get('/api/v1/courses/', {'name':name}, format = 'json')
    
    data = responce.json()

    assert responce.status_code == 200

    assert data[0]['name'] == name


@pytest.mark.django_db
def test_create_course(client):
    
    data_ = {'name':'mathematics'}

    assert Course.objects.filter(name = 'mathematics').count() == 0

    responce = client.post('/api/v1/courses/', data = data_, format = 'json')

    assert responce.status_code == 201

    assert Course.objects.filter(name = 'mathematics').count() == 1


@pytest.mark.django_db
def test_update_course(client,courses):

    cours = courses(_quantity = 1)

    data_ = {'name':'geometry'}

    responce = client.patch(f'/api/v1/courses/{cours[0].id}/', data = data_ , format = 'json')

    assert responce.status_code == 200

    assert Course.objects.count() == 1

    assert Course.objects.filter(name = 'geometry').count() == 1


@pytest.mark.django_db
def test_delete_course(client,courses):
    
    cours = courses(_quantity = 1)

    responce = client.delete(f'/api/v1/courses/{cours[0].id}/', format = 'json')

    assert responce.status_code == 204

    assert Course.objects.count() == 0



