from locust import HttpLocust, TaskSet, task

class Hello(TaskSet):
    @task(1)
    def index(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    task_set = Hello
    min_wait = 1000
    max_wait = 1000