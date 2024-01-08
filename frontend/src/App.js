import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import SurveyForm from './components/SurveyForm';
import SurveyList from './components/SurveyList';
import SurveyAnalytics from './components/SurveyAnalytics';
import ResponseList from './components/ResponseList';
import Login from './components/Login';
import Register from './components/Register';
import './styles/main.css';

function App() {
  const [user, setUser] = useState(null);

  const handleLogin = (userData) => {
    setUser(userData);
  };

  const handleLogout = () => {
    setUser(null);
  };

  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/login">
            <Login onLogin={handleLogin} />
          </Route>
          <Route path="/register">
            <Register />
          </Route>
          <Route path="/create-survey">
            {user ? <SurveyForm /> : <Login onLogin={handleLogin} />}
          </Route>
          <Route path="/surveys">
            {user ? <SurveyList /> : <Login onLogin={handleLogin} />}
          </Route>
          <Route path="/responses">
            {user ? <ResponseList /> : <Login onLogin={handleLogin} />}
          </Route>
          <Route path="/analytics">
            {user ? <SurveyAnalytics /> : <Login onLogin={handleLogin} />}
          </Route>
          <Route path="/" exact>
            {user ? <SurveyList /> : <Login onLogin={handleLogin} />}
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;