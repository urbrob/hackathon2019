package com.niewycompany.klejton.studentbook;

import android.app.ListActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import com.google.gson.Gson;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class GroupDisplayActivity extends ListActivity
{
    String groupsJSON;
    String userId;
    Boolean requestDone = false;
    Map<Long,String> groupIdToViewId = new HashMap<Long,String>();
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
        while(!requestDone)
        {
            //don't
        }

        Gson gson = new Gson();
        Group[] groups = gson.fromJson(groupsJSON,Group[].class);
        Long i=0L;
        for(Group g : groups)
        {
            groupIdToViewId.put(i,g.pk);
            listItems.add(g.name);
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

        Intent intent = new Intent(this, QuizListActivity.class);
        String groupId = groupIdToViewId.get(id);
        intent.putExtra("GROUP_ID", groupId);
        intent.putExtra("USER_ID", this.userId);
        startActivity(intent);
    }
}