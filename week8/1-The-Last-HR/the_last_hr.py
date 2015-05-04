import requests


class GatherInfo:

    def __init__(self, url):
        self.url = url
        self.courses = set()
        self.students = []
        self.info = self.gather_info()

    def gather_info(self):
        r = requests.get(self.url)
        for student in r.json():
            name = student["name"]
            github = student["github"]
            courses = [course["name"] for course in student["courses"]]
            self.students.append({
                                "name": name,
                                "courses": courses,
                                "github": github,
                                })

    def get_student_and_github(self):
        result = []
        for student in self.students:
            result.append((student["name"], student["github"]))
        return result

    def get_student_and_course(self):
        result = []
        for student in self.students:
            result.append((student["name"], student["courses"]))
        return result

    def get_all_courses(self):
        result = set()
        for student in self.students:
            for course in student["courses"]:
                result.add((course, ))
        result = list(result)
        return result

    def get_most_attending_students(self):
        result = set()
        cool_students = []
        for student in self.students:
            result.add(len(student["courses"]))
        max_course_count = max(result)
        for student in self.students:
            if len(student["courses"]) == max_course_count:
                cool_students.append(student["name"])
        return cool_students
