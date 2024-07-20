from fastapi import FastAPI, Query, Path
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

count = 0
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# http://127.0.0.1:8001/public/*
app.mount('/public', StaticFiles(directory='public'))


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    global count
    return templates.TemplateResponse(name="index.html", request=request, context={"count": str(count)})


@app.get('/redirect', response_class=RedirectResponse, status_code=302)
def redirect():
    return 'https://www.google.ru/'


@app.get('/users/{user_id}', response_class=HTMLResponse)
def users(
        request: Request,
        user_id=Path(),
        name=Query(default='Abama', min_length=0, max_length=100),
):
    return (templates.TemplateResponse(
        name="user.html",
        request=request,
        context={"name": name, "user_id": user_id}
    ))


@app.post('/incrementCount', response_class=JSONResponse)
def increment_count():
    global count
    count += 1
    return {"count": count}


@app.post('/decrementCount', response_class=JSONResponse)
def decrement_count():
    global count
    count -= 1
    return {"count": count}
