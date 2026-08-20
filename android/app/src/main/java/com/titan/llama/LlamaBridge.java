package com.titan.llama;

public class LlamaBridge {

    static {
        System.loadLibrary("titan_native");
    }

    public static native long loadModel(String modelPath);

    public static native void freeModel(long modelHandle);

    public static native String generate(
            long modelHandle,
            String prompt
    );
}
