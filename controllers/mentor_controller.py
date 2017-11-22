from models.user_container import UserContainer
from models.assignment import Assignment
from models.assignment_container import AssignmentContainer
from views.mentor_view import MentorView
from models.group_container import GroupContainer
from models.group import Group
from models.student import Student
from datetime import date
import traceback


class MentorController:

    def __init__(self):
        ...

    def start(self):
        exit_program = False
        while not exit_program:
            try:
                option = MentorView.display_menu()
                if option == '1':
                    self.show_students()
                elif option == '2':
                    self.add_assignment()
                elif option == '3':
                    self.show_assignments()
                elif option == '4':
                    self.grade_assignment()
                elif option == '5':
                    self.check_attendance()
                elif option == '6':
                    self.change_student_data()
                elif option == '7':
                    self.promote_user_to_student()
                elif option == '8':
                    self.edit_groups()
                elif option == '9':
                    self.edit_groups(False)
                elif option == '0':
                    exit_program = True
                else:
                    MentorView.show_invalid_input()
            except IndexError:
                MentorView.display_index_error()
            except ValueError as error:
                if 'invalid literal' in str(error):
                    MentorView.show_invalid_input()
                else:
                    MentorView.display_date_error()
            except AttributeError:
                MentorView.display_group_exists()
            except Exception:
                tb = traceback.format_exc()
                print(tb)
                input()

        UserContainer.get_instance().save_users_to_file()
        exit()

    def show_students(self):
        students_list = UserContainer.get_instance().get_students_list()
        MentorView.display_students_list(students_list)

    def show_assignments(self):
        assignments = AssignmentContainer.get_instance().get_assignments_list()
        MentorView.display_assignments(assignments)

    def add_assignment(self):
        students_list = UserContainer.get_instance().get_students_list()
        deadline, title, description = MentorView.return_assignment_values()
        new_assignment = Assignment(deadline, title, description)
        AssignmentContainer.get_instance().add_assignment(new_assignment)
        for student in students_list:
            student.add_student_assignment(deadline, title, description)

    def grade_assignment(self):
        students_list = UserContainer.get_instance().get_students_list()
        if not students_list:
            MentorView.display_not_enough_data()
            return
        student_index = MentorView.get_student_index(students_list)
        student_index = int(student_index)
        student = students_list[student_index]
        assignment_index, grade = MentorView.get_grade_values(student)
        students_list = UserContainer.get_instance().get_students_list()
        students_list[student_index].assignments[assignment_index].grade = grade

    def check_attendance(self):
        groups = GroupContainer.get_instance().get_groups_list()
        if groups:
            group_index = MentorView.get_group_index(groups)
            group_index = int(group_index)
            group = groups[group_index]
        else:
            MentorView.display_not_enough_data()
            return
        group_students = GroupContainer.get_instance().get_group(group.name).get_student_list()
        for student in group_students:
            student_present = MentorView.get_presence(student)
            if student_present:
                student.attendance += 1
        UserContainer.get_instance().save_users_to_file()
        group.attendance_check_count += 1
        GroupContainer.get_instance().save_groups_to_file()

    def change_student_data(self):
        value_changing = True
        students_list = UserContainer.get_instance().get_students_list()
        if not students_list:
            MentorView.display_not_enough_data()
            return
        student_index = MentorView.get_student_index(students_list)
        student_index = int(student_index)
        student = students_list[student_index]
        while value_changing:
            value_to_change = MentorView.get_student_value_to_change()
            if value_to_change == '1':
                student.login = MentorView.get_new_value('login')
            elif value_to_change == '2':
                student.name = MentorView.get_new_value('name')
            elif value_to_change == '3':
                student.password = MentorView.get_new_value('password')
            elif value_to_change == '4':
                additional_days = MentorView.get_additional_attendance()
                student.attendance += int(additional_days)
                MentorView.show_invalid_input()
            elif value_to_change == '5':
                groups = GroupContainer.get_instance().get_groups_list()
                if not groups:
                    MentorView.display_not_enough_data()
                    return
                group_index = MentorView.get_group_index(groups)
                group_index = int(group_index)
                GroupContainer.get_instance().add_student_to_group(groups[group_index].name, student)
                UserContainer.get_instance().save_users_to_file()
            elif value_to_change == '6':
                return
            else:
                MentorView.show_invalid_input()

    def promote_user_to_student(self):
        not_assigned_users = UserContainer.get_instance().get_not_assigned_users_list()
        user_index = MentorView.get_user_index(not_assigned_users)
        user_index = int(user_index)
        user_to_assign = not_assigned_users[user_index]
        name = user_to_assign.name
        login = user_to_assign.login
        password = user_to_assign.password
        phone_number = user_to_assign.phone_number
        email = user_to_assign.email
        UserContainer.get_instance().remove_user(user_to_assign)
        if not user_to_assign:
            return
        user_to_assign = Student(name, login, password, phone_number, email)
        UserContainer.get_instance().add_user(user_to_assign)

    def edit_groups(self, create_new=True):
        if create_new:
            new_group_name = MentorView.get_group_name()
            group = Group(new_group_name)
            GroupContainer.get_instance().add_group(group.name)
        else:
            groups_list = GroupContainer.get_instance().get_groups_list()
            group_index = int(MentorView.get_group_index(groups_list))
            new_group_name = MentorView.get_group_name()
            for group in groups_list:
                if group.name == new_group_name:
                    raise AttributeError
            groups_list[group_index].name = new_group_name



