cmake_minimum_required(VERSION 3.8)
project(Editor)

find_package(WickedEngine REQUIRED)

set (SOURCE_FILES
	Source/stdafx.cpp
	Source/Editor.cpp
	Source/Editor.h
	Source/stdafx.h
)

if (WIN32)
	list (APPEND SOURCE_FILES
		Source/main_Windows.cpp
		Source/main_Windows.h
		Source/Editor.rc
	)

	add_executable(Editor WIN32 ${SOURCE_FILES})

	target_link_libraries(Editor PUBLIC
		WickedEngine_Windows
	)
else()
	list (APPEND SOURCE_FILES
		Source/main_SDL2.cpp
	)

	add_executable(Editor ${SOURCE_FILES})

	target_link_libraries(Editor PUBLIC
		WickedEngine::WickedEngine
	)
endif ()



if (MSVC)
	set_property(TARGET Editor PROPERTY VS_DEBUGGER_WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}")
endif ()

get_target_property(LIB_DXCOMPILER_LOCATION WickedEngine::dxcompiler IMPORTED_LOCATION)

# Copy content to build folder:
add_custom_command(
	TARGET Editor POST_BUILD
	# Copy the shader library next to the executable
	COMMAND ${CMAKE_COMMAND} -E copy_if_different "${LIB_DXCOMPILER_LOCATION}" "${CMAKE_CURRENT_BINARY_DIR}"
)
