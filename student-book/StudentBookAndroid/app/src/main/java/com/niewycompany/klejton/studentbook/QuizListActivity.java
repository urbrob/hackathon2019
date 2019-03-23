package com.niewycompany.klejton.studentbook;

import android.app.ListActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;
import com.google.gson.Gson;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class QuizListActivity extends ListActivity
{
    String quizzesJSON;
    String groupId;
    String userId;
    Boolean requestDone = false;
    Map<Long,String> quizIdToViewId = new HashMap<Long,String>();
    ArrayList<String> listItems = new ArrayList<String>();
    ArrayAdapter<String> adapter;
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        Intent intent = getIntent();
        this.groupId = intent.getStringExtra("GROUP_ID");
        this.userId = intent.getStringExtra("USER_ID");

        try
        {
            quizzesJSON = new REST_Integration().execute(userId, "quizes", groupId).get();
            requestDone=true;
        }
        catch(Exception e)
        {
            //hecc
        }
        while(!requestDone)
        {
            //don't
        }

        Gson gson = new Gson();
        Quiz[] quizes = gson.fromJson(quizzesJSON,Quiz[].class);
        Long i=0L;
        for(Quiz q : quizes)
        {
            quizIdToViewId.put(i,q.pk);
            listItems.add(q.name);
            i++;
        }
        setContentView(R.layout.activity_group_display);
        adapter=new ArrayAdapter<String>(this,
                android.R.layout.simple_list_item_1,
                listItems);
        this.setListAdapter(adapter);
    }

    @Override
    protected void onListItemClick(ListView l, View v, int pos, long id)
    {
        super.onListItemClick(l, v, pos, id);

        Toast.makeText(getBaseContext(),String.valueOf(id) + " fUCKS gIVEN",Toast.LENGTH_SHORT).show();

        Intent intent = new Intent(this, QuizActivity.class);
        String quizId = quizIdToViewId.get(id);
        intent.putExtra("QUIZ_ID", quizId);
        startActivity(intent);
    }
}
