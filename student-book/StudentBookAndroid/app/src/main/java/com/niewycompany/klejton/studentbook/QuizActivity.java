package com.niewycompany.klejton.studentbook;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.os.Handler;
import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Toast;

public class QuizActivity extends AppCompatActivity
{
    private ViewPager viewPager;
    private SlideAdapter myadapter;
    private int currentItem;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        Intent intent = getIntent();
        setContentView(R.layout.activity_quiz);
        viewPager = (ViewPager) findViewById(R.id.viewpager);
        myadapter = new SlideAdapter(this);
        myadapter.quizId = intent.getStringExtra("QUIZ_ID");
        this.currentItem = 0;
        viewPager.setAdapter(myadapter);
    }

    public void buttonPressed(View view)
    {
        if (view.getTag() == "true")
        {
            Toast.makeText(getBaseContext(), "Poprawna odpowiedź!", Toast.LENGTH_LONG).show();
            view.setBackgroundColor(Color.GREEN);
        }
        if (view.getTag() == "false")
        {
            Toast.makeText(getBaseContext(), "Zła odpowiedź!", Toast.LENGTH_LONG).show();
            view.setBackgroundColor(Color.RED);
        }

        final Handler handler = new Handler();
        handler.postDelayed(new Runnable() {
            @Override
            public void run() {
                // Do something after 1s = 1000ms
                int count = viewPager.getAdapter().getCount();
                if(currentItem == count-1)
                {
                    Toast.makeText(getBaseContext(), "Koniec pytań :c", Toast.LENGTH_LONG).show();
                    finish();
                }
                viewPager.setCurrentItem(++currentItem);
            }
        }, 1000);
    }
}
