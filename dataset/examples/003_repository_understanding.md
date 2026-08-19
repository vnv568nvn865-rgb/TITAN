# عينة التدريب 003 — فهم مشروع متعدد الملفات

## المعرّف
003_repository_understanding

## الفئة
فهم المشاريع

## مستوى الصعوبة
متوسط

## المهمة
يوجد مشروع Python صغير لإدارة قائمة مهام.

يتكون المشروع من ثلاثة ملفات:

app.py
tasks.py
storage.py

المطلوب فهم بنية المشروع وتحديد المكان الصحيح لإضافة دالة تسمح بحذف مهمة من قائمة المهام.

## حالة المشروع

### الملف app.py

from tasks import add_task, list_tasks
from storage import save_tasks, load_tasks

tasks = load_tasks()

while True:
    command = input("الأمر: ")

    if command == "add":
        title = input("اسم المهمة: ")
        add_task(tasks, title)
        save_tasks(tasks)

    elif command == "list":
        list_tasks(tasks)

    elif command == "exit":
        break

## الملف tasks.py

def add_task(tasks, title):
    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)


def list_tasks(tasks):
    for index, task in enumerate(tasks):
        print(index, task["title"], task["completed"])

## الملف storage.py

import json

FILE_NAME = "tasks.json"


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

## السياق
المشروع يفصل بين مسؤوليات مختلفة:

app.py مسؤول عن تشغيل البرنامج والتفاعل مع المستخدم.

tasks.py يحتوي على العمليات المتعلقة بالمهام.

storage.py مسؤول عن حفظ البيانات وقراءتها.

المطلوب إضافة ميزة حذف مهمة دون كسر هذا التصميم.

## المتطلبات
1. تحديد الملف المناسب لإضافة منطق حذف المهمة.
2. عدم وضع منطق إدارة المهام داخل storage.py.
3. عدم وضع منطق حذف المهمة بالكامل داخل app.py.
4. إنشاء دالة مستقلة لحذف المهمة.
5. تعديل app.py لاستخدام الدالة الجديدة.
6. الحفاظ على وظيفة إضافة المهام وعرضها وحفظها.

## التحليل
العملية المطلوبة هي عملية منطقية مرتبطة بالمهام نفسها، لذلك المكان الأنسب لها هو tasks.py.

لا ينبغي وضعها في storage.py لأن هذا الملف مسؤول عن التخزين وليس عن منطق إدارة المهام.

ولا ينبغي وضع منطق الحذف بالكامل داخل app.py لأن ذلك سيجعل ملف التشغيل مسؤولًا عن تفاصيل منطقية تخص المهام.

لذلك يجب إضافة دالة delete_task داخل tasks.py، ثم استيرادها واستخدامها في app.py.

## الخطة
1. فتح tasks.py.
2. إنشاء دالة delete_task.
3. جعل الدالة تستقبل قائمة المهام ورقم المهمة.
4. التحقق من أن الرقم ضمن حدود القائمة.
5. حذف المهمة عند وجود رقم صحيح.
6. تعديل app.py لاستيراد الدالة.
7. إضافة أمر delete إلى واجهة البرنامج.
8. حفظ القائمة بعد الحذف.
9. اختبار الإضافة والعرض والحذف والحالات غير الصحيحة.

## التنفيذ

### تعديل tasks.py

def add_task(tasks, title):
    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)


def list_tasks(tasks):
    for index, task in enumerate(tasks):
        print(index, task["title"], task["completed"])


def delete_task(tasks, index):
    if index < 0 or index >= len(tasks):
        return False

    del tasks[index]
    return True

### تعديل app.py

from tasks import add_task, list_tasks, delete_task
from storage import save_tasks, load_tasks

tasks = load_tasks()

while True:
    command = input("الأمر: ")

    if command == "add":
        title = input("اسم المهمة: ")
        add_task(tasks, title)
        save_tasks(tasks)

    elif command == "list":
        list_tasks(tasks)

    elif command == "delete":
        index = int(input("رقم المهمة: "))

        if delete_task(tasks, index):
            save_tasks(tasks)
            print("تم حذف المهمة.")
        else:
            print("رقم المهمة غير صحيح.")

    elif command == "exit":
        break

## التحقق

### الاختبار الأول — حذف مهمة موجودة

قائمة البداية:

[
    {"title": "قراءة", "completed": False},
    {"title": "برمجة", "completed": False},
    {"title": "رياضة", "completed": False}
]

رقم المهمة:

1

النتيجة المتوقعة:

يتم حذف مهمة "برمجة".

النتيجة:

تم حذف المهمة بنجاح.

الحالة:

نجاح

### الاختبار الثاني — رقم غير موجود

رقم المهمة:

10

النتيجة المتوقعة:

يتم رفض العملية دون حذف أي مهمة.

النتيجة:

رقم المهمة غير صحيح.

الحالة:

نجاح

### الاختبار الثالث — رقم سالب

رقم المهمة:

-1

النتيجة المتوقعة:

يتم رفض العملية.

النتيجة:

رقم المهمة غير صحيح.

الحالة:

نجاح

### الاختبار الرابع — التخزين

بعد حذف مهمة صحيحة، يتم استدعاء save_tasks.

النتيجة:

يتم حفظ القائمة الجديدة.

الحالة:

نجاح

## النتيجة النهائية
تمت إضافة ميزة حذف المهام مع الحفاظ على فصل المسؤوليات بين ملفات المشروع.

منطق إدارة المهام موجود في tasks.py.

التفاعل مع المستخدم موجود في app.py.

التخزين موجود في storage.py.

## الدروس المستخلصة
1. يجب فهم بنية المشروع قبل تعديل الكود.
2. يجب وضع التعديل في المكان الذي يتوافق مع مسؤولية الملف.
3. فصل المسؤوليات يقلل التعقيد.
4. تعديل مشروع متعدد الملفات يتطلب تتبع العلاقات بين الملفات.
5. يجب اختبار الملفات المتأثرة بعد التعديل.
6. يجب الحفاظ على الوظائف الموجودة وعدم كسرها أثناء إضافة ميزة جديدة.

## تقييم الجودة
الصحة: عالية
فهم المشروع: عالٍ
جودة الخطة: عالية
جودة التنفيذ: عالية
التحقق: مكتمل
الالتزام بالمتطلبات: كامل
قابلية التعلم: عالية
