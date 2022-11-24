cmake_minimum_required(VERSION 3.15)
project(usage CXX)

add_custom_command(
    OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp
    COMMAND cppfront ${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp2
    COMMENT "Run cppfront on .cpp2 files"
)

find_package(cppfront REQUIRED CONFIG)

add_executable(${CMAKE_PROJECT_NAME} ${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp)
set_property(TARGET ${CMAKE_PROJECT_NAME} PROPERTY CXX_STANDARD 20)
target_link_libraries(${CMAKE_PROJECT_NAME} cppfront::cppfront)

install(TARGETS ${CMAKE_PROJECT_NAME})
