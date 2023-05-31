# There is a difference between @task(shared=True) and @shared_task
#
#
# The task decorator will share tasks between apps by default so that if you do:

app1 = Celery()

@app1.task
def test():
pass

app2 = Celery()

# the test task will be registered in both apps:

assert app1.tasks[test.name]
assert app2.tasks[test.name]


# However, the name ‘test’ will always refer to the instance bound to the ‘app1’
# app, so it will be configured using app1’s configuration:

assert test.app is app1



# The @shared_task decorator returns a proxy that always uses the task instance
# in the current_app:


app1 = Celery()

@shared_task
def test():
    pass
assert test.app is app1


app2 = Celery()
assert test.app is app2