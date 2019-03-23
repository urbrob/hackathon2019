package com.niewycompany.klejton.studentbook;

import java.util.List;

public class Question
{
    String Id;
    String question;
    Answer[] answers;

    public Question(String id, String question, Answer[] answers)
    {
        Id = id;
        this.question = question;
        this.answers = answers;
    }
}
