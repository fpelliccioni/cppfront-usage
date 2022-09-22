cmake_minimum_required(VERSION 3.15)
project(usage CXX)

# add_custom_command(
#     OUTPUT ${CMAKE_BINARY_DIR}/generated/main.cpp
#     COMMAND cppfront ${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp2 ${CMAKE_BINARY_DIR}/generated/main.cpp
#     COMMENT "Run cppfront on .cpp2 files"
# )

# add_executable(${CMAKE_PROJECT_NAME} ${CMAKE_BINARY_DIR}/generated/main.cpp)

add_custom_command(
    OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp
    COMMAND cppfront ${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp2
    COMMENT "Run cppfront on .cpp2 files"
)

find_package(cppfront REQUIRED CONFIG)

add_executable(${CMAKE_PROJECT_NAME} ${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp)
set_property(TARGET ${CMAKE_PROJECT_NAME} PROPERTY CXX_STANDARD 20)
target_link_libraries(${CMAKE_PROJECT_NAME} cppfront::cppfront)

# target_include_directories(${CMAKE_PROJECT_NAME} PUBLIC include)

install(TARGETS ${CMAKE_PROJECT_NAME})







# find_package(cppfront REQUIRED CONFIG)

# # TEST_PACKAGE #################################################################
# add_executable(${CMAKE_PROJECT_NAME} test_package.cpp)
# set_property(TARGET ${CMAKE_PROJECT_NAME} PROPERTY CXX_STANDARD 14)
# if(FMT_HEADER_ONLY)
#     target_link_libraries(${CMAKE_PROJECT_NAME} fmt::fmt-header-only)
# else()
#     target_link_libraries(${CMAKE_PROJECT_NAME} fmt::fmt)
# endif()

# # TEST_RANGES ##################################################################
# add_executable(test_ranges test_ranges.cpp)
# set_property(TARGET test_ranges PROPERTY CXX_STANDARD 14)
# if(FMT_HEADER_ONLY)
#     target_link_libraries(test_ranges fmt::fmt-header-only)
# else()
#     target_link_libraries(test_ranges fmt::fmt)
# endif()
