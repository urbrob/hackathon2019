package com.niewycompany.klejton.studentbook;

public class Answer
{
    String id;
    String questionId;
    String answer;
    Boolean correct;

    public Answer(String id, String questionId, String answer, Boolean correct)
    {
        this.id = id;
        this.questionId = questionId;
        this.answer = answer;
        this.correct = correct;
    }
}
