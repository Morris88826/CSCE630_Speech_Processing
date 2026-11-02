import base64
from pathlib import Path
from IPython.display import HTML, display

def audio_player(path):
    with open(path, "rb") as f:
        audio_data = base64.b64encode(f.read()).decode("utf-8")

    return (
        '<audio controls preload="none" style="width:180px;">'
        f'<source src="data:audio/wav;base64,{audio_data}" type="audio/wav">'
        '</audio>'
    )


def display_audio_table(results):
    headers = list(results.keys())
    n_rows = len(results["Original"])

    html = """
    <div style="overflow-x:auto;">
    <table style="border-collapse:collapse; text-align:center;">
    <thead><tr>
    """

    for header in headers:
        html += f'<th style="padding:12px; border:1px solid #ccc;">{header}</th>'

    html += "</tr></thead><tbody>"

    for i in range(n_rows):
        html += "<tr>"

        for header in headers:
            path = results[header][i]

            # Show filename only in the original column
            name = (
                f"<b>{Path(path).stem}</b><br>"
                if header == "Original" else ""
            )

            html += (
                '<td style="padding:10px; border:1px solid #ccc;">'
                f'{name}{audio_player(path)}'
                '</td>'
            )

        html += "</tr>"

    html += "</tbody></table></div>"

    display(HTML(html))