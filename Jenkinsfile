pipeline {
  agent {
    docker {
      image 'mcr.microsoft.com/playwright/python:v1.22.0-focal'
    }
  }
  stages {
    stage('install playwright') {
      steps {
        sh '''
          pip -H install --upgrade pip
          pip -H install playwright
          playwright install
          pip -H install pytest-playwright -H
        '''
      }
    }
    stage('test') {
      steps {
        sh '''
          pytest -s -v --tb=short -m auth
        '''
        }
      }
    }
  }
