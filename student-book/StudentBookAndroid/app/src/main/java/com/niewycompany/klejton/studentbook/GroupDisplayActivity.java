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

public class GroupDisplayActivity extends ListActivity
{
    String groupsJSON;
    String userId;
    Boolean requestDone = false;
    Map<String,String> quizNameToQuizId = new HashMap<String,String>();
    ArrayList<String> listItems = new ArrayList<String>();
    ArrayAdapter<String> adapter;
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        Intent intent = getIntent();
        this.userId = intent.getStringExtra("USER_ID");

        try
        {
            groupsJSON = new REST_Integration().execute(userId, "groups").get();
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
        Group[] groups = gson.fromJson(groupsJSON,Group[].class);
        for(Group g : groups)
        {
            quizNameToQuizId.put(g.pk,g.name);
            listItems.add(g.name);
        }
        listItems.add("hECC");
        setContentView(R.layout.activity_group_display);
        /*Toolbar myToolbar = (Toolbar) findViewById(R.id.my_toolbar);
        myToolbar.setTitle("Grupy");
        setSupportActionBar(myToolbar);*/
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
    }
}