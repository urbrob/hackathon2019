package com.niewycompany.klejton.studentbook;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;

public class Studentbook extends AppCompatActivity
{

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_studentbook);
    }

    public void openQuiz(View view)
    {
        Intent intent = new Intent(this, QuizActivity.class);
        String quizId = "hecc";
        intent.putExtra("QUIZ_ID", quizId);
        startActivity(intent);
    }
}
