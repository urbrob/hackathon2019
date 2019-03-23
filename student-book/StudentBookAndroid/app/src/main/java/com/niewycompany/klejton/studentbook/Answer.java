package com.niewycompany.klejton.studentbook;

public class Answer
{
    String pk;
    String description;
    Boolean is_valid;

    public Answer(String id, String questionId, String answer, Boolean correct)
    {
        this.pk = id;
        this.description = answer;
        this.is_valid = correct;
    }
}
