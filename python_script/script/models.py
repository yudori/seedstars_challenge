import sqlite3
from datetime import datetime


conn = sqlite3.connect('jenkins_data.db')


class Job:
    def __init__(self, job_name, status, time_last_checked=datetime.utcnow()):
        self.job_name = job_name
        self.status = status
        self.time_last_checked = time_last_checked

    def __str__(self):
        return "Job = {}\nEnabled = {}\nTime Last Checked = {}\n"\
            .format(self.job_name, self.status, self.time_last_checked)


def create_table():
    with conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS jobs
                     (job_name text, status text,
                      time_last_checked text);
                      ''')
        c.execute('''CREATE UNIQUE INDEX IF NOT EXISTS idx ON jobs
                      (job_name);''')
        conn.commit()


def save_job(job):
    with conn:
        c = conn.cursor()
        values = (job.job_name, job.status, datetime.utcnow())
        c.execute("REPLACE INTO jobs VALUES (?,?,?)", values)
        conn.commit()


def print_jobs():
    with conn:
        c = conn.cursor()
        for row in c.execute('SELECT * FROM jobs ORDER BY time_last_checked'):
            print Job(row[0], row[1], row[2])

