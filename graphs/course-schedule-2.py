def course_schedule(num_courses, pre_requisites):
    # create all the course and its pre_requisites
    courses_dict = {i: [] for i in range(num_courses)}
    for course, pre_req in pre_requisites:
        courses_dict[course].append(pre_req)

    result = []
    visited_course = set()
    # if a course is already in the current path of courses then a cycle is detected
    curr_path = set()

    def dfs(curr_course):
        if curr_course in curr_path:
            return False
        if curr_course in visited_course:
            return True

        # add course to the current path
        curr_path.add(curr_course)

        # call dfs on its pre-req
        for pre_req_course in courses_dict[curr_course]:
            if not dfs(pre_req_course):
                return False
        curr_path.remove(curr_course)

        # all its pre-req have been visited so add the current course to the result and mark as visited
        visited_course.add(curr_course)
        result.append(curr_course)

        return True

    for course in range(num_courses):
        if not dfs(course):
            return []

    return result


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
res = course_schedule(numCourses, prerequisites)
print(res)
