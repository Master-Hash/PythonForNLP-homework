from docx import Document


def main() -> int:
    # 读取文档
    doc = Document("data60.docx")
    # 获取文档中的所有表格
    table = doc.tables[0]
    # 返回所有单元格之和
    return sum((int(cell.text) for row in table.rows for cell in row.cells))


print(main())
