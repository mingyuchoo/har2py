from locust import HttpLocust, TaskSequence, seq_task
from haralyzerfile import get_info_from_har



class TaskSet(TaskSequence):

    context = None

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def login(self):
        pass

    def logout(self):
        pass

    @seq_task(1)
    def request(self):
        if self.context['method'] == 'GET':
            self.client.get(self.context['url'])
        elif self.context['method'] == 'POST':
            self.client.post(self.context['url'])
        elif self.context['method'] == 'PUT':
            self.client.put(self.context['url'])
        elif self.context['method'] == 'DELETE':
            self.client.delete(self.context['url'])
        else:
            pass

class WebsiteUser(HttpLocust):
    """
    USAGE: locust -f locustfile.py --no-web -c 1 -r 1 -t 1m
    """
    file_path = 'resources/gatling.har'
    context = get_info_from_har(file_path)

    url_tokens = context['url'].split('/')
    host = ''.join([url_tokens[0], '//', url_tokens[2]])

    task_set = TaskSet
    task_set.context = context

    min_wait = 1000
    max_wait = 3000


