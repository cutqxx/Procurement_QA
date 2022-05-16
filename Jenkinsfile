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
          pip install playwright
          playwright install
          pip install pytest-playwright
        '''
      }
    }
    stage('help') {
      steps {
        sh 'npx playwright test --help'
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
