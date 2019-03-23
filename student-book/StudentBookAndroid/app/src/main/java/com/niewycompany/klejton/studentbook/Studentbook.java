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
        String quizId = "BBBo8j9X";
        intent.putExtra("QUIZ_ID", quizId);
        startActivity(intent);
    }

    public void openFeed(View view)
    {
        Intent intent = new Intent(this, FeedActivity.class);
        String groupId = "hecc";
        intent.putExtra("GROUP_ID", groupId);
        startActivity(intent);
    }

    public void openGroupList(View view)
    {
        Intent intent = new Intent(this, GroupDisplayActivity.class);
        String userId = "XOLPGno";
        intent.putExtra("USER_ID", userId);
        startActivity(intent);
    }
}
