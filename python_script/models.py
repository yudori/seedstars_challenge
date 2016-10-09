import sqlite3
from datetime import datetime

conn = sqlite3.connect('jenkins_data.db')


class Job:
    def __init__(self, address, job_name, status,
                 time_last_checked):
        self.address = address
        self.job_name = job_name
        self.status = status
        self.time_last_checked = time_last_checked


def create_table():
    c = conn.cursor()

    c.execute('''CREATE TABLE jobs
                 (address text, job_name text, status integer,
                  time_last_checked text)''')

    conn.commit()
    #conn.close()


def save_job(job):
    c = conn.cursor()

    values = (job.address, job.job_name, job.status, datetime.utcnow())

    c.execute("INSERT INTO jobs VALUES (?,?,?,?)", values)

    conn.commit()
    #conn.close()


def print_jobs():
    c = conn.cursor()
    for row in c.execute('SELECT * FROM jobs ORDER BY time_last_checked'):
        print row + "\n"

