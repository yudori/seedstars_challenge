from jenkinsapi.jenkins import Jenkins

import click
from models import save_job, print_jobs, Job


@click.group()
def main():
    pass


@click.command("show-jobs")
def get_jobs():
    """
    Prints saved jobs from database
    """
    print_jobs()


@click.command("save-jobs")
@click.option('--address', default="http://localhost:8080/", prompt='Server Address',
              help='The address of the Jenkins Server')
@click.option('--username', default=None, prompt='Username',
              help='Your jenkins username')
@click.option('--password', default=None, prompt='Password', hide_input=True,
              help='Your jenkins password')
def save_jobs(address, username, password):
    """
    stores list of jobs from a given jenkins instance
    """
    try:
        server = Jenkins(address, username=username, password=password)
        for job_name, job_instance in server.get_jobs():
            job = Job(job_instance.name, str(job_instance.is_enabled()))
            save_job(job)
            click.echo("{} saved to database".format(job.job_name))
    except:
        click.echo("Oops! Something went wrong \n"
                   "Please check that all parameters are valid")


main.add_command(get_jobs)
main.add_command(save_jobs)