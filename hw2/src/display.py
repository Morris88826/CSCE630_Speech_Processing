import base64
from pathlib import Path
from IPython.display import HTML, display

def audio_player(path):
    with open(path, "rb") as f:
        audio_data = base64.b64encode(f.read()).decode("utf-8")

    return (
        f'<audio controls preload="none" style="width:180px;">'
        f'<source src="data:audio/wav;base64,{audio_data}" type="audio/wav">'
        f'</audio>'
    )


def display_audio_table(effects, headers, results):
    html = """
    <div style="overflow-x:auto;">
    <table style="border-collapse:collapse; text-align:center;">
    <thead><tr>
    """

    for header in headers:
        html += f'<th style="padding:12px; border:1px solid #ccc;">{header}</th>'

    html += "</tr></thead><tbody>"

    for original_path, modifications in results.items():
        modified = dict(modifications)

        html += "<tr>"

        # First column: original audio
        html += (
            '<td style="padding:10px; border:1px solid #ccc;">'
            f'<b>{Path(original_path).stem}</b><br>'
            f'{audio_player(original_path)}'
            '</td>'
        )

        # Remaining columns: modified audio
        for effect in effects:
            path = modified[effect]
            html += (
                '<td style="padding:10px; border:1px solid #ccc;">'
                f'{audio_player(path)}'
                '</td>'
            )

        html += "</tr>"

    html += "</tbody></table></div>"

    display(HTML(html))