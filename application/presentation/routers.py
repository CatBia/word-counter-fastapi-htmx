
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from presentation.constants import TEMPLATE_FOLDER
from typing import Annotated
from business_rules import services 

main_router = APIRouter(prefix='')

templates = Jinja2Templates(directory=TEMPLATE_FOLDER)

@main_router.get(
    '/',
    response_class=HTMLResponse
)
async def main_view(request:Request):
    return templates.TemplateResponse(
        request=request, name='main.html'
    )
    
@main_router.post(
    '/word_counter',
)
async def word_counter(
    text: Annotated[str, Form()],
):
    count = await services.word_count(text=text)
    return count
    