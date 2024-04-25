# main.py
import uvicorn
from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.requests import Request
from starlette.middleware.sessions import SessionMiddleware
import secrets

app = FastAPI()


# SessionMiddleware
app.add_middleware(
    SessionMiddleware,
    secret_key=secrets.token_urlsafe(32),  # 生成一個隨機的安全金鑰
    https_only=True,  # 只允許 https
    max_age=120  # session過期時間
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# 首頁
@app.get("/")
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# 登入頁面
@app.post("/signin")
async def post_signin(request: Request, username: str = Form(""), password: str = Form("")):
    # 帳號密碼都是test
    if username == "test" and password == "test":
        # 登入成功，將使用者資訊存入 session
        request.session["user"] = username
        # 記錄session後，才跳轉到/member；要用status_code=303不然會出現127.0.0.1:64961 - "POST /member HTTP/1.1" 405 Method Not Allowed
        return RedirectResponse(url="/member", status_code=303)

    else:
        # 登入失敗會跳轉到/error
        return RedirectResponse(url="/error?message=請輸入帳號和密碼", status_code=303)


# 登入成功/member
@app.get("/member", response_class=HTMLResponse)
async def get_member(request: Request):
    # 檢查session是否有user，檢查登入狀態
    user = request.session.get("user")
    if not user:
        # 如果没有，導回首頁
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse("signin_success.html", {"request": request})


# 登入失敗/error
@app.get("/error", response_class=HTMLResponse)
async def get_error(request: Request, message: str):
    return templates.TemplateResponse("wrong_username_or_password.html", {"request": request, "message": message})


@app.get("/signout")
async def get_signout(request: Request):
    # 移除session中的user資訊
    request.session.pop("user", None)
    # 導回首頁
    return RedirectResponse(url="/", status_code=303)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
