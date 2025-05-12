# Copyright © 2024 Bret Brown
# SPDX-License-Identifier: MIT

cmake_minimum_required(VERSION 3.23)
project(zerocode
  VERSION 1.0.0
  DESCRIPTION "A C++ project with no code"
  LANGUAGES CXX
)

option(ZEROCODE_ENABLE_WARNINGS "Enable compiler warnings" ON)
option(ZEROCODE_BUILD_TESTS "Build tests" OFF)

if(ZEROCODE_ENABLE_WARNINGS)
  if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    add_compile_options(-Wall -Wextra -Wpedantic)
  elseif(CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
    add_compile_options(/W4)
  endif()
endif()

add_subdirectory(src/zerocode)

if(ZEROCODE_BUILD_TESTS)
  include(CTest)
  enable_testing()
  add_subdirectory(test/zerocode)
endif()
