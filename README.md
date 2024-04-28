Problem Set I - Regex

Write a regex to extract all the numbers with orange color background from the below text in italics
(Output should be a list)
text={"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},
{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"
[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}

Answer:
numbers= re.findall(r'"id":(\d+)',text)
print(numbers)


Problem Set 3
Please answer the below questions:

A. Write and share a small note about your choice of system to schedule periodic tasks
(such as downloading a list of ISINs every 24 hours). Why did you choose it? Is it reliable enough;
Or will it scale? If not, what are the problems with it? And, what else would you recommend to fix this
problem at scale in production?
Answer:
When it comes to scheduling periodic tasks like downloading a list of ISINs, there are various options available,
such as Cron, Windows Task Scheduler, and Celery. Each of these systems has its advantages and disadvantages.

Cron is a time-based job scheduler in Unix-based operating systems. It is lightweight and easy to set up, making
it a popular choice for simple periodic tasks. However, it can be challenging to manage large numbers of jobs
with Cron, and it lacks some features like centralized management and monitoring.

Windows Task Scheduler is similar to Cron, but it runs on Microsoft Windows systems.
It has a graphical user interface (GUI), which makes it easier to use for people who are not comfortable with
the command line. However, like Cron, it can be difficult to manage large numbers of tasks with Windows Task
Scheduler.

Celery is a distributed task queue that can run periodic tasks on a schedule.
It has features like task retries, error handling, and centralized monitoring, making it a more robust option
for production environments. However, it may require more configuration and setup than Cron or Windows Task
Scheduler.

Ultimately, the choice of system will depend on the specific requirements of the task and the resources available.
For a simple periodic task like downloading a list of ISINs, Cron or Windows Task Scheduler may be sufficient.
However, for more complex tasks that require scalability and robustness, Celery or other distributed task queues
may be a better option.
In terms of scalability, Celery and other distributed task queues are designed to handle large numbers of
tasks and can be scaled horizontally to handle increasing loads. However, like any system, they may have
limitations in terms of the hardware and resources available.
To fix scalability problems in production, additional resources like servers, databases, and load balancers
can be added. Additionally, implementing a distributed architecture and using technologies like Kubernetes or
Docker can help with managing and scaling the system.

B. In what circumstances would you use Flask instead of Django and vice versa?
Answer:
Both Flask and Django are popular web frameworks used for developing web applications in Python.
However, they have different strengths and weaknesses, and the choice of which one to use depends on the
specific requirements of the project.
Flask is a micro web framework that is lightweight and flexible, making it a good choice for small to
medium-sized projects. It is designed to be minimalistic, with a small core and easy-to-use extensions.
Flask is suitable for applications that require high levels of customization, and it can be a good choice
when speed is a priority. Flask also has a low learning curve, which makes it a popular choice for developers
who are new to web development.
On the other hand, Django is a full-stack web framework that provides a lot of built-in functionality,
making it a good choice for large and complex projects. Django includes features like an ORM, a built-in admin
interface, and a templating engine, which can save time in development. Django also has a robust ecosystem, with
many third-party libraries and extensions available. Django is suitable for applications that require a lot of
functionality out of the box and need to be scalable.
In general, Flask is a better choice when the application needs to be customized and optimized for speed,
whereas Django is a better choice when the application needs to be scalable and have a lot of built-in
functionality.
That being said, the choice of which web framework to use ultimately depends on the specific requirements of
the project. If the project requires a lot of customization and speed is a priority, Flask may be the better
choice. If the project requires a lot of built-in functionality and scalability is a priority, Django may be
the better choice.
In some cases, it may even be appropriate to use both frameworks in the same project. For example, Flask can be
used to create microservices that are integrated with a larger Django application.
