# Olvy API Documentation

Welcome to the Olvy API documentation. This document provides information on how to interact with the API endpoints for Olvy's Customer Survey Tool.

## Base URL

All URLs referenced in the documentation have the following base:

```
${API_URL}
```

## Authentication

To access the API, you will need to authenticate using the `authenticateUser` function. This will provide you with a token that you must include in the header of your requests.

```
POST /api/user/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "yourpassword"
}

Response:
{
  "token": "your-auth-token"
}
```

## Users

### Register a New User

```
POST /api/user/register
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "password": "password123"
}

Response:
{
  "message": "USER_AUTH_SUCCESS",
  "userId": "user-id"
}
```

## Surveys

### Create a New Survey

```
POST /api/survey/create
Content-Type: application/json
Authorization: Bearer your-auth-token

{
  "title": "Customer Satisfaction",
  "questions": [
    {
      "text": "How satisfied are you with our product?",
      "type": "multiple choice",
      "options": ["Very satisfied", "Satisfied", "Neutral", "Unsatisfied", "Very unsatisfied"]
    },
    {
      "text": "Any suggestions for improvement?",
      "type": "open-ended"
    }
  ],
  "language": "en",
  "expiresAt": "2023-12-31T23:59:59Z"
}

Response:
{
  "message": "SURVEY_CREATED",
  "surveyId": "survey-id"
}
```

### Get All Surveys

```
GET /api/survey/all
Authorization: Bearer your-auth-token

Response:
[
  {
    "id": "survey-id",
    "title": "Customer Satisfaction",
    "createdAt": "2023-01-01T00:00:00Z",
    "expiresAt": "2023-12-31T23:59:59Z"
  },
  ...
]
```

## Responses

### Submit a Survey Response

```
POST /api/response/submit
Content-Type: application/json
Authorization: Bearer your-auth-token

{
  "surveyId": "survey-id",
  "responses": [
    {
      "questionId": "question-id",
      "answer": "Very satisfied"
    },
    {
      "questionId": "question-id",
      "answer": "No suggestions"
    }
  ]
}

Response:
{
  "message": "RESPONSE_SUBMITTED",
  "responseId": "response-id"
}
```

### Get Responses for a Survey

```
GET /api/response/survey/{surveyId}
Authorization: Bearer your-auth-token

Response:
[
  {
    "responseId": "response-id",
    "surveyId": "survey-id",
    "answers": [
      {
        "questionId": "question-id",
        "answer": "Very satisfied"
      },
      ...
    ],
    "respondent": "respondent-id",
    "submittedAt": "2023-01-02T00:00:00Z"
  },
  ...
]
```

## Analysis

### Analyze Survey Responses

```
GET /api/analysis/survey/{surveyId}
Authorization: Bearer your-auth-token

Response:
{
  "surveyId": "survey-id",
  "sentimentAnalysis": {
    "positive": 70,
    "neutral": 20,
    "negative": 10
  },
  "keywordExtraction": [
    "quality", "price", "features"
  ],
  "responseRate": 85
}
```

## Errors

The API uses the following error codes:

- `400` Bad Request
- `401` Unauthorized
- `403` Forbidden
- `404` Not Found
- `500` Internal Server Error

## Conclusion

This API documentation covers the main operations related to the Customer Survey Tool. For more detailed information or assistance, please refer to the `docs/user_manual.md` and `docs/development_guide.md`.