cmake_minimum_required(VERSION 2.6)
project(MissileDefense)

set(SRC_FILES
	src/startup.cpp
	src/Game.cpp
	src/glad.c
	src/gl_frontend.cpp
	src/glutils.cpp
	src/GLMesh.cpp
	src/Controller.cpp
	)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

include_directories("include")
set(GLFW_BUILD_DOCS OFF CACHE BOOL "" FORCE)
set(GLFW_BUILD_TESTS OFF CACHE BOOL "" FORCE)
set(GLFW_BUILD_EXAMPLES OFF CACHE BOOL "" FORCE)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -Wall -std=c++11")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -g -Wall")

file(COPY "shaders" DESTINATION ".")

add_subdirectory("ThirdParty/glfw")

add_executable(missiledefense
	${SRC_FILES}
	)

add_executable(glfw_test
	src/glfw_test.cpp
	src/glad.c
	)
find_package(OpenGL)

target_link_libraries(missiledefense
	glfw
	)
target_link_libraries(glfw_test
	glfw
	)
