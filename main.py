# main.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# FastAPI 객체를 만들고
app=FastAPI()

# templates 폴더 연결 (Jinja2 를 사용해서 응답하기 위함)
templates = Jinja2Templates(directory="templates")

# 클라이언트가 "/" 최상위 경로 요청을 해오면 응답할 내용
@app.get("/", response_class=HTMLResponse)
def home(request:Request):
    result = templates.TemplateResponse("index.html",{"request":request, "fortuneToday":"동쪽으로가면 귀인을 만나요"})
    return result
