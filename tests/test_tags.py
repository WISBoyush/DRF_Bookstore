import pytest

from tags.models import Tag


class TestTag:

    @pytest.mark.django_db
    def test_tag_list(self, api_client, user):
        url = '/api/tag/'

        response = api_client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_tag_list_detail(self, api_client, user):
        url = f'/api/tag/1'

        response = api_client.get(url, follow=True)
        assert response.status_code == 200
        assert Tag.objects.get(id=1).tag_title == response.data['tag_title']

    @pytest.mark.django_db
    def test_tag_change_tag_not_su(self, api_client, user):
        url = f'/api/tag/1/update_tag'

        response = api_client.patch(url, {"tag_title": "Test title"}, follow=True)
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_tag_change_tag_su(self, api_client, superuser):
        url = f'/api/tag/1/update_tag/'

        response = api_client.patch(url, {"tag_title": "Test title"}, format='json', follow=True)
        assert response.status_code == 200
        assert Tag.objects.get(id=1).tag_title == "Test title"
