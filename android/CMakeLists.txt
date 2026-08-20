cmake_minimum_required(VERSION 3.22.1)

project(titan_native)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if(NOT DEFINED LLAMA_SOURCE_DIR)
    message(FATAL_ERROR "LLAMA_SOURCE_DIR is required")
endif()

if(NOT DEFINED LLAMA_BUILD_DIR)
    message(FATAL_ERROR "LLAMA_BUILD_DIR is required")
endif()

add_library(titan_native SHARED
    native_bridge.cpp
)

target_include_directories(titan_native PRIVATE
    "${LLAMA_SOURCE_DIR}/include"
    "${LLAMA_SOURCE_DIR}/ggml/include"
)

target_link_directories(titan_native PRIVATE
    "${LLAMA_BUILD_DIR}/src"
    "${LLAMA_BUILD_DIR}/ggml/src"
)

find_library(log-lib log)

target_link_libraries(titan_native
    llama
    ggml
    ggml-base
    ggml-cpu
    ${log-lib}
)
