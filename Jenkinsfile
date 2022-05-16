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
          pip install --upgrade pip -H
          pip install playwright -H
          playwright install
          pip install pytest-playwright -H
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
