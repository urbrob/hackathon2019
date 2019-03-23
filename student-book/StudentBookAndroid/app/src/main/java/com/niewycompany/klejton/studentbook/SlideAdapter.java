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
            quizJSON = new REST_Integration().execute(quizId, "quiz").get();
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
        }

        container.addView(view);
        return view;
    }

    @Override
    public void destroyItem(ViewGroup container, int position, Object object) {
        container.removeView((LinearLayout)object);
    }
}
