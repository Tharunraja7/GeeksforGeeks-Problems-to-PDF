import requests
from bs4 import BeautifulSoup
from weasyprint import HTML, CSS
import json

def generate_pdf(urls, pdf_name):  # Add pdf_name as a parameter
    html_content = ""
    for i, url in enumerate(urls, 1):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        script_tag = soup.find('script', {'id': '__NEXT_DATA__', 'type': 'application/json'})
        json_data = json.loads(script_tag.string)
        problem_resource = url.split('/')[-2]
        path_to_key = ['props', 'pageProps', 'initialState', 'problemApi', 'queries', f'getProblemDetails({{"isProblemPublic":true,"probResource":"{problem_resource}","problemBatchSlug":null,"problemTrackSlug":null}})', 'data']
        data = json_data
        for key in path_to_key:
            data = data[key]
        html_content += f"<div style='page-break-after: always; overflow:auto;'><h1 style='color: red; font-size: 30px;'>{i}. {data['problem_name']}</h1><p>{data['problem_question']}</p></div>"
        print(f"{i} links scrapped out of {len(urls)}")

    HTML(string=html_content).write_pdf(f"{pdf_name}.pdf", stylesheets=[CSS(string="body { font-family: serif; }")])  # Use the pdf_name for the output file
