cmake_minimum_required(VERSION 3.26)
project(hellbindah VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(hellbindah src/main.cpp)

target_compile_features(hellbindah PRIVATE cxx_std_23)

if (MSVC)
  target_compile_options(hellbindah PRIVATE /W4 /permissive-)
else()
  target_compile_options(hellbindah PRIVATE -Wall -Wextra -Wpedantic)
endif()

enable_testing()
add_test(NAME hellbindah_boot COMMAND hellbindah --self-test)
