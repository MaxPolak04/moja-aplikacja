pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Info') {
      steps {
        echo "Gałąź: ${env.BRANCH_NAME}"
        echo "Build: ${env.BUILD_NUMBER}"
      }
    }
    stage('Testy') {
      when {
        expression { env.BRANCH_NAME != 'main' }
      }
      steps {
        sh 'python3 test_app.py'
      }
    }
    stage('Aplikacja') {
      steps {
        sh 'python3 app.py'
      }
    }
  }
  post {
    success {
      echo "OK — gałąź: ${env.BRANCH_NAME}"
    }
    failure {
      echo 'BŁĄD! Sprawdź logi.'
    }
  }
}
