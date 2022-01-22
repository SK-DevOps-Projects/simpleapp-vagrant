### Learnings

What is Vagrant and how to setup Vagrantfile
https://learn.hashicorp.com/tutorials/vagrant/getting-started-index?in=vagrant/getting-started

Vagrant boxes is the base image used to create your environment
https://app.vagrantup.com/boxes/search

Many configurations that can be done on the Vagrantfile
- expose a port
- set a box(image)
- set memory & cpu for the environment - https://www.vagrantup.com/docs/providers/virtualbox/configuration#vboxmanage-customizations
- run a script after environment is setup

Deploy Python flask application to production using apache webserver and mod_wsgi
https://flask.palletsprojects.com/en/2.0.x/deploying/mod_wsgi/
https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
https://asdkazmi.medium.com/deploying-flask-app-with-wsgi-and-apache-server-on-ubuntu-20-04-396607e0e40f

apache available site configs and enabled sites
/etc/apache2/sites-available/
/etc/apache2/sites-enabled/

when there are two sites at the same tree for the same domain name the default one needs to be disabled.

apache2 details - https://httpd.apache.org/docs/2.4/