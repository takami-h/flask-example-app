from locust import HttpUser, task

class FlaskrUser(HttpUser):
  @task
  def index(self):
    self.client.get("/", name="visit index")
