Overview
========

skyl2 is an aggressively under-engineered blogging platform on Django 1.6.
It's just ReST. It's just "blogging". There are no features.
It should be simple enough to hack the source if you want to do something else.
You can make a few changes and push it out to a server with
a command or two.

Features
========

ReST in the admin with live preview. Syntax highlighting. Disqus comments.

Modify the source
=================

* Edit `feeder/templates/disqus.html` and put your `disqus_shortname` there.
* Change the git repo in deploy/roles/web/tasks.yml to your repo.
* Put in your local_settings.py.j2 template

This will need a `SECRET_KEY` and lives at
`deploy/roles/web/templates/local_settings.py.j2`

.. sourcecode:: python

    SECRET_KEY = 'gobbledygook'
    OAUTH_TOKEN = "Twitter key"
    OAUTH_SECRET = "Twitter oauth secret"
    CONSUMER_KEY = "Twitter consumer"
    CONSUMER_SECRET = "stuff"
    from twitter import Twitter, OAuth
    TWITTER = Twitter(
        auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    )


Ship
====

Deployment with ansible assumes a recent ubuntu/debian (TODO - yum).
You don't need to use EC2. But, you can.
If you have your own way, skip the provisioning gloss-over below.

Provision (EC2)
===============

You can use EC2 and get stuff provisioned for you too.
The provision.yml playbook is provided just as a convenience.
If you have a machine you can ssh into, skip all this.
Get AWS setup, `export AWS_ACCESS_KEY`, `export AWS_SECRET_KEY`,
`export EC2_URL` in your bash shell.
Create a keypair for the right region.

.. sourcecode:: bash

    # no .pem on the key name.
    ansible-playbook provision.yml -e "key_name=skyl"

If you provisioned your machine in this way, you probably will want
to save the json output of the provisioning task somewhere.

There are a lot of nuances to AWS permissions/regions/etc
which are beyond the scope of this readme.

Put your .pem identity file into your .ssh/config, perhaps

.. sourcecode::

    IdentityFile ~/Downloads/skyl.pem

Deploy
======

Once you can ssh into you instance, put the IP in your hosts file
under the `skyl2` group.

.. sourcecode::

    [skyl2]
    54.200.210.238 ansible_ssh_user=ubuntu

Now, you can run the main playbook against this one server.

.. sourcecode:: bash

    ansible-playbook main.yml
