package com.example.myapplication15;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import android.view.View;
import android.widget.TextView;


public class MainActivity extends AppCompatActivity {


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final TextView txt1 = (TextView) findViewById(R.id.text1);

        Button btnPlus = (Button) findViewById(R.id.buttonPlus);
        Button btnMinus = (Button) findViewById(R.id.buttonMinus);

        btnPlus.setOnClickListener(new Button.OnClickListener() {
            @Override
            public void onClick(View v) {
                Integer res = Integer.parseInt(txt1.getText().toString());
                txt1.setText(String.valueOf(++res));
            }
        });

        btnMinus.setOnClickListener(new Button.OnClickListener() {
            @Override
            public void onClick(View v) {
                Integer res = Integer.parseInt(txt1.getText().toString());
                txt1.setText(String.valueOf(--res));
            }
        });
    }
}
