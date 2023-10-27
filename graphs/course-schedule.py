def course_schedule(num_courses, pre_requisites):
    # create all the course and its pre_requisites
    courses_dict = {i: [] for i in range(num_courses)}
    for course, pre_req in pre_requisites:
        courses_dict[course].append(pre_req)

    visited_course = set()

    def dfs(curr_course):
        if curr_course in visited_course:
            return False
        # if it does not have any pre-req then return True
        if not courses_dict[curr_course]:
            return True

        visited_course.add(curr_course)
        # loop through all its pre-req
        for pre_req_course in courses_dict[curr_course]:
            if not dfs(pre_req_course):
                return False

        # remove the visited course from the set
        visited_course.remove(curr_course)

        # empty all the pre-req when the course req-req are looped through
        courses_dict[curr_course] = []

        # if all the pre-req can be completed
        return True

    # need to check for all the given courses
    for course in range(num_courses):
        if not dfs(course):
            return False

    return True


numCourses = 5
prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
res = course_schedule(numCourses, prerequisites)
print(res)
