package com.niewycompany.klejton.studentbook;

import android.content.Context;
import android.support.v4.view.PagerAdapter;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;
import com.google.gson.Gson;

public class SlideAdapter extends PagerAdapter {
    Context context;
    LayoutInflater inflater;
    String quizId;

    /*Answer a1 = new Answer("1234", "42069","yass", true);
    Answer a2 = new Answer("1235", "42069","nah", false);
    Answer a3 = new Answer("1236", "42069","wat", false);
    Answer a4 = new Answer("1237", "42069","que", false);
    Answer[] answers1 = new Answer[]{a1,a2,a3,a4};

    Answer a5 = new Answer("1238", "69420","yass", false);
    Answer a6 = new Answer("1239", "69420","nah", true);
    Answer a7 = new Answer("1240", "69420","wat", false);
    Answer a8 = new Answer("1241", "69420","que", false);
    Answer[] answers2 = new Answer[]{a5,a6,a7,a8};*/

    String quizJSON;

    public Quiz quiz;

    public Question[] questionList;

    public SlideAdapter(Context context) {
        this.context = context;
    }

    public Boolean requestDone = false;

    @Override
    public int getCount() {
        try
        {
            quizJSON = new REST_Integration().execute(quizId).get();
            requestDone=true;
        }
        catch(Exception e)
        {
            //hecc
        }
        while(requestDone==false)
        {
            //don't
        }

        Gson gson = new Gson();
        Quiz tempQuiz = gson.fromJson(quizJSON,Quiz.class);
        quiz = new Quiz();
        quiz.created_by = tempQuiz.created_by;
        quiz.name = tempQuiz.name;
        quiz.pk = tempQuiz.pk;
        quiz.questions = new Question[tempQuiz.questions.length];
        int i=0;
        for(Question q : tempQuiz.questions)
        {
            if(q.answers.length >= 2 && q.answers.length <= 4 && !q.description.isEmpty())
            {
                quiz.questions[i]=q;
                i++;
            }
        }
        questionList = new Question[i];
        for(int j=0; j<i; j++)
        {
            questionList[j] = quiz.questions[j];
        }
        return questionList.length;
    }

    @Override
    public boolean isViewFromObject(View view, Object object) {
        return (view==(LinearLayout)object);
    }

    @Override
    public Object instantiateItem(ViewGroup container, int position)
    {
        inflater = (LayoutInflater) context.getSystemService(context.LAYOUT_INFLATER_SERVICE);
        View view = inflater.inflate(R.layout.slide,container,false);
        LinearLayout layoutslide = (LinearLayout) view.findViewById(R.id.slidelinearlayout);
        TextView question = (TextView) view.findViewById(R.id.question);
        Button answerA = (Button) view.findViewById(R.id.answerA);
        Button answerB = (Button) view.findViewById(R.id.answerB);
        Button answerC = (Button) view.findViewById(R.id.answerC);
        Button answerD = (Button) view.findViewById(R.id.answerD);
        question.setText(questionList[position].description);
        answerA.setText(questionList[position].answers[0].description);
        answerB.setText(questionList[position].answers[1].description);
        if(questionList[position].answers.length >= 3)
        {
            answerC.setText(questionList[position].answers[2].description);
        }
        else
        {
            answerC.setVisibility(View.GONE);
        }
        if(questionList[position].answers.length == 4)
        {
            answerD.setText(questionList[position].answers[3].description);
        }
        else
        {
            answerD.setVisibility(View.GONE);
            answerC.setX(270);
            answerC.setY(0);
        }

        container.addView(view);
        return view;
    }

    @Override
    public void destroyItem(ViewGroup container, int position, Object object) {
        container.removeView((LinearLayout)object);
    }
}
