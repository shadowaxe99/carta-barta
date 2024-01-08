// validationUtils.js

const validateEmail = (email) => {
  const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
};

const validatePassword = (password) => {
  // Minimum eight characters, at least one letter and one number:
  const re = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
  return re.test(String(password));
};

const validateSurveyForm = (surveyData) => {
  const { title, questions } = surveyData;
  if (!title || title.trim() === '') {
    return { valid: false, message: 'Survey title is required.' };
  }
  if (!questions || !Array.isArray(questions) || questions.length === 0) {
    return { valid: false, message: 'At least one question is required.' };
  }
  for (let question of questions) {
    if (!question.text || question.text.trim() === '') {
      return { valid: false, message: 'All questions must have text.' };
    }
    if (!question.type || !['multiple choice', 'open-ended'].includes(question.type)) {
      return { valid: false, message: 'Invalid question type.' };
    }
    if (question.type === 'multiple choice' && (!question.options || question.options.length < 2)) {
      return { valid: false, message: 'Multiple choice questions must have at least two options.' };
    }
  }
  return { valid: true, message: 'Survey form is valid.' };
};

export {
  validateEmail,
  validatePassword,
  validateSurveyForm
};