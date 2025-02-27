def convert_lesson_string_to_list(lessons_selected):
    lessons = lessons_selected.split(',')
    lesson_list = []

    for lesson in lessons:
        lesson = lesson.strip()
        if '-' in lesson:
            start, end = lesson.split('-')
            if start.isdigit() and end.isdigit():
                lesson_list.extend(range(int(start), int(end) + 1))
            else:
                return None
        elif lesson.isdigit():
            lesson_list.append(int(lesson))
        else:
            return None
        
    return lesson_list