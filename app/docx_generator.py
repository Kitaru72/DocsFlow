from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH as ALIGN


STUDENT_REPORT_PATH = "output/student_report.docx"


def create_document_data(student, report):
    return {
        "student": student,
        "report": report,
    }


def save_student_report(report_data, path=STUDENT_REPORT_PATH):
    doc = Document()

    student = report_data["student"]
    report = report_data["report"]

    style = doc.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(14)

    for _ in range(6):
        doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = ALIGN.CENTER
    run_discipline = p.add_run(report["discipline"])
    run_discipline.font.size = Pt(18)
    run_discipline.bold = True

    p = doc.add_paragraph()
    p.alignment = ALIGN.CENTER
    run_lab_number = p.add_run(f"Лабораторная работа №{report['lab_number']}")
    run_lab_number.bold = True

    p = doc.add_paragraph()
    p.alignment = ALIGN.CENTER
    run_topic = p.add_run(f"Тема: \"{report['topic']}\"")
    run_topic.bold = True

    for _ in range(7):
        doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = ALIGN.LEFT
    p.add_run(f"Выполнил: {student['full_name']}")

    p = doc.add_paragraph()
    p.alignment = ALIGN.LEFT
    p.add_run(f"Учебная группа: {student['group']} {student['faculty']}")

    for _ in range(3):
        doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = ALIGN.CENTER
    run_city = p.add_run("Нижевартовск, 2026")
    run_city.bold = True

    p = doc.add_paragraph()
    p.alignment = ALIGN.CENTER
    run_task_heading = p.add_run("Задания")
    run_task_heading.font.size = Pt(18)
    run_task_heading.bold = True

    for num, task in enumerate(report["tasks"], start=1):
        p = doc.add_paragraph()
        run = p.add_run(f"Задание {num}. ")
        run.bold = True
        run = p.add_run(f"{task}")
        run.bold = False

    try:
        doc.save(path)
    except OSError:
        raise ValueError(f"Не удалось сохранить файл {path}")
