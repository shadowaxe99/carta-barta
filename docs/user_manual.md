# Olvy User Manual

Welcome to the Olvy User Manual. This document will guide you through the process of using Olvy's Customer Survey Tool.

## Getting Started

### Registration

To use Olvy, you must first register an account:

1. Navigate to the Olvy registration page.
2. Fill in the `registerForm` with your details.
3. Submit the form to create your account.

### Login

After registration, you can log in:

1. Go to the Olvy login page.
2. Enter your credentials in the `loginForm`.
3. Click the login button to access your dashboard.

## Creating Surveys

### Accessing the Survey Creation Form

1. From your dashboard, click on the "Create Survey" button.
2. You will be directed to the `surveyForm`.

### Defining Survey Questions

1. Enter your survey questions and select the response type (multiple choice, open-ended).
2. To support multiple languages, click on the language option and select the desired languages.

### Setting Survey Parameters

1. Specify the expiration date for the survey.
2. Limit the number of responses if necessary.

### Saving the Survey

1. Once you have completed the survey, click the "Save" button.
2. You will receive a `SURVEY_CREATED` message upon successful creation.

## Distributing Surveys

### Email Invitations

1. Select the survey you wish to distribute.
2. Click on the "Distribute" button and choose "Email".
3. Use the `sendEmailInvitation` function to send personalized links to your respondents.

### Embedding on Websites

1. Choose the "Embed" option.
2. Copy the provided HTML code and paste it into your website's source code.

### Sharing on Social Media

1. Select the "Share" option.
2. Choose your preferred social media platform and post the survey link.

## Collecting Responses

Responses are collected in real-time. You can view them by:

1. Navigating to the `responseList` from your dashboard.
2. Clicking on a specific survey to see its responses.

## Analyzing Survey Results

### Accessing Analytics

1. From the dashboard, select the survey you want to analyze.
2. Click on the "Analytics" button to view the analysis.

### Understanding the Analysis

Olvy provides sentiment analysis, keyword extraction, and other analytics features:

1. Sentiment analysis is displayed in a graphical format.
2. Keyword extraction is listed for easy review.

### Generating Reports

1. Click on the "Generate Report" button.
2. The `generateReport` function will create a detailed report of the survey results.

## Integration with Other Tools

### Carta Integration

1. Navigate to the integration settings.
2. Connect your Olvy account with Carta using the `carta_integration.py` script.

### CRM Integration

1. In the integration settings, select your CRM platform.
2. Use the `crm_integration.py` script to sync respondent data.

## Conclusion

Thank you for choosing Olvy. We hope this manual helps you effectively use the Customer Survey Tool to gather and analyze stakeholder feedback. For further assistance, please refer to our `api_documentation.md` and `development_guide.md`.