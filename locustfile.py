from locust import HttpLocust, TaskSet
import random

def index(l):
    l.client.get("/")

def train(l):
    l.client.post("/train")

class UserBehavior(TaskSet):
    tasks = {index:1, train:2}
#    tasks = {index:1}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_function = lambda self: random.randint(5,15)*1000
