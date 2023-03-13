from docx import Document


def main() -> str:
    # 读取文档
    doc = Document("data60.docx")
    # 获取文档中的所有段落
    paras = doc.paragraphs

    return [para.text for para in paras if "山东" in para.text if "烟台" in para.text][0]


print(main())
