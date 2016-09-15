# deployment_app
Flask app for fast model deployment

## Deployment
```bash
git clone https://github.com/mconley-kaizen/deployment_app.git
python deployment_app/app.py <port> <package name>
```

`package name` can be any module on the local system with a function called `main`

Using `mconley-kaizen/iris_prediction` would look like:

`python deployment_app/app.py 5000 iris_prediction`
