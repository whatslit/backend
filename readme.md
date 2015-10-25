# WhatsLit
WhatsLit tonight?

### Git Branching Model
We're using Git to manage all of our source code and production. [Please learn git.](https://www.atlassian.com/git/tutorials/) We have a production branch (master) and a development branch (dev). There are a few things you need to know
 *  If you're developing, you push only to the development branch.
 * If you want to push to production, make a pull request or merge to make a new version.

### Backend-Frontend Protocol
Here will be some documentation for the protocol.

### Setup
Want to set up the repo?
 * [Windows](windows.md)
 * [Mac](mac.md)

### Notes for Setup
 * Check out this [readme](https://github.com/etianen/django-herokuapp) to setup waitress-serve (and heroku in general)

### Django Notes
 * RECOMMENDED: [Writing your first Django app] (https://docs.djangoproject.com/en/1.8/intro/tutorial01/); extremely helpful in understanding directory structures, common methods, postgres integration etc.
 * [Excellent Django REST framework intro](https://github.com/rancavil/django-py3-openshift-quickstart/wiki/Creating-a-REST-service-API-with-Django-and-Django-Rest-Framework)
 * [Django REST framework website](http://www.django-rest-framework.org/#quickstart)
 * If you don't have a local superuser setup for the api-auth, you have to django-ify your superuser. [This section](https://docs.djangoproject.com/en/1.8/intro/tutorial02/) of the tutorial goes over how to do this.
