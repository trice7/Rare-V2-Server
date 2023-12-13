# Setup Instructions

Clone repository and run the following two commands within the cloned directory

`pipenv shell`
`pipenv install`

---

If one wasn't created during the installation process, then create a `.vscode` folder.
Ensure you have two files in the `.vscode` folder. `launch.json` and `settings.json`

`settings.json` should have the following code:

```
{
  "python.linting.pylintArgs": [
      "--load-plugins=pylint_django",
      "--django-settings-module=rare.settings",
  ],
}
```

`launch.json` should have the following code:

```
{
  "version": "0.2.0",
  "configurations": [
      {
          "name": "Python: Django",
          "type": "python",
          "request": "launch",
          "program": "${workspaceFolder}/manage.py",
          "args": ["runserver"],
          "django": true,
          "autoReload":{
              "enable": true
          }
      }
  ]
}
```


Run the code to create the basic Django tables

`python manage.py migrate`
