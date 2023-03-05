import unittest
import os
os.environ['TESTING'] = 'true'

from app import app
class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        assert "<a class=\"nav-link\" href=\"#about\">About</a>" in html
        assert "<span class=\"pull\"> Pull </span>" in html
    
    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        # TODO add more tests relating to the /api/timeline_post GET and POST apis
        response = self.client.post("/api/timeline_post", 
                                   data= { "name": "John Doe", "email": 'john@example.com', "content": "Hello world, I'm john!"})
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert json['content'] == "Hello world, I'm john!"
        assert json['email'] == "john@example.com"
        assert json['id'] == 1
        assert json['name'] == "John Doe"
        response = self.client.get("/api/timeline_post")
        json = response.get_json()
        assert response.status_code == 200
        assert response.is_json
        assert json['timeline_posts'][0]['content'] == "Hello world, I'm john!"
        assert json['timeline_posts'][0]['email'] == "john@example.com"
        assert json['timeline_posts'][0]['id'] == 1
        assert json['timeline_posts'][0]['name'] == "John Doe"

        # TODO Add more tests relating to the timeline page
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<div class=\"col-md-12\">" in html
        assert "<h2>Timeline Posts</h2>" in html
     
       
    
    def test_malformed_timeline_post(self):
        response = self.client.post("/api/timeline_post", data= {"email": 'john@example.com', "content": "Hello world, I'm john!"})
        assert response.status_code == 400
     
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        response = self.client.post("/api/timeline_post", data= { "name": "John Doe", "email": 'john@example.com', "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        response = self.client.post("/api/timeline_post", data= { "name": "John Doe", "email": 'not-an-email', "content": "Hello world, I'm john!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html

        