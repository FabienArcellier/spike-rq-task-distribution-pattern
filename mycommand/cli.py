#!/usr/bin/python
# coding=utf-8

from __future__ import print_function
import time

import click
from redis import Redis
from rq import Queue
from rq.job import Job

from mycommand.utils import count_words_at_url
queue = Queue(connection=Redis())


@click.group()
def cli():
    pass


@click.command('trigger')
@click.option('--url')
def trigger(url):
    job = queue.enqueue(count_words_at_url, url, result_ttl=3600)
    print(job.id)


@click.command('result')
@click.option('--jobid')
def result(jobid):
    job = Job.fetch(jobid, connection=Redis())
    print(job.result)


cli.add_command(trigger)
cli.add_command(result)

if __name__ == '__main__':
    cli()
