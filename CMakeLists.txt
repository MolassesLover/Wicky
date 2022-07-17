cmake_minimum_required(VERSION 3.8)
project(Wicky)

find_package(PythonLibs)

execute_process(
    OUTPUT_VARIABLE testVariable
    COMMAND bash -c "cd ${CMAKE_CURRENT_SOURCE_DIR}/Source && cython Wicky.py && cython Start.py"
)

set (SOURCE_FILES
    Source/Wicky.c
    Source/Start.c
)

include_directories(${PYTHON_INCLUDE_DIRS})

add_library(Wicky SHARED 
${SOURCE_FILES}
)

target_link_libraries(Wicky ${PYTHON_LIBRARIES})