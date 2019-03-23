package com.niewycompany.klejton.studentbook;

import android.os.AsyncTask;

import javax.net.ssl.HttpsURLConnection;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;

public class REST_Integration
{
    public static Question[] getQuestions()
    {
        AsyncTask.execute(new Runnable()
        {
            @Override
            public void run()
            {
                URL restEndpoint = null;
                try
                {
                    restEndpoint = new URL("FUCCMEJERRY");
                }
                catch(MalformedURLException e)
                {
                    //it's fucced
                }

                HttpsURLConnection myConnection = null;
                try
                {
                    myConnection = (HttpsURLConnection) restEndpoint.openConnection();
                }
                catch(IOException e)
                {
                    //it's fucced
                }

                Integer responseCode = 0;
                try
                {
                    responseCode = myConnection.getResponseCode();
                }
                catch(IOException e)
                {
                    //it's fucced
                }

                if (responseCode == 200)
                {
                    // Success
                    // Further processing here
                }
                else
                {
                    // Error handling code goes here
                }
            }
        });
        return null;
    }
}
