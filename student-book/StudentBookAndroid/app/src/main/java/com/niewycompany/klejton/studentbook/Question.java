package com.niewycompany.klejton.studentbook;

public class Question
{
    String pk;
    String description;
    Answer[] answers;

    public Question(String id, String question, Answer[] answers)
    {
        pk = id;
        this.description = question;
        this.answers = answers;
    }
}
