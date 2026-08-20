package com.titan.llama;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.provider.OpenableColumns;
import android.database.Cursor;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;

import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStream;

public class MainActivity extends Activity {

    private static final int PICK_MODEL = 1001;

    private TextView statusText;
    private long modelHandle = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        LinearLayout layout = new LinearLayout(this);
        layout.setOrientation(LinearLayout.VERTICAL);
        layout.setPadding(32, 32, 32, 32);

        TextView title = new TextView(this);
        title.setText("TITAN");
        title.setTextSize(28);

        statusText = new TextView(this);
        statusText.setText("اختر ملف نموذج GGUF");
        statusText.setTextSize(18);

        Button selectButton = new Button(this);
        selectButton.setText("اختيار نموذج GGUF");

        selectButton.setOnClickListener(v -> openModelPicker());

        layout.addView(title);
        layout.addView(statusText);
        layout.addView(selectButton);

        setContentView(layout);
    }

    private void openModelPicker() {
        Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
        intent.addCategory(Intent.CATEGORY_OPENABLE);
        intent.setType("*/*");
        startActivityForResult(intent, PICK_MODEL);
    }

    @Override
    protected void onActivityResult(
            int requestCode,
            int resultCode,
            Intent data) {

        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode != PICK_MODEL ||
                resultCode != RESULT_OK ||
                data == null ||
                data.getData() == null) {
            return;
        }

        Uri uri = data.getData();

        try {
            File modelFile = copyModelToInternalStorage(uri);

            statusText.setText(
                    "تم نسخ النموذج:\n" + modelFile.getName()
            );

            if (modelHandle != 0) {
                LlamaBridge.freeModel(modelHandle);
                modelHandle = 0;
            }

            modelHandle = LlamaBridge.loadModel(
                    modelFile.getAbsolutePath()
            );

            if (modelHandle != 0) {
                statusText.setText(
                        "تم تحميل نموذج GGUF بنجاح."
                );
            } else {
                statusText.setText(
                        "فشل تحميل نموذج GGUF."
                );
            }

        } catch (Exception e) {
            statusText.setText(
                    "خطأ: " + e.getMessage()
            );
        }
    }

    private File copyModelToInternalStorage(Uri uri)
            throws Exception {

        File modelDir = new File(
                getFilesDir(),
                "models"
        );

        if (!modelDir.exists()) {
            modelDir.mkdirs();
        }

        String fileName = getFileName(uri);

        if (fileName == null || fileName.length() == 0) {
            fileName = "model.gguf";
        }

        File outputFile = new File(
                modelDir,
                fileName
        );

        InputStream input =
                getContentResolver().openInputStream(uri);

        FileOutputStream output =
                new FileOutputStream(outputFile);

        byte[] buffer = new byte[1024 * 1024];
        int bytesRead;

        while ((bytesRead = input.read(buffer)) != -1) {
            output.write(buffer, 0, bytesRead);
        }

        output.flush();
        output.close();
        input.close();

        return outputFile;
    }

    private String getFileName(Uri uri) {

        Cursor cursor = getContentResolver().query(
                uri,
                null,
                null,
                null,
                null
        );

        if (cursor != null) {
            try {
                int nameIndex =
                        cursor.getColumnIndex(
                                OpenableColumns.DISPLAY_NAME
                        );

                if (cursor.moveToFirst() &&
                        nameIndex >= 0) {
                    return cursor.getString(nameIndex);
                }

            } finally {
                cursor.close();
            }
        }

        return null;
    }

    @Override
    protected void onDestroy() {

        if (modelHandle != 0) {
            LlamaBridge.freeModel(modelHandle);
            modelHandle = 0;
        }

        super.onDestroy();
    }
}
