import justpy as jp

from jsoneditor_on_vue import jsoneditorcomponents as jecomp

jeopts = {
    'jeoptions': 'here'
}


def launch_jsonEditor():
    wp = jp.QuasarPage()
    wp.head_html = """
    <script src = "https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.5.1/chart.js"></script >\n    
    <script src="https://cdn.tailwindcss.com/"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/inter-ui@3.13.1/inter.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jsoneditor/9.6.0/jsoneditor.min.css"></link>
    
    <script src="https://cdn.jsdelivr.net/npm/jsoneditor"></script>    
    """
    wp.css = 'body { font-family: Inter; }'
    wp.tailwind = False
    #wp.head_html = """<script src = "https://cdn.jsdelivr.net/npm/chart.js" > </script >\n    <link href = "https://unpkg.com/tailwindcss/dist/tailwind.min.css" rel = "stylesheet" >"""

    panel_jsonEditor_ = jecomp.JsonEditor_(
        "panel_jsonEditor", pcp=[], options=jeopts, jsontext="i am json")
    dbref = panel_jsonEditor_(wp, "")
    return wp


app = jp.app
jp.justpy(launch_jsonEditor, start_server=False)
