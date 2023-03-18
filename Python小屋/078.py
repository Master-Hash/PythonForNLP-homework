from operator import itemgetter
from typing import Tuple, Dict
from docx import Document
from docx.shared import RGBColor


def main() -> Tuple[str, str, str]:
    # read the docx file
    doc = Document("data78.docx")
    # get color used
    # color_used = ["FF0000", "FF0000", "FF0000", "FF0000", "FF0000", "E36C0A"]
    color_used = [
        str(r.font.color.rgb)
        for p in doc.paragraphs
        for r in p.runs
        if r.font.color.rgb
        if str(r.font.color.rgb) != "000000"
    ]
    d: Dict[str, int] = {}
    for i in color_used:
        d[i] = d.get(i, 0) + 1
    # get the 3 most used color
    e = sorted(d.items(), key=itemgetter(1), reverse=True)
    return tuple([i[0] for i in e][:3])


print(main())
