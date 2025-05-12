# Copyright © 2024 Bret Brown
# SPDX-License-Identifier: MIT

cmake_minimum_required(VERSION 3.23)
project(zerocode
  VERSION 1.0.0
  DESCRIPTION "A C++ project with no code"
  LANGUAGES CXX
)
include(CTest)

add_subdirectory(src/zerocode)
add_subdirectory(test/zerocode)

include(CMakePackageConfigHelpers)

write_basic_package_version_file(
  "${CMAKE_CURRENT_BINARY_DIR}/zerocode-config-version.cmake"
  VERSION ${PROJECT_VERSION}
  COMPATIBILITY SameMajorVersion
)

configure_package_config_file(
  "${CMAKE_CURRENT_SOURCE_DIR}/cmake/zerocode-config.cmake.in"
  "${CMAKE_CURRENT_BINARY_DIR}/zerocode-config.cmake"
  INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/zerocode
)

install(FILES
  "${CMAKE_CURRENT_BINARY_DIR}/zerocode-config.cmake"
  "${CMAKE_CURRENT_BINARY_DIR}/zerocode-config-version.cmake"
  DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/zerocode
  COMPONENT libzerocode-dev
)

install(EXPORT zerocode
  FILE zerocodeTargets.cmake
  DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/zerocode"
  COMPONENT libzerocode-dev
  NAMESPACE zerocode::
)
