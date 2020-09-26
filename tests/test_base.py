from flask_testing import TestCase
from flask import current_app, url_for

from main import app

class MainTest(TestCase):

  def create_app(self):
    app.config['TESTING'] = True            # The testing enviroment is activated
    app.config['WTF_CSRF_ENABLE'] = False   # It is indicated that the session token it is not necessary

    return app

  # Verify if the app flask app exists
  def test_app_exists(self):
    self.assertIsNotNone(current_app)

  # Verify if the app is in the test enviroment
  def test_app_in_test_mode(self):
    self.assertTrue(current_app.config['TESTING'])

  # Verify if the index redirect to hello
  def test_index_redirects(self):
    response = self.client.get(url_for('index'))

    self.assertRedirects(response, url_for('hello'))

  # Verify if hello returns 200 when a get is made it
  def test_hello_get(self):
    response = self.client.get(url_for('hello'))

    self.assert200(response)

  # Verify if the post to hello es working ok
  def test_hello_post(self):
    fake_form = {
      'username': 'fake',
      'password': 'fake-password'
    }
    response = self.client.post(url_for('hello'), data=fake_form)

    self.assertRedirects(response, url_for('index'))

  # Verify if the authentication Blueprints exists
  def test_auth_blueprint_exists(self):
    self.assertIn('auth', self.app.blueprints) # Here is where Flask save all the blueprints

  # Verify if the auth login route return a 200 code
  def test_auth_login_get(self):
    response = self.client.get(url_for('auth.login'))

    self.assert200(response)

  # Verify if the login template is returned
  def test_auth_login_template(self):
    self.client.get(url_for('auth.login'))
    self.assertTemplateUsed('login.html')
