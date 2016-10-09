from jenkinsapi.jenkins import Jenkins

import click


def get_server_instance(url, username, password):
    server = Jenkins(url, username=username, password=password)
    return server.version


@click.group()
def main():
    pass


@click.command("get-jobs")
@click.option('--address', prompt='Server Address',
              help='The address of the Jenkins Server')
@click.option('--username', prompt='Username',
              help='Your jenkins username')
@click.option('--password', prompt='Password',
              help='Your jenkins password')
def get_jobs(address, username, password):
    click.echo("{}, {}, {}".format)


if __name__ == "__main__":
    #print get_server_instance()
    main.add_command(get_jobs)